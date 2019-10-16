### Input files
* `data/nextstrain_tree_sub{x}.trees` _not committed to this repo_
* `data/location_mapping.csv` _not committed to this repo_

### Augur version
You must use augur branch `beast-v2`.
When augur v6 is released these notes will be updated accordingly.


### Convert lat-longs into auspice-usable format

This script uses `./data/location_mapping.csv` and converts it into an augur-parseable format.

```bash
python scripts/make_lat_longs.py > results/lat_longs.tsv
```

### Parse beast files using augur

```bash
numDate="2017.260" # 2017-04-05
for i in {1..10}; do
  augur import-beast --mcc data/nextstrain_tree_sub1.trees --output-tree results/basel-flu_${i}.new --output-node-data results/basel-flu_${i}_node_data.json --tip-date-format decimal --most-recent-tip-date ${numDate} --recursion-limit 10000;
done;
```


### Modifications to the node-data specific to this analysis
```bash
for i in {1..10}; do
  python scripts/transform_node_data.py results/basel-flu_${i}_node_data.json results/basel-flu_${i}_node_data_transformed.json;
done
```


### Export data for auspice

```bash
for i in {1..10}; do
  augur export v1 --tree results/basel-flu_${i}.new --node-data results/basel-flu_${i}_node_data_transformed.json --auspice-config config/auspice_config.json --output-meta auspice/basel-flu_${i}_meta.json --output-tree auspice/basel-flu_${i}_tree.json --metadata config/metadata.tsv --lat-longs results/lat_longs.tsv;
done
```