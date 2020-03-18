import re
import os
file = open('README.md',"w")
file.writelines('<p text-align="center"><h1>cracking the coding interview</h1></p>')
file.writelines('<hr/>')
file.writelines('<center><img src="img/img.png" alt="image" /></center>')
file.writelines('<hr/>')
file.writelines('solution for book "cracking the coding interview')
file.writelines('<h2> Index </h2>')

for list in os.walk('.',topdown=True):
    if len(re.findall('\.',list[0])) == 1 and os.path.basename(list[0]) != '.':
        print(list[0])
        file.writelines('<h2>' + ' > '.join(list[0].split('/')[1:]) +'</h2>')
        file.writelines('<br/>')
        file.writelines("<ul>")
        for line in list[2]:
            file.writelines(' <li><a href=" ' + line +'" >'+ os.path.basename(line) + '</a></li>')
        file.writelines("</ul>")
    file.writelines('<hr/>')
file.close()
