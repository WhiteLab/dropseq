#!/usr/bin/env python
'''
Written by Miguel Brown, 2016-Apr-27. Create a training set for downstream drop-seq PCA analysis
Usage: ./2_calc_mean_variance_bin.py <table> <out> <hflag>

Arguments:
<table>     table with molecule counts, samples in head, genes as row labels
<out>       output file name rather than stdout
<hflag>     0 if input table has a header row, 0 if not

Options:
-h  prints help.  note that if hlag is 1, it wll not pint the header, you'll have to prepend that to the file yourself
before moving on!
'''
import sys
from statistics import mean
from statistics import variance
from docopt import docopt

args = docopt(__doc__)
fn = args['<table>']
out = args['<out>']
hflag = int(args['<hflag>'])

fh = open(fn, 'r')
if hflag == 1:
    head = next(fh)

stats_dict = {}
gm = open(out, 'w')
if hflag == 1:
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