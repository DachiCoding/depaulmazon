import csv
import urllib
import random
from BeautifulSoup import BeautifulSoup as Soup

PREFIX = 'http://www.superherodb.com'
URL = PREFIX+'/characters/'

def get_heroes():
    heroes = []
    html = urllib.urlopen(URL).read()
    soup = Soup(html)
    lis = soup.findAll('li',{'class':'char-li'})

    # for fun!
    random.shuffle(lis)
    lis = lis[:100]
    # end for fun!

    for li in lis:
        a = li.find('a')
        name = a.contents[0].strip()
        href = PREFIX+a['href']
        print name, href
        hero = get_powers(name, href)
        heroes.append(hero)
    return heroes

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

def write_heroes(heroes, filename="superheroes.csv"):
    columns = 'NAME,INTELLIGENCE,STRENGTH,SPEED,DURABILITY,POWER,COMBAT'.split(',')    
    with open(filename,'w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(columns)
        for d in heroes:
            if len(d)==7:
                lst = [d[strength] for strength in columns]
                writer.writerow(lst)
            else:
                print 'ERROR:',d
                  
        
#write_hero(get_powers())
write_heroes(get_heroes())
