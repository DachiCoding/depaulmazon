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
        print name
    with open('names.csv','w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(['NAME'])
        for name in names:
            writer.writerow([name])

def get_powers(name="Superman",
               url = 'http://www.superherodb.com/superman/10-791/'):
    d = {}
    html = urllib.urlopen(url).read()
    soup = Soup(html)
    cblock = soup.find('div',{'class':'cblock'})
    items = cblock.findAll('div',{'class':'gridbarholder'})
    for item in items:
        label = item.find('div',{'class':'gridbarlabel'})
        pb = item.find('div',{'role':'progressbar'})
        d[label.text.upper()] = int(pb['aria-valuenow'])
    d["NAME"] = name
    return d

def write_hero(d, filename="superman.csv"):
    columns = 'NAME,INTELLIGENCE,STRENGTH,SPEED,DURABILITY,POWER,COMBAT'.split(',')    
    with open(filename,'w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(columns)
        lst = [d[strength] for strength in columns]
        writer.writerow(lst)
                          
write_hero(get_powers())
