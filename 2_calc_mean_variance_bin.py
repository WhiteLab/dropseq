#!/usr/bin/env python

import sys
from statistics import mean
from statistics import variance
import pdb

fn = sys.argv[1]
fh = open(fn, 'r')
head = next(fh)

stats_dict = {}
gm = open('Gene_metrics.txt', 'w')
gm.write('Gene\tmean molecule count\tvariance\tdispersion measure\n')

j = 1
m = 500

for line in fh:
    if j % m == 0:
        sys.stderr.write('Calculating metric for line ' + str(j) + '\n')
    data = line.rstrip('\n').split('\t')
    pdb.set_trace()
    vals = map(float, data[1:])
    stats_dict[data[0]] = {}
    gene_var = variance(vals)
    gene_mean = mean(vals)
    gene_dm = (gene_var/gene_mean)
    stats_dict[data[0]].update({'mean': gene_mean, 'var': gene_var, 'dm': gene_dm})
    gm.write('\t'.join((data[0], gene_mean, gene_var, gene_dm)) + '\n')
    j += 1
gm.close()