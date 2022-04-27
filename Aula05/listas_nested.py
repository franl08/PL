import sys

# ANALISADOR LÉXICO

import ply.lex as lex

# tokens = ["PA", "PF", "NUM", "PAL"]

tokens = ["NUM", "PAL"]
literals = ["[", "]", ","] # define uma regra de token criada de forma automática para eles [só pode ser 1 caractere!], podemos depois adicioná-los às gramáticas sem keywords

# t_PA = r"\["
# t_PF = r"\]"
t_NUM = r"\d+"
t_PAL = r"[a-zA-Z]+"

t_ignore = " \n\t\r";

def t_error(t):
    print("Illegal character " + t.value[0]) # quando dá erro, o valor que guarda é desde o caractere que dá erro até ao fim da string
    
lexer = lex.lex()

## VAMOS AGORA PARA O ANALISADOR SINTÁTICO

import ply.yacc as yacc  # utiliza estratégia bottom up, logo, a recursividade à esquerda é mais eficiente

# o espaço antes dos : é obrigatório
# quando é vazio, não se coloca nada
# o nome dos símbolos terminais tem de ser igual ao nome dos tokens

#def p_grammar(p):
#    """
#    lista : PA elementos PF
    
#    elementos : 
#              | elem elementos
    
#    elem : NUM
#         | PAL
#    """

def p_grammar(p):
    """
    lista : '[' conteudo ']'
    
    conteudo :
             | elementos
    
    elementos : elem
              | elementos ',' elem
    
    elem : NUM
         | PAL
         | lista
    """

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()


for line in sys.stdin:
    parser.parse(line)
