import re

# Remove as palavras repetidas seguidas (mesmo que em linhas diferentes) de um texto

f = open('repetidas.txt', "r")

content = f.read()
new_content = re.sub(r'\b(\w+)\s+\1\b', r'\1', content)
print(new_content)

f.close()