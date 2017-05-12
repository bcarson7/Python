#!/bin/python
import os
VU = ''
URL = ''
TESTTIME = ''
TESTNAME = ''
RAMPTIME = ''
HOLDTIME = ''

os.system('clear')

print('Enter the test name')
TESTNAME = raw_input()

print('Enter the load destination including http')
URL = raw_input()

print('Emter the number of virtual users (100 or fewer)')
VU = raw_input()
if int(VU) > 100:
        VU = 100

print('Enter the linear ramp time in minutes')
RAMPTIME = int(raw_input())

print('Enter the total test time in minutes')
TESTTIME = int(raw_input())

HOLDTIME = TESTTIME - RAMPTIME

VU=str(VU)
RAMPTIME=str(RAMPTIME)
TESTTIME=str(TESTTIME)
HOLDTIME=str(HOLDTIME)

F = open(TESTNAME + '.yml','w')
F.write(
"execution:" +"\n"
"- concurrency: " + VU + "\n"
"  ramp-up: " + RAMPTIME + "m" + "\n"
"  hold-for: " + HOLDTIME + "m" + "\n"
"  scenario: " + TESTNAME + "\n"
"\n"
"scenarios:" + "\n"
" " + TESTNAME + ":" + "\n"
"    requests:" + "\n"
"    - " + URL + "\n"
)
F.close()
os.system('bzt ' + TESTNAME + '.yml')
