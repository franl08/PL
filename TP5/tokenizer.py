import ply.lex as lex # apenas o módulo léxico da biblioteca ply
import sys

# A biblioteca depende de certas vars definidas no ficheiro, logo, temos de dar o nome
# específico que a biblioteca quer às vars

# a * (2 + 4)
# ID OP PA NUM OP NUM PF

# NUM -> \d+
# OP -> [+\-*/] -> talvez seja mais correto ter um token separado para cada operação
# ID -> [a-zA-Z]\w*
# PA -> \(
# PF -> \)

# Lista de tokens que a linguagem vai ter (Notação obrigatória)
tokens = ["NUM", "ID", "OP"]

# Associar as expressões regulares aos seus tokens (Notação obrigatória [t_<nome_do_token>])
# Sem especificarmos a ordem, o ply procura as expreg de forma prioritária dada pelo seu tamanho
t_ID = r'\[a-zA-Z]\w*'
t_OP = r'[+\-*/]'
t_PA = r'\('
t_PF = r'\)'

# Para especificarmos a ordem, podemos definir as regras em forma de funções
# A prioridade será dada pela ordem das funções
def t_NUM(t):
    r'\d+' # logo a seguir à definição da função é preciso especificar a expressão regular
    print("Encontrei um número") # sempre que encontra um número escreve esta string
    t.value = int(t.value) # passa a string do número para a sua versão inteira
    return t # devolve o token

# Podemos querer ignorar algumas coisas, como, por exemplo, espaços (Notação obrigatória)
t_ignore = " \n\t" # ignora os espaços e os \n

# O que é que o analisador faz quando recebe um token inesperado (Notação obrigatória)
def t_error(t):
    value = t.value[0] # t.value devolve todos os caracteres desde que deu erro até ao fim, mas queremos apenas o que deu erro
    pos = (t.lineno, t.lexpos)
    print(f"Illegal character '{value}' at position '{pos}'")
    exit() # sai do programa

# Criar o analisador léxico
lexer = lex.lex()

# PARA TESTAR

for line in sys.stdin:
    lexer.input(line) # lexer recebe o input
    # Temos agora de percorrer token a token para verificar se existe algum erro
    for tok in lexer: # o lexer acaba por funcionar como uma "lista"
        print(tok)