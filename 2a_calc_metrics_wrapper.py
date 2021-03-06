#!/usr/bin/env python

import subprocess
import sys
import math

sys.path.append('/home/ubuntu/TOOLS/Scripts/utility')
from job_manager import job_manager

fn = sys.argv[1]
th = sys.argv[2]

# create sub_files to process
lc_info = subprocess.check_output('wc -l ' + fn, shell=True)
fh = open(fn, 'r')
lc = lc_info.split()
line_split = math.ciel(float(lc[0])/float(th))
cur = 1
fct = 1
flist = []
cur_file = fn + str(fct) + 'split'
out_pre = 'Gene_metrics' + str(fct)
out = open(cur_file, 'w')
job_list = []
cmd = '/home/ubuntu/TOOLS/dropseq/2_calc_mean_variance_bin.py '
job_list.append(cmd + cur_file + ' ' + out_pre + ' 0')
head = next(fh)
# out.write(head)
for line in fh:
    if cur > line_split:
        out.close()
        fct += 1
        cur_file = fn + str(fct) + 'split'
        out = open(cur_file, 'w')
        out_pre = 'Gene_metrics' + str(fct)
        job_list.append(cmd + cur_file + ' ' + out_pre)
        cur = 1
        # out.write(head)
    out.write(line)
    cur += 1
out.close()
job_manager(job_list, th)
