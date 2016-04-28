#!/usr/bin/env python
# Written by Miguel Brown, 2016-Apr-27.  Takes table with gene metrics and selects for high variability
'''
Written by Miguel Brown, 2016-Apr-27. Bins and normalizes genes for last step in drop-seq training set creation
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
import scipy

args = docopt(__doc__)

table = open(args['<table>'], 'r')
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
(hist, bins) = numpy.histogram(means, 20)
pos = numpy.digitize(means, bins)

