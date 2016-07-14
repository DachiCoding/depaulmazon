from BeautifulSoup import BeautifulSoup as Soup

s = """<select id="subjectFilter"><option value="-1" selected="selected">All Courses</option><option value="ANI">Animation</option><option value="CNS">Computer, Information and Network Security</option><option value="CSC">Computer Science</option><option value="DC">Digital Cinema</option><option value="DMA">Digital Media Arts</option><option value="ECT">E-Commerce Technology</option><option value="EXP">Experience Design</option><option value="GAM">Game Development</option><option value="GD">Graphic Design</option><option value="GPH">Computer Graphics and Motion Technology</option><option value="HCD">Human Centered Design</option><option value="HCI">Human-Computer Interaction</option><option value="HIT">Health Information Technology</option><option value="ILL">Illustration</option><option value="IM">Interactive Media</option><option value="IS">Information Systems</option><option value="ISM">Interactive and Social Media</option><option value="IT">Information Technology</option><option value="LSP">Liberal Studies Program</option><option value="PM">Project Management</option><option value="SE">Software Engineering</option><option value="TDC">Telecommunications</option><option value="TV">Television Production</option><option value="VFX">Visual Effects</option></select>"""

soup = Soup(s)
ids = []
for option in soup.findAll('option'):
    ids.append(option['value'])
print ids
