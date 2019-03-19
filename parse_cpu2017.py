#!/usr/bin/python
import commands
import sys
import time
import elasticsearch
import os.path
import csv
import datetime

int1 = open("/home/tester/test-bench/cpu2017/result/CPU2017.001.intrate.refrate.csv", 'r')
for test1 in int1:
    if 'SPECrate2017_int_base' in test1:
        newCSV = open("speccpu.csv", "w")
        newCSV.write(test1)

int2 = open("/home/tester/test-bench/cpu2017/result/CPU2017.003.intrate.refrate.csv", 'r')
for test2 in int2:
    if 'SPECrate2017_int_base' in test2:
        newCSV.write(test2)

int3 = open("/home/tester/test-bench/cpu2017/result/CPU2017.005.intrate.refrate.csv", 'r')
for test3 in int3:
    if 'SPECrate2017_int_base' in test3:
        newCSV.write(test3)

fp1 = open("/home/tester/test-bench/cpu2017/result/CPU2017.002.fprate.refrate.csv", 'r')
for fptest1 in fp1:
    if 'SPECrate2017_fp_base' in fptest1:
        newCSV.write(fptest1)

fp2 = open("/home/tester/test-bench/cpu2017/result/CPU2017.004.fprate.refrate.csv", 'r')
for fptest2 in fp2:
    if 'SPECrate2017_fp_base' in fptest2:
        newCSV.write(fptest2)

fp3 = open("/home/tester/test-bench/cpu2017/result/CPU2017.006.fprate.refrate.csv", 'r')
for fptest3 in fp3:
    if 'SPECrate2017_fp_base' in fptest3:
        newCSV.write(fptest3)
        newCSV.close()
