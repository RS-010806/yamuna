# `yamuna_encroachment.ipynb`

The executed end-to-end pipeline: 51 cells, 25 of them code, committed with all
outputs intact so that every figure and number in the paper can be traced to the
cell that produced it without re-running anything.

| Stage | Cells | What it does |
|---|---|---|
| 0 Environment | 2 | Sets the working directory and `sys.path`, records the NumPy version |
| A Geospatial foundation | 4 | Rasterizes the real floodplain polygon to the 50 m grid, derives the river centre-line, DEM, slope, HAND and distance fields |
| B Scene synthesis | 6 | Builds the six-epoch, six-band reflectance benchmark and its exact land-cover labels, with irreversible pressure-driven encroachment |
| C Features, RF and SVM | 8 | 17-feature stack; Random Forest and RBF SVM trained north of the split, scored on the shared southern hold-out |
| D CNN | 11, 13 | `src/nn.py` with its gradient check, then training, hold-out scoring and wall-to-wall inference |
| E Change detection | 15 | Transition matrix, per-epoch class areas, encroachment trajectory |
| F Forecasting | 17 | Linear, exponential and logistic areal fits; cellular-automata allocation; hindcast validation |
| Figures | 19, 20 | Writes the 12 figures into `figures/` |
| Tables | 22 to 24 | Summary tables for the paper |
| Display | 26 to 49 | Shows each figure with its caption |

Run the cells in order. Seeds are fixed throughout (`default_rng(42)` in Stage A,
`default_rng(11)` in the CNN stage), so results are deterministic.

## Paths

The notebook is committed exactly as executed. Its first code cell therefore
reads

```python
os.chdir("/home/claude/yamuna"); sys.path.insert(0, "src")
```

and all later paths resolve beneath that directory. Either run
`bash scripts/prepare_workspace.sh` from the repository root, which creates that
path and links `data/`, `src/` and `figures/` into it, or change that one
`os.chdir` argument to your clone. No other absolute path appears anywhere in the
notebook.

Editing the source of an executed cell desynchronizes it from its stored output,
which is why the path is handled outside the notebook rather than inside it.

## Figure numbering

The notebook numbers its figures 1 to 12; the paper numbers the same figures 2 to
13, because the paper adds the framework diagram as its Fig. 1. The mapping table
is in the repository README.
