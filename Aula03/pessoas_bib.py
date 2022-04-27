import re
# Transforma um nome do tipo Cristiano Ronaldo em Ronaldo, C.
f = open("pessoas.txt", "r")

for line in f:
    line = re.sub(r'(?P<first_letter>\w)\w* (?P<surname>\w+)', r'\g<surname>, \g<first_letter>.', line.strip())
    print(line)
    
f.close()