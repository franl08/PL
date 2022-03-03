import re 
import sys

m = re.compile(r'^(_|\.)\d+[A-Za-z]{3,}_?$')

for line in sys.stdin:
    ans = m.search(line)
    if(ans):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")

