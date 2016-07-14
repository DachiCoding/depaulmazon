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

    total = sum(row[1] for row in data)

    open('amount.1.txt','w').write("%.2f" % total)

if __name__ == '__main__': main()
