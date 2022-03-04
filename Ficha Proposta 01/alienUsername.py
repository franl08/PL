import re 
import sys

m = re.compile(r'^(_|\.)\d+[A-Za-z]{3,}_?$')
f = open ("ips.txt", "r")
for line in f:
    ans = m.search(line)
    if(ans):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")

