import json
import sys

def search_courses(keywords):
    if not keywords:
        return []
    matching_courses = []
    with open('CSC.json') as myfile:
        courses = json.load(myfile)
        for course in courses:
            text = course['descr']
            if all(k in text for k in keywords):
                matching_courses.append(course)
    return matching_courses

def main():
    keywords = sys.argv[1:]
    matching_courses = search_courses(keywords)
    for course in matching_courses:
        print course['subjectid'], 
        print course['catalognbr'],
        print course['descr']

if __name__ == '__main__':
    main()
