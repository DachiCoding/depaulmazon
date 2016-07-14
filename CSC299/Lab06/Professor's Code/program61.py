import csv
import urllib
from BeautifulSoup import BeautifulSoup as Soup

URL = 'http://www.superherodb.com/characters/'

def main():
    html = urllib.urlopen(URL).read()
    soup = Soup(html)
    names = []
    lis = soup.findAll('li',{'class':'char-li'})
    for li in lis:
        name = li.find('a').contents[0].strip()
        names.append(name)
        print (name)
    with open('names.csv','w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(['NAME'])
        for name in names:
            writer.writerow([name])

main()
