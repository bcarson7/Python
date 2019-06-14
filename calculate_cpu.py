#!/usr/bin/python3.6
import pandas as pd
#from matplotlib import pyplot as plt
import numpy as np
#import commands
import subprocess
import sys
import elasticsearch
import csv
import os.path
import datetime

VENDOR = sys.argv[1]
TEST_RUN = sys.argv[2]
ES_INDEX = sys.argv[3] + "_cpu"

es = elasticsearch.Elasticsearch(["http://10.22.248.172"],http_auth=("bcarson"),port="9200")
_TYPE = VENDOR.upper() + "x" + TEST_RUN.upper()
server = subprocess.getoutput("hostname")
hostname = server.split(".")

cpu = pd.read_csv("speccpu.csv", usecols=["score"])
print(cpu.info())
int_row1 = cpu.loc[0]
int_row2 = cpu.loc[1]
int_row3 = cpu.loc[2]
fp_row4 = cpu.loc[3]
fp_row5 = cpu.loc[4]
fp_row6 = cpu.loc[5]
cpu_int = np.average([int_row1, int_row2, int_row3]).round(1)
cpu_fp = np.average([fp_row4, fp_row5, fp_row6]).round(1)
print("Avg_INT   ", cpu_int)
print("Avg_FP    ", cpu_fp)

pulled_data = {}
pulled_data["VENDOR"] = VENDOR
pulled_data["TEST_RUN"] = TEST_RUN
pulled_data["SERVER"] = hostname[0]
pulled_data["INT"] = cpu_int
pulled_data["FP"] = cpu_fp
print(pulled_data)
es.index(index=ES_INDEX, doc_type=_TYPE, body=pulled_data)
