#!/usr/bin/env python
# Written by Miguel Brown, 2016-Apr-27.  Takes table with gene metrics and selects for high variability
'''
Written by Miguel Brown, 2016-Apr-27. Bins and normalizes genes for last step in drop-seq training set creation
Prints to stdout, specify > output_file at end!!!
Usage: ./3_bin_norm_sel.py <table> <score>

Arguments:
<table>     table with gene metrics mean, variance and disperion
<score>       Z score cutoff for selection

Options:
-h
'''
import sys
from docopt import docopt
import numpy
from scipy import stats

args = docopt(__doc__)

table = open(args['<table>'], 'r')
score = float(args['<score>'])
nbins = 20

head = next(table)
# get range of dataset to bin
genes = []
means = []
dm = []
for line in table:
    data = line.rstrip('\n').split('\t')
    genes.append(data[0])
    means.append(float(data[1]))
    dm.append(float(data[-1]))
table.close()
# binning done by means
(hist, bins) = numpy.histogram(means, nbins)
pos = numpy.digitize(means, bins)
sys.stderr.write('Bin edges:\n')
for i in bins:
    sys.stderr.write('\t' + str(i) + '\n')
# "Validation" done by dispersion metric!
sys.stdout.write('bin\tgene\tdm\tzscore\n')
for i in xrange(0, len(bins), 1):
    cur = []
    ind = []
    for j in xrange(0, len(pos), 1):
        if pos[j] == i:
            ind.append(j)
            cur.append(dm[j])
    if len(cur) > 1:
        zcur = stats.zscore(cur)
    else:
        sys.stderr.write('Nothing fit into bin ' + str(i) + '\n')
        continue
    flag = 0
    for j in xrange(0, len(cur), 1):
        if zcur[j] >= score:
            sys.stdout.write(str(i) + '\t' + '\t'.join((genes[ind[j]], str(dm[ind[j]]), str(zcur[j]))) + '\n')
            flag = 1
    if flag == 0:
        sys.stderr.write('Nothing variable enough in bin ' + str(i) + '\n')