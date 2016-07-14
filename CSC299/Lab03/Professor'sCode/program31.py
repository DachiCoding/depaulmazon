import urllib

def main():
    url1 = 'http://mdp.cdm.depaul.edu/csc299/static/data/%s.accounts.csv'
    url2 = 'http://mdp.cdm.depaul.edu/csc299/static/data/%s.expenses.csv'
    
    for url in [url1, url2]:
        data = urllib.urlopen(url % '111').read()
        open(url[-12:],'w').write(data)

main()
