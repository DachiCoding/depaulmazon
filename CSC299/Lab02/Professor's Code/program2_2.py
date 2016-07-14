import csv

ncols = 4
counters = [0]*ncols

with open('data.csv','r') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        row = map(int,row)
        for c in range(4):
            counters[c] += row[c]

open('sums.csv','w').write(', '.join(map(str,counters)))
