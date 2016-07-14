import os
import json
import urllib
import urllib2
from bs4 import BeautifulSoup

with open('teacher_data.json','r') as teacher_data:
    for line in teacher_data:
        teacher_info = json.loads(line)
        teacher_name = teacher_info['name'].replace(" ","_")
        urllib.urlretrieve(teacher_info['imgurl'], "img/" + os.path.basename(teacher_name)+".jpeg")
