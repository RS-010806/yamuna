# Input data

## `yfp7_digi.*`: digitized active floodplain, Delhi Yamuna

The only real input to this study. An ESRI shapefile holding one polygon
feature, delineated by the authors from a reclassified satellite-derived raster
of the Delhi reach of the river Yamuna (Palla/Wazirabad in the north to Okhla in
the south).

| Property | Value |
|---|---|
| Geometry | 1 polygon feature |
| CRS | EPSG:32643, WGS 84 / UTM zone 43N |
| Area | 67.70 km² |
| Extent (UTM 43N) | x 713,126 to 729,762 m; y 3,155,773 to 3,194,435 m |
| Extent (approx. WGS 84) | 28.51 to 28.86 °N, 77.18 to 77.36 °E |
| Attributes | `Id`, `gridcode` |
| Sidecar files | `.shx`, `.dbf`, `.prj`, `.cpg`, `.sbn`, `.sbx`, `_shp.xml` |

Stage A of the notebook rasterizes this polygon onto a 50 m analysis grid with a
1,500 m buffer on each side, giving 834 by 393 cells (327,762 cells, of which
28,706 fall inside the floodplain, 71.8 km² at grid resolution). The buffer is
deliberate: it keeps the urban fabric on both banks inside the grid, so the
classifiers are not trained on floodplain pixels alone.

The small difference between the 67.70 km² polygon area and the 71.8 km² grid
area is rasterization at 50 m.

## What is not here

No satellite imagery. The six-epoch, six-band reflectance cube and its land-cover
labels are synthesized by Stage B of the notebook from this polygon and are a
controlled benchmark with exact ground truth, not observed reflectance. The
repository README and Section III-B of the paper state this in full.

## Generated intermediates

Stages A, B, C, D, E and F cache arrays and result dictionaries into this
directory: `*.npy`, `meta.json`, `eval_set.json`, `cnn_results.json`,
`change_results.json`, `forecast_results.json` and `pred/`. They are gitignored
because every one of them is reproducible from the notebook with fixed seeds.
