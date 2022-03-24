import sys
import ply.lex as lex


tokens = ["NUM", "PAL"]
literals = ["[", "]", ","] 

t_NUM = r"\d+"
t_PAL = r"[a-zA-Z]+"

t_ignore = " \n\t\r";

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
    
def p_elem_pal(p):
    "elem : PAL"
    
def p_elem_lista(p):
    "elem : lista"

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()


for line in sys.stdin:
    parser.parse(line)