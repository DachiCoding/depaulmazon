import mechanize
from BeautifulSoup import BeautifulSoup as Soup

def add(a,b):
    br = mechanize.Browser()
    br.open("http://mdp.cdm.depaul.edu/csc299/some_forms/add")
    br.select_form(nr=0)
    br.form['x'] = str(a)
    br.form['y'] = str(b)
    br.submit()
    html = br.response().read()
    soup = Soup(html)
    return soup.find('span',{'class':'answer'}).text


print add(76,98)
