from program41 import download, URL
from BeautifulSoup import BeautifulSoup as Soup

#html = download(URL)
def main():
    html = open('accounts.1.html').read()
    soup = Soup(html)
    table = soup.find('table')
    trs = table.find('tbody').findAll('tr')
    
    data = []
    for tr in trs:
        tds = tr.findAll('td')
        data.append([tds[1].text, float(tds[2].text[1:])])
    data = dict(data)
        
    amount = data['Luise Carpentier']
    open('amount.luise.txt','w').write("%.2f" % amount)

if __name__ == '__main__': main()
