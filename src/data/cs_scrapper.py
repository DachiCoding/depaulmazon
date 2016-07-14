import json
import urllib2
from bs4 import BeautifulSoup

class course():

    def __init__(self,id,title,url):
        self.id = id
        self.title = title
        self.url = url

    def setPreTeacherList(self,teacherList):
        self.teachers = teacherList

    def setDescription(self,desc):
        self.desc = desc

    def __str__(self):
        return self.id + "," + self.title + ": " + self.url

class teacher():

    def __init__(self,name,url):
        self.name = name
        self.url = url

    def __str__(self):
        return self.name + ": " + self.url

#depts = ['CSC']
#urls = [
#    'https://www.cdm.depaul.edu/academics/Pages/CourseSchedule.aspx?department=CSC&quarter=20171&',
#]
#

depts = ['CSC','IS','IT','ECT','HCI']
urls = [
    'https://www.cdm.depaul.edu/academics/Pages/CourseSchedule.aspx?department=CSC&quarter=20171&',
    'https://www.cdm.depaul.edu/academics/Pages/CourseSchedule.aspx?department=IS&quarter=20171&',
    'https://www.cdm.depaul.edu/academics/Pages/CourseSchedule.aspx?department=IT&quarter=20171&',
    'https://www.cdm.depaul.edu/academics/Pages/CourseSchedule.aspx?department=ECT&quarter=20171&',
    'https://www.cdm.depaul.edu/academics/Pages/CourseSchedule.aspx?department=HCI&quarter=20171&'
]

base_url = 'https://www.cdm.depaul.edu'

depts_dict = dict()
courses = []

for i in range(len(depts)):
    depts_dict[depts[i]] = urls[i]

# Loop all department urls
for dept in depts:
    page = urllib2.urlopen(depts_dict[dept])
    soup = BeautifulSoup(page,"lxml")
    soup.prettify()

    # Find all course under the department
    for anchor in soup.findAll(attrs={"class":"course"}):

        for link in anchor.findAll('a',href=True):
            print "Processing " + link["id"]
            course_temp = course(link["id"],link.get_text()[7:].strip(),base_url+link['href'])
            cpage = urllib2.urlopen(course_temp.url)
            csoup = BeautifulSoup(cpage,"lxml")
            csoup.prettify()
            desc_temp = csoup.find(attrs={'class':'CDMPageTitle'}).next_sibling.next_sibling.get_text()[6:]
            course_temp.setDescription(desc_temp)

            # Find all teachers
            teacherDiv = csoup.find(attrs={"id":"previousInstructorList"})
            teacherList = list()
            for i in teacherDiv.findAll('li'):
                teacher_temp = teacher(i.get_text(),base_url+i.find('a')['href'])
                teacherList.append(teacher_temp)
            course_temp.setPreTeacherList(teacherList)
            courses.append(course_temp)

with open('course_data.json','w') as f:
    for i in range(len(courses)):
        json.dump(
        {'id': courses[i].id,
         'title': courses[i].title,
         'desc': courses[i].desc,
         'url': courses[i].url,
         'teachers': [
             {"name":x.name,"url":x.url} for x in courses[i].teachers
         ]
        },f)
        f.write('\n')
