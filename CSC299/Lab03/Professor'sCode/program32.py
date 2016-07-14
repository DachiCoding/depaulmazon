import csv

def main():
    with open('accounts.csv') as myfile:
        reader = csv.reader(myfile)
        rows = [row for row in reader]
        total = 0
        for row in rows[1:]:
            total += float(row[3][1:])
    with open('balance.txt','w') as myoutfile:
        myoutfile.write('$%.2f' % total)

main()
