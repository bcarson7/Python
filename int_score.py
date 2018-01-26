#!/usr/bin/python
import commands
import sys

INT_TEST = sys.argv[1]

lines = []
#with open("CFP2006.004.ref.txt", "rt") as cfp:
with open(INT_TEST, "rt") as cint:
        for line in cint:
                lines.append(line)
print(lines[57])
