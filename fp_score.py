#!/usr/bin/python
import commands
import sys

FP_TEST = sys.argv[1]

lines = []
#with open("CFP2006.004.ref.txt", "rt") as cfp:
with open(FP_TEST, "rt") as cfp:
        for line in cfp:
                lines.append(line)
                if 'Est. SPECfp(R)_rate_base2006' in line:
                        print(line)
