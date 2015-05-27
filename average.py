#!/usr/bin/env python

import sys
import argparse
import numpy as np
import scipy as sp
import scipy.stats


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t.ppf((1+confidence)/2., n-1)
    return m, m-h, m+h

parser = argparse.ArgumentParser(description="Compute average and confidence interval")
parser.add_argument('-c', '--col', default=0, type=int, help='Column number - default=0')
parser.add_argument('-i', '--int', default=95, type=float, help='Confidence interval - default=95')

parser.add_argument('file')
args = parser.parse_args()

#i = 0
data=[]
with open(args.file) as file:
    xsum = 0
    xmean = 0
    for  line in file:
        line = line.split()
        data.append(float(line[args.col]))
        #print(i,'  ',data[i])
        #i = i + 1

print(mean_confidence_interval(data,args.int*1.0/100.))



