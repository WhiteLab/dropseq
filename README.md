# Dropseq Clustering Preprocessing
## Installation requirements:
The req.txt file has all the python packages needed to run the scripts
```
sudo pip install -r req.txt
```

## Running preprocessing scripts
#### 1_filt_samp_by_gene_ct_value.py
Usage: ./1_filter_table_by_gene_ct_value.py \<table\> \<ct\> \> 1_output_filename.txt 2\> filter.log
(log will have status updates on where it is in the file)
EXAMPLE:
```
./1_filter_table_by_gene_ct_value.py dropseq_all.txt 900 > dropseq_training.txt 2> filter.log
```
Arguments:
<table>     table with molecule counts, samples in head, genes as row labels
<ct>        min gene count threshold for sample inclusion

#### 2_calc_mean_variance_bin.py

Usage: ./2_calc_mean_variance_bin.py \<table\> \<out\> \<hflag\> 2\> metrics.log
(log will have progress of script)
EXAMPLE: 
```
./2_calc_mean_variance_bin.py dropseq_training.txt dropseq_metrics.txt 1 2> metric.log
```
Arguments:
<table>     table with molecule counts, samples in head, genes as row labels (table from step one)
<out>       output file name rather than stdout
<hflag>     0 if input table has a header row, 0 if not

#### 3_bin_norm_sel.py

Usage: ./3_bin_norm_sel.py \<table\> \<score\> 2\> bin.log
(log will have progress and brief description of statistical output)
EXAMPLE:
```
./3_bin_norm_sel.py dropseq_metrics.txt 1.7 2> select.log
```
Arguments:
<table>     table with gene metrics mean, variance and disperion
<score>       Z score cutoff for selection

Options:
-h

#### TODO
This script is forthcoming, will use samples from first output, genes from last output to create table for PCA