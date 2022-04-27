import re 
import sys

er = re.compile('[Hh][Ee][Ll][Oo]')

for line in sys.stdin:
    mo = er.findall(line);
    if(mo):
        print("FOUND:")
        print(mo)
    else:
        print("INVÁLIDO")