#!/usr/bin/env python
'''
Written by Miguel Brown, 2016-Apr-27. Create a training set for downstream drop-seq PCA analysis
Usage: ./2_calc_mean_variance_bin.py <table> <out>

Arguments:
<table>     table with molecule counts, samples in head, genes as row labels
<out>       output file name rather than stdout

Options:
-h
'''
import sys
from statistics import mean
from statistics import variance
from docopt import docopt

args = docopt(__doc__)
fn = args['<table>']
out = args['<out>']
fh = open(fn, 'r')
head = next(fh)

stats_dict = {}
gm = open(out, 'w')
gm.write('Gene\tmean molecule count\tvariance\tdispersion measure\n')

j = 1
m = 500

for line in fh:
    if j % m == 0:
        sys.stderr.write('Calculating metric for line ' + str(j) + '\n')
    data = line.rstrip('\n').split('\t')
    vals = map(float, data[1:])
    stats_dict[data[0]] = {}
    gene_var = variance(vals)
    gene_mean = mean(vals)
    gene_dm = 0
    if gene_mean > 0:
        gene_dm = (gene_var/gene_mean)
    stats_dict[data[0]].update({'mean': gene_mean, 'var': gene_var, 'dm': gene_dm})
    gm.write('\t'.join((data[0], str(gene_mean), str(gene_var), str(gene_dm))) + '\n')
    j += 1
gm.close()