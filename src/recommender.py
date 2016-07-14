import csv
import json
import numpy
import random

class profile():
    def __init__(self,major,level,concen):
        self.major = major
        self.level = level
        self.concen = concen

def load_tdidf():

    tdidf = []
    with open('data/tdidf.csv','r') as tdidf_file:
        reader = csv.reader(tdidf_file,delimiter=',')
        for line in reader:
            tdidf.append([float(x) for x in line])
    return tdidf

def load_cosSim():

    cosSim = []
    with open('data/tdidf_sim.csv','r') as tdidf_file:
        reader = csv.reader(tdidf_file,delimiter=',')
        for line in reader:
            cosSim.append([float(x) for x in line])
    return cosSim

def load_course():

    courses = []
    with open('data/course_data.json') as course_json:
        for line in course_json:
            courses.append(json.loads(line))
    return courses

def load_teacher():

    teachers = []
    with open('data/teacher_data.json') as teacher_json:
        for line in teacher_json:
            teachers.append(json.loads(line))
    return teachers

def load_keywords():

    kw = dict()
    with open('data/keywords.txt') as file:
        for line in file:
            kw_arr = line.split(",")
            kw[kw_arr[0]]=int(kw_arr[1][:-1])
    return kw

def profileOptions():
    majors = [
        {'name':'PA','group':'group1'},
        {'name':'IS','group':'group1'},
        {'name':'CS','group':'group1'},
        {'name':'ECT','group':'group1'},
    ]

    levels = [
        {'name':'undergraduate','group':'group2'},
        {'name':'graduate','group':'group2'}
    ]
    return majors,levels

def recConcentrations(major):
    concens = []
    with open('data/concentrations.json') as concen_json:
        for line in concen_json:
            concen_data = json.loads(line)
            if concen_data['major'] == major:
                concens =  concen_data['concentrations']
    concens = [str(x) for x in concens]
    return concens

def recCourseTeachers(userProfile):

    # load userProfile
    level = userProfile.level
    concens = userProfile.concen

    # load data
    tdidf = numpy.array(load_tdidf())
    cosSim = numpy.array(load_cosSim())
    keywords = load_keywords()
    courses = load_course()
    teachers = load_teacher()
    teachers_all_name = [x['name'] for x in teachers]

    # Select course based on the level and concentrations
    '''
    1.Select courses with high value on the specified concentration column
    2.Select similar courses of the courses selected in step 1
    3.Select course < 400 for undergraduate and >= 400 for graduate students
    4.Select teachers that has taught the course selected in step 1 and 2
    '''

    courseIds = set()
    teacherIds = set()
    course_selected = []
    teacher_selected = []
    course_selected_idx = []
    teacher_selected_idx = []

    # Select courses
    for c in concens:
        concenIdx = int(keywords[c])

        # Select top 5 courses based on tdidf
        topCourseIdxs = numpy.argsort(tdidf[:,concenIdx])[-5:]
        courseIds = courseIds.union(set(topCourseIdxs))

        for idx in topCourseIdxs:

            # Select top 5 similar course for each course based on cosSim
            simCourseIdxs = numpy.argsort(cosSim[:,idx])[-5:]
            courseIds = courseIds.union(set(simCourseIdxs))


    # Filter course based on level
    for i in courseIds:
        courseNum = int(courses[i]['id'][-3:])
        if level == 'undergraduate' and courseNum < 400:
            course_selected_idx.append(i)
        elif level == 'graduate' and courseNum >= 400:
            course_selected_idx.append(i)
        elif level == "":
            course_selected_idx.append(i)

    # Pick 4 random courses from the eligible course ids
    course_selected_idx_pick = random.sample(range(len(course_selected_idx)), 4)
    course_selected_idx = [course_selected_idx[x] for x in course_selected_idx_pick]

    # Pick 4 teachers based on the selected course
    for i in course_selected_idx:
        teachers_temp = courses[i]['teachers']
        teachers_temp = [x['name'] for x in teachers_temp]
        for j in teachers_temp:
            teacherIds.add(teachers_all_name.index(j))

    teacher_selected_idx = list(teacherIds)
    teacher_select_idx_pick = random.sample(range(len(teacher_selected_idx)),4)
    teacher_selected_idx = [teacher_selected_idx[x] for x in teacher_select_idx_pick]

    for i in course_selected_idx:
        course_selected.append(courses[i])

    for i in teacher_selected_idx:
        teacher_selected.append(teachers[i])

    return course_selected, teacher_selected




