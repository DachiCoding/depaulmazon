import csv

with open('data.csv','r') as myfile:
    reader = csv.reader(myfile)
    for r,row in enumerate(reader):
        row = map(int,row)
        if r==0:
            ncols = len(row)
            counters = [0]*ncols
        for c in range(ncols):
            counters[c] += row[c]

with open('sums.csv','w') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(counters)
