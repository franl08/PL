import re

er = re.compile(r'hello');
f = open('basic3TXT.txt', 'r')
linesToWrite = ""

for line in f:
    mo = er.search(line)
    if(mo):
        line = line.replace('hello', '*YEP*')
    linesToWrite += line        
f.close()

f = open('basic3TXT.txt', 'w')
f.write(linesToWrite)
f.close()