from BeautifulSoup import BeautifulSoup as Soup
import urllib
import hashlib
import os

URL = 'http://mdp.cdm.depaul.edu/csc299/default/accounts?page=%i'

def download(url):
    print 'dowloading...'+url
    return urllib.urlopen(url).read()

def cache_download(url):
    filename =  hashlib.sha1(url).hexdigest()
    if os.path.exists(filename):
        return open(filename).read()
    else:
        html = download(url)
        open(filename,'w').write(html)
        return html

def download_data(page_number=1):
    html = cache_download(URL % page_number)
    soup = Soup(html)
    table = soup.find('table')
    if not table:
        return []
    tbody = table.find('tbody')
    if not tbody:
        return []
    trs = tbody.findAll('tr')    
    data = []
    for tr in trs:
        tds = tr.findAll('td')
        if len(tds)==4:
            data.append([tds[1].text, float(tds[2].text[1:])])

    return data

def download_all_pages():
    page = 1
    data = []
    while True:
        page_data = download_data(page)
        if len(page_data) == 0:
            break
        data = data + page_data
        page += 1
    return data

def main():
    data = download_all_pages()
    total = sum(row[1] for row in data)
    open('amount.total.txt','w').write('%.2f' % total)

if __name__ == '__main__': main()
