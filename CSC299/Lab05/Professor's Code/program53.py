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
    

def parse_properties():
    regex = re.compile('d\:\w+')
    courses = []
    with open('CSC.xml') as myfile:
        xml = myfile.read()
        soup = Soup(xml)

        properties_sets = soup.findAll('m:properties')
        for properties in  properties_sets:
            items = properties.findAll(regex)
            course = {}
            for item in items:
                course[item.name[2:]] = item.text
            courses.append(course)
            print course['subjectid'],course['catalognbr']
        with open('CSC.json','w') as ofile:
            json.dump(courses,ofile)

def main():
    maybe_download_data()
    parse_properties()

if __name__ == '__main__':
    main()
