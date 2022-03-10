import re

texto = "Hello World"

novo_texto = re.sub(r'(\w+) +(\w+)', r'\g<2> \1', texto) # Vai trocar a ordem de Hello e World
# Utilizando \x para obter um grupo apresenta o limite inferior de 0 e superior de 99
# Podemos utilizar \g<x> para contornar esse "problema"
print(novo_texto)