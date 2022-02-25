import re
import sys

m = re.compile(r'^\((-|\+)?([0-8]\d?(\.\d+)?|90(\.0+)?),\s(-?|\+?)(\d\d?|[01][0-7]?\d?(\.\d+)?|180(\.0+)?)\)$')

for line in sys.stdin:
    ans = m.match(line)
    if(ans):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")
        
