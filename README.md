### Input files
* `data/nextstrain_tree_sub{x}.trees` _not committed to this repo_
* `data/location_mapping.csv` _not committed to this repo_

### Augur version
Branch `beast-v2`. Commit ``.


### Convert lat-longs into auspice-usable format

```bash
python scripts/make_lat_longs.py > results/lat_longs.tsv
```

### Parse beast file using augur
```bash
augur import-beast --mcc data/nextstrain_tree_sub1.trees --output-tree results/basel-flu_1.new --output-node-data results/basel-flu_1_node_data.json --tip-date-format decimal --most-recent-tip-date 2050 --recursion-limit 10000;
```


### Modifications to the node-data specific to this analysis
```bash
python scripts/transform_node_data.py results/basel-flu_1_node_data.json results/basel-flu_1_node_data_transformed.json
```


### Export data for auspice

```bash
augur export v1 --tree results/basel-flu_1.new --node-data results/basel-flu_1_node_data_transformed.json --auspice-config config/auspice_config.json --output-meta auspice/basel-flu_1_meta.json --output-tree auspice/basel-flu_1_tree.json --metadata config/metadata.tsv --lat-longs results/lat_longs.tsv 
```