#!/usr/bin/env python

import subprocess
import sys

sys.path.append('/home/ubuntu/TOOLS/Scripts/utility')
from job_manager import job_manager

fn = sys.argv[1]
th = sys.argv[2]

# create sub_files to process
lc = subprocess.check_output('wc -l ' + fn, shell=True)
fh = open(fn, 'r')

line_split = int(lc)/int(th)
cur = 1
fct = 1
flist = []
cur_file = fn + str(fct)
out_pre = 'Gene_metrics' + str(fct)
out = open(cur_file, 'w')
job_list = []
cmd = '/home/ubuntu/TOOLS/dropseq/2_calc_mean_variance_bin.py '
job_list.append(cmd + cur_file + ' ' + out_pre)
head = next(fh)
out.write(head)
for line in fh:
    if cur > line_split:
        out.close()
        fct += 1
        cur_file = fn + str(fct)
        out = open(cur_file, 'w')
        out_pre = 'Gene_metrics' + str(fct)
        job_list.append(cmd + cur_file + ' ' + out_pre)
        cur = 1
    out.write(head)
    cur += 1
out.close()
job_manager(job_list, th)