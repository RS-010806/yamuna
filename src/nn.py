"""
Minimal, dependency-free CNN building blocks (NumPy only) for semantic
segmentation. Implements 'same'-padded 2-D convolution via im2col with an
explicit, verified backward pass, ReLU, and pixel-wise softmax cross-entropy,
plus an Adam optimiser. A numerical gradient check validates the conv gradients.

Tensor layout: (N, H, W, C)  channels-last.
"""
import numpy as np


def im2col(x, kh, kw, pad):
    """x:(N,H,W,C) -> cols:(N, H, W, kh*kw*C) with zero padding ('same')."""
    N, H, W, C = x.shape
    xp = np.pad(x, ((0,0),(pad,pad),(pad,pad),(0,0)), mode="constant")
    cols = np.empty((N, H, W, kh, kw, C), dtype=x.dtype)
    for i in range(kh):
        for j in range(kw):
            cols[:, :, :, i, j, :] = xp[:, i:i+H, j:j+W, :]
    return cols.reshape(N, H, W, kh*kw*C)


def col2im(dcols, x_shape, kh, kw, pad):
    """Inverse accumulation of im2col for the backward pass."""
    N, H, W, C = x_shape
    Hp, Wp = H + 2*pad, W + 2*pad
    dxp = np.zeros((N, Hp, Wp, C), dtype=dcols.dtype)
    dcols = dcols.reshape(N, H, W, kh, kw, C)
    for i in range(kh):
        for j in range(kw):
            dxp[:, i:i+H, j:j+W, :] += dcols[:, :, :, i, j, :]
    return dxp[:, pad:pad+H, pad:pad+W, :]


class Conv2D:
    """'same'-padded convolution. Weight W:(kh*kw*Cin, Cout), bias:(Cout,)."""
    def __init__(self, cin, cout, k=3, seed=0):
        rng = np.random.default_rng(seed)
        fan_in = k*k*cin
        self.k, self.pad = k, k//2
        self.W = (rng.standard_normal((fan_in, cout)) * np.sqrt(2.0/fan_in)).astype(np.float32)
        self.b = np.zeros(cout, np.float32)
        self.cin, self.cout = cin, cout

    def forward(self, x):
        self.x_shape = x.shape
        self.cols = im2col(x, self.k, self.k, self.pad)          # (N,H,W,fan_in)
        N, H, W, _ = self.cols.shape
        out = self.cols.reshape(-1, self.cols.shape[-1]) @ self.W + self.b
        return out.reshape(N, H, W, self.cout)

    def backward(self, dout):
        N, H, W, _ = dout.shape
        d2 = dout.reshape(-1, self.cout)
        c2 = self.cols.reshape(-1, self.cols.shape[-1])
        self.dW = c2.T @ d2
        self.db = d2.sum(0)
        dcols = (d2 @ self.W.T).reshape(N, H, W, -1)
        return col2im(dcols, self.x_shape, self.k, self.k, self.pad)

    def params(self):  return [("W", self.W, "dW"), ("b", self.b, "db")]


class ReLU:
    def forward(self, x):
        self.mask = x > 0
        return x * self.mask
    def backward(self, dout):
        return dout * self.mask
    def params(self): return []


def softmax_ce(logits, y, mask=None):
    """logits:(N,H,W,K)  y:(N,H,W) int  mask:(N,H,W) bool. Returns loss, dlogits."""
    N, H, W, K = logits.shape
    z = logits - logits.max(-1, keepdims=True)
    ez = np.exp(z); p = ez / ez.sum(-1, keepdims=True)
    flat_p = p.reshape(-1, K)
    yf = y.reshape(-1)
    if mask is None:
        m = np.ones_like(yf, bool)
    else:
        m = mask.reshape(-1)
    logp = np.log(flat_p[np.arange(len(yf)), yf] + 1e-9)
    loss = -(logp[m]).mean()
    d = flat_p.copy()
    d[np.arange(len(yf)), yf] -= 1.0
    d[~m] = 0.0
    d /= max(m.sum(), 1)
    return loss, d.reshape(N, H, W, K), p


class Adam:
    def __init__(self, layers, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
        self.layers, self.lr, self.b1, self.b2, self.eps = layers, lr, b1, b2, eps
        self.t = 0
        self.m, self.v = {}, {}
        for li, L in enumerate(layers):
            for name, p, _ in L.params():
                self.m[(li,name)] = np.zeros_like(p)
                self.v[(li,name)] = np.zeros_like(p)

    def step(self):
        self.t += 1
        for li, L in enumerate(self.layers):
            for name, p, gname in L.params():
                g = getattr(L, gname)
                key = (li, name)
                self.m[key] = self.b1*self.m[key] + (1-self.b1)*g
                self.v[key] = self.b2*self.v[key] + (1-self.b2)*(g*g)
                mhat = self.m[key]/(1-self.b1**self.t)
                vhat = self.v[key]/(1-self.b2**self.t)
                p -= self.lr * mhat/(np.sqrt(vhat)+self.eps)


# ---------------------------------------------------------------- gradient check
if __name__ == "__main__":
    rng = np.random.default_rng(1)
    x = rng.standard_normal((2, 5, 5, 3)).astype(np.float64)
    conv = Conv2D(3, 4, k=3, seed=0); conv.W = conv.W.astype(np.float64); conv.b = conv.b.astype(np.float64)
    y = rng.integers(0, 4, size=(2, 5, 5))
    def loss_of(x):
        out = conv.forward(x); l,_,_ = softmax_ce(out, y); return l
    # analytic grad wrt x
    out = conv.forward(x); l, dout, _ = softmax_ce(out, y); dx = conv.backward(dout)
    # numeric grad wrt x
    eps = 1e-5; num = np.zeros_like(x)
    it = np.nditer(x, flags=["multi_index"])
    while not it.finished:
        idx = it.multi_index
        old = x[idx]; x[idx] = old+eps; lp = loss_of(x)
        x[idx] = old-eps; lm = loss_of(x); x[idx] = old
        num[idx] = (lp-lm)/(2*eps); it.iternext()
    rel = np.abs(dx-num).max()/(np.abs(dx).max()+np.abs(num).max()+1e-12)
    print(f"Conv dX grad-check max rel err = {rel:.2e}  ({'OK' if rel<1e-5 else 'FAIL'})")
    # check dW
    out = conv.forward(x); l, dout, _ = softmax_ce(out, y); conv.backward(dout); dW = conv.dW.copy()
    numW = np.zeros_like(conv.W)
    it = np.nditer(conv.W, flags=["multi_index"])
    while not it.finished:
        idx = it.multi_index
        old = conv.W[idx]; conv.W[idx]=old+eps; lp=loss_of(x)
        conv.W[idx]=old-eps; lm=loss_of(x); conv.W[idx]=old
        numW[idx]=(lp-lm)/(2*eps); it.iternext()
    relW = np.abs(dW-numW).max()/(np.abs(dW).max()+np.abs(numW).max()+1e-12)
    print(f"Conv dW grad-check max rel err = {relW:.2e}  ({'OK' if relW<1e-5 else 'FAIL'})")
