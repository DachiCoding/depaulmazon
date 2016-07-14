import re
import urllib

def main():
    html = urllib.urlopen('http://www.cdm.depaul.edu/about/Pages/People/Faculty.aspx?ftype=&selectedareataught=&lastnamefilter=ALL&level=').read()

    r = re.compile('mailto\:([\w\@\_\.]*)')
    emails = r.findall(html)
    emails = sorted(set(emails))
    for email in emails:
        print email

main()
