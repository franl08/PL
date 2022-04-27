import re

er = re.compile(r',')
f = open('basic5TXT.txt', 'r')
linesToWrite = ""

for line in f:
    mo = er.search(line)
    if(mo):
        line = line.replace(',', ' , ')
    linesToWrite += line
f.close()

f = open('basic5TXT.txt', 'w')
f.write(linesToWrite)
f.close()