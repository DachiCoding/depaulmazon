import csv
import collections

def main():
    with open('accounts.csv') as myfile:
        reader = csv.reader(myfile)
        accounts = [row for row in reader]

    with open('expenses.csv') as myfile:
        reader = csv.reader(myfile)
        rows = [row for row in reader]
        d = collections.defaultdict(float)
        for row in rows[1:]: 
            user_id = row[0]
            transaction_amount =  float(row[1][1:])
            d[user_id] += transaction_amount

    # 
    with open('results.csv','w') as myoutfile:
        writer = csv.writer(myoutfile)
        writer.writerow(['USER_ID', 'FIRST_NAME', 
                         'LAST_NAME', 'BEGIN_BALANCE', 'END_BALANCE'])
        for row in accounts[1:]:
            user_id = row[0]
            first_name = row[1]
            last_name = row[2]
            beginning_balance = float(row[-1][1:])
            total_transactions = d[user_id]
            end_balance = beginning_balance - total_transactions
            writer.writerow([user_id, first_name, last_name, 
                             '$%.2f' % beginning_balance, 
                             '$%.2f' % end_balance])

main()
