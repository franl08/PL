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
    
def p_conteudo_vazio(p):
    "conteudo : "
    
def p_conteudo_elementos(p):
    "conteudo : elementos"
    
def p_elementos_single(p):
    "elementos : elem"
    
def p_elementos_multi(p):
    "elementos : elementos ',' elem"
    
def p_elem_num(p):
    "elem : NUM"
#   p.parser.soma += int (p[1]) # preciso dar cast porque o p é lido como string
    p.parser.soma += p[1]

def p_elem_pal(p):
    "elem : PAL"
    
def p_elem_lista(p):
    "elem : lista"

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
parser.soma = 0


for line in sys.stdin:
    parser.parse(line)