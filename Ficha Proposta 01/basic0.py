import re
import sys

hello = re.compile(r'hello')
for line in sys.stdin:
    mObject = hello.match(line);
    if(mObject):
        print("HELLO")
    else:
        print("INVÁLIDO")