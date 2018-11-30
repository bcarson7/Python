import csv
import numpy as np
exampleFile = open('CFP2006.002.ref.csv')
cpuint = csv.reader(exampleFile)
for row in cpuint:
    if 'ref iteration #1' in row:
        iterate1 = (row[2])
        #iterate1 = int(iterate1)
    if 'ref iteration #2' in row:
        iterate2 = (row[2])
    if 'ref iteration #3' in row:
        iterate3 = (row[2])
        #workload_avg = (float(iterate1)+float(iterate2)+float(iterate3))/3
        workload_median = np.median([float(iterate1),float(iterate2),float(iterate3)])
        print(row[0], workload_median)
