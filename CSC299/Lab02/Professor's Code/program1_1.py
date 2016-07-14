import csv
from random import randint

with open('data.csv','w') as myfile:
    writer = csv.writer(myfile)
    for k in range(1000):
        row = [randint(0,1000) for i in range(4)]
        writer.writerow(row)

