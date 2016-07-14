import os
import csv

counters = {}
filenames = os.listdir('/bin')
for filename in filenames:
    length = len(filename)
    if not length in counters:
        counters[length] = 1
    else:
        counters[length] += 1
#    print filename, counters

with open('bincount.csv','w') as myfile:
    writer = csv.writer(myfile)
    for key in sorted(counters):
        writer.writerow([key, counters[key]])
