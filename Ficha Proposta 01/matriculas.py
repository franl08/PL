import re

m = re.compile(r'(\d{2}\.{3}\d{2}\.{3}\d{2}\.{3}\d{2})|(\d{2}-\d{2}-\d{2}-\d{2})|(\d{2}:\d{2}:\d{2}:\d{2})')
f = open('texto.txt', 'r')
nMatriculas = 0

for line in f:
    lista = m.findall(line)
    if(lista):
        nMatriculas += 1

print("Encontradas %d matrículas" % (nMatriculas))