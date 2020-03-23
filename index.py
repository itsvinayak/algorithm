import re
import os
file = open('README.md',"w")
file.writelines('<p text-align="center"><h1>cracking the coding interview</h1></p>')

file.writelines('<center><img src="img/img.png" alt="image" /></center>')
file.writelines('<hr/>')
file.writelines('solution for book "cracking the coding interview')
file.writelines('<p text-align="center"><h2> Index </h2></p>')

for list in os.walk('.',topdown=True):
    if len(re.findall('\.',list[0])) == 1 and os.path.basename(list[0]) not in ['.','img','book','python']:
        print(list[0])
        file.writelines('<h2>' + ' --> '.join(list[0].split('/')[1:]) +'</h2>')
        file.writelines('<br/>')
        file.writelines("<ul>")
        for dir in list[2]:
            file.writelines(' <li><a href=" .' + list[0][1:] +' " >'+ os.path.basename(dir) + '</a></li>')
        file.writelines("</ul>")
        file.writelines('<br/>')
file.close()