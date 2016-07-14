import urllib

def download(url):
    return urllib.urlopen(url).read()

URL = 'http://mdp.cdm.depaul.edu/csc299/default/accounts?page=1'

def main():    
    html = download(URL)
    with open('accounts.1.html','w') as myfile:
        myfile.write(html)

if __name__=='__main__':
    main()
