import urllib
import os
import re
import json
from BeautifulSoup import BeautifulSoup as Soup

URL = "http://odata.cdm.depaul.edu/Cdm.svc/Courses?$orderby=CatalogNbr&$filter=EffStatus%20eq%20%27A%27%20and%20SubjectId%20eq%27CSC%27"

def maybe_download_data():
    if not os.path.exists('CSC.xml'):
        xml = urllib.urlopen(URL).read()
        with open('CSC.xml','w') as myfile:
            myfile.write(xml)
    
    
def print_first_set_of_properties():
    with open('CSC.xml') as myfile:
        xml = myfile.read()
        soup = Soup(xml)
        properties = soup.find('m:properties')
        if properties:
            with open('CSC.properties.1.xml','w') as ofile:
                ofile.write(str(properties)[15:-16])

def parse_properties():
    regex = re.compile('d\:\w+')
    with open('CSC.xml') as myfile:
        xml = myfile.read()
        soup = Soup(xml)
        properties = soup.find('m:properties')
        items = properties.findAll(regex)
        course = {}
        for item in items:
            course[item.name[2:]] = item.text
        with open('CSC.properties.1.json','w') as ofile:
            json.dump(course,ofile)

def main():
    maybe_download_data()
    # print_first_set_of_properties()
    parse_properties()

if __name__ == '__main__':
    main()
