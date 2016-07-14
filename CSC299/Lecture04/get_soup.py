import urllib
from BeautifulSoup import BeautifulSoup as Soup

html = urllib.urlopen('http://www.cdm.depaul.edu/about/Pages/People/Faculty.aspx?ftype=&selectedareataught=&lastnamefilter=ALL&level=').read()

soup = Soup(html)
for item  in soup.findAll('li'):
    try:
        a_items = item.findAll('a')
        print a_items[0].text, a_items[1]['href'][7:]
    except:
        pass
