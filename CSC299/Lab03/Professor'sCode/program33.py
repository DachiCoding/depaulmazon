import csv
import collections

def main():
    with open('expenses.csv') as myfile:
        reader = csv.reader(myfile)
        rows = [row for row in reader]
        d = collections.defaultdict(float)
        for row in rows[1:]: 
            account_id = row[0]
            transaction_amount =  float(row[1][1:])
            d[account_id] += transaction_amount

    with open('totals.csv','w') as myoutfile:
        writer = csv.writer(myoutfile)
        writer.writerow(['USER_ID', 'TOTAL_EXPENSE'])
        for account_id in sorted(d):
            writer.writerow((account_id, '$%.2f' % d[account_id]))

main()
