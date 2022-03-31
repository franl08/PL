import sys
import ply.lex as lex


tokens = ["NUM", "PAL"]
literals = ["[", "]", ","] 

t_PAL = r"[a-zA-Z]+"

def t_NUM(t):
    r'\d+'
    t.value = int (t.value) # ao darmos o cast aqui, permitimos que o valor do token passe logo para string e assim não temos de dar cast no parser
    return t

t_ignore = " \n\t\r"

def t_error(t):
    print("Illegal character " + t.value[0])
    
lexer = lex.lex()

import ply.yacc as yacc

def p_lista(p):
    "lista : '[' conteudo ']'"
    p[0] = p[2]
    
def p_conteudo_vazio(p):
    "conteudo : "
    p[0] = []
    
def p_conteudo_elementos(p):
    "conteudo : elementos"
    p[0] = p[1]
    
def p_elementos_single(p):
    "elementos : elem"
    p[0] = [p[1]]
    
def p_elementos_multi(p):
    "elementos : elementos ',' elem"
    p[0] = [p[3]] + p[1]    # desta forma faz o reverse, devido à recursividade do parser, yacc faz bottom up
    
def p_elem_num(p):
    "elem : NUM"
    p[0] = p[1]
#    p.parser.lista.append(p[1]) Isto adiciona tudo à mesma lista, mesmo que seja em listas nested

def p_elem_pal(p):
    "elem : PAL"
    p[0] = p[1]
#    p.parser.lista.append(p[1]) Isto adiciona tudo à mesma lista, mesmo que seja em listas nested
    
def p_elem_lista(p):
    "elem : lista"
    p[0] = p[1]
    
def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
# parser.lista = [] preferível colocar o parser a fazer isto

for line in sys.stdin:
    res = parser.parse(line) # como atribuímos um valor ao p[0], o parser retorna esse valor