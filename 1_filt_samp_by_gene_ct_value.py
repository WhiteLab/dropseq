#!/usr/bin/env python
# Written by Miguel Brown, 2016-Apr-27.  Takes table with molecule counts, samples in head, genes as row labels and
# a min gene count threshold to use
# Creates training set
import sys

fh = sys.argv[1]
ct = int(sys.argv[2])

table = open(fh, 'r')
head = next(table)

samp = head.rstrip('\n').split('\t')

g_ct = {}
for i in xrange(1, len(samp), 1):
    g_ct[samp[i]] = 0

j=1
m = 500
for info in table:
    if j % m == 0:
        sys.stderr.write('Processing line ' + str(j) + '\n')
    data = info.rstrip('\n').split('\t')
    for i in xrange(1, len(data), 1):
        cur = float(data[i])
        if cur > 0:
            g_ct[samp[i]] += 1
    j += 1
table.close()

ind = []

sys.stdout.write('gene/cell')

s_ct = 0

for i in xrange(1, len(samp), 1):
    if g_ct[samp[i]] >= ct:
        sys.stdout.write('\t' + samp[i])
        s_ct += 1
        ind.append(i)
sys.stdout.write('\n')
sys.stderr.write('Printing values for ' + str(s_ct) + ' cell samples meeting criteria\n')


table = open(fh, 'r')
skip = next(table)
for line in table:
    data = line.rstrip('\n').split('\t')
    sys.stdout.write(data[0])
    for i in ind:
        try:
            sys.stdout.write('\t' + data[i])
        except:
            sys.stderr.write('Index to print excced array size for gene ' + data[0] + '.  Was at ' + str(i) + '\n')
            exit(1)
    sys.stdout.write('\n')
table.close()
