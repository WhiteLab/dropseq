#!/usr/bin/env python
'''
Written by Miguel Brown, 2016-May-05. Uses training set table and filtered gene list to create table for PC analysis
Prints to stdout, specify > output_file at end!!!
Usage: ./4_create_pared_table.py <ttable> <gtable>

Arguments:
<ttable>    training table with molecule counts, samples in head, genes as row labels
<gtable>    filtered gene table with zcore cutoffs, etc

Options:
-h
'''
import sys
from docopt import docopt

args = docopt(__doc__)

glist = {}

gfile = open(args['<gtable>'], 'r')
head = next(gfile)
for line in gfile:
    info = line.split('\t')
    glist[info[1]] = 1
gfile.close()

tfile = open(args['<ttable>'])

head = next(tfile)
head = head.rstrip('\n')
print head
for line in tfile:
    info = line.split('\t')
    if info[0] in glist:
        line = line.rstrip('\n')
        print line
tfile.close()
