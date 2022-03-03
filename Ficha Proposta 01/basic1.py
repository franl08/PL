import re
import sys

er = re.compile(r'hello')

for line in sys.stdin:
    mo = er.search(line)
    if(mo):
        print("HELLO");
    else:
        print("INVÁLIDO");