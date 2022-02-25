import re
import sys

ipv4 = re.compile(r'^(([0-1]?\d{0,2}|2[0-4]\d|25[0-5]|2\d?)\.){3}[0-1]?\d{0,2}|2[0-4]\d|25[0-5]|2\d$')
ipv6 = re.compile(r'^([0-9A-Za-z]{4}\:){7}[0-9A-Za-z]{4}$')

for line in sys.stdin:
    ans = ipv4.match(line)
    ans6 = ipv6.match(line)
    if(ans):
        print("Endereço IPV4")
    else:
        ans6 = ipv6.match(line)
        if(ans6):
            print("Endereço IPV6")
        else:
            print("INVÁLIDO")
