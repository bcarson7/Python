#!/usr/bin/python
import commands
import sys
import time
import elasticsearch
import os.path
import csv
import datetime

int_files = ["CPU2017.001.intrate.refrate.csv", "CPU2017.003.intrate.refrate.csv", "CPU2017.005.intrate.refrate.csv"]
fp_files = ["CPU2017.002.fprate.refrate.csv", "CPU2017.004.fprate.refrate.csv", "CPU2017.006.fprate.refrate.csv"]

def open_int(x):
    cpufile = open("/home/tester/test-bench/cpu2017/" + int_files[x])
    for line in cpufile:
        if 'SPECrate2017_int_base' in line:
            newCSV = open("speccpu.csv", "a")
            newCSV.write(line)
            #newCSV.close()

def open_fp(x):
    cpufile = open("/home/tester/test-bench/cpu2017/" + fp_files[x])
    for line in cpufile:
        if 'SPECrate2017_fp_base' in line:
            newCSV = open("speccpu.csv", "a")
            newCSV.write(line)
            #newCSV.close()

open_int(0)
open_int(1)
open_int(2)
open_fp(0)
open_fp(1)
open_fp(2)
