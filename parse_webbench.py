#!/usr/bin/python
import commands
import sys
import time
import elasticsearch
import os.path
import csv
import datetime

webbench_files = ["dell26_r740_bios2211_phoronix_1", "dell26_r740_bios2211_phoronix_2", "dell26_r740_bios2211_phoronix_3"]

def add_header():
    newCSV = open("webbench.csv", "a")
    newCSV.write("benchmark,score,null,other\n")
    newCSV.close()

def parse_ab(x):
    webfile = open("/home/tester/test-bench/" + webbench_files[x])
    for line in webfile:
        if 'Requests Per Second' in line:
            newCSV = open("webbench.csv", "a")
            newCSV.write(line)
            newCSV.close()

def parse_php(x):
    webfile = open("/home/tester/test-bench/" + webbench_files[x])
    for line in webfile:
        if 'Score' in line:
            newCSV = open("webbench.csv", "a")
            newCSV.write(line)
            newCSV.close()

add_header()
parse_ab(0)
parse_ab(1)
parse_ab(2)
parse_php(0)
parse_php(1)
parse_php(2)
