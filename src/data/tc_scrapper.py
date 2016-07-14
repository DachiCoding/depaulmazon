import json
import urllib2
from bs4 import BeautifulSoup

class teacherClass():
    def __init__(self,name,url,title,dept,imgurl):
        self.name = name
        self.url = url
        self.title = title
        self.dept = dept
        self.imgurl = imgurl

base_url = 'https://www.cdm.depaul.edu'
teachers_url = 'https://www.cdm.depaul.edu/Faculty-and-Staff/Pages/Faculty.aspx?ftype=&selectedareataught=&lastnamefilter=ALL&level=-1'

page = urllib2.urlopen(teachers_url)
soup = BeautifulSoup(page,"lxml")
soup.prettify()

teachers_list = []

teachers = soup.find(attrs={'id':'facultyList'})
for teacher in teachers.findAll('li'):
    name = teacher.find('img')['alt']
    print "Processing " + name
    imgurl = teacher.find('img')['src']
    url = base_url + teacher.findAll('a')[0]['href']
    title = teacher.find(attrs={"class":"facultyTitle"}).get_text()
    dept = teacher.find(attrs={"class":"facultyTitle"}).next_sibling.next_sibling.get_text()
    teacher_ins = teacherClass(name,url,title,dept,imgurl)
    teachers_list.append(teacher_ins)

with open('teacher_data.json','w') as f:
    for i in range(len(teachers_list)):
        json.dump(
        {'name': teachers_list[i].name,
         'url': teachers_list[i].url,
         'title': teachers_list[i].title,
         'dept': teachers_list[i].dept,
         'imgurl': teachers_list[i].imgurl
        },f)
        f.write('\n')