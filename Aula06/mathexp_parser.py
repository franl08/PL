import ply.yacc as yacc
import sys
from mathexp_lexer import tokens
    
def p_exp(p):
    "exp : aexp"
    p[0] = p[1]
    
def p_aexp_termo(p):
    "aexp : termo"
    p[0] = p[1]
    
def p_aexp_add(p):
    "aexp : aexp '+' termo"
    p[0] = p[1] + p[3]
    
def p_aexp_sub(p):
    "aexp : aexp '-' termo"
    p[0] = p[1] - p[3]
    
def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]
    
def p_termo_mult(p):
    "termo : termo '*' fator"
    p[0] = p[1] * p[3]
    
def p_termo_div(p):
    "termo : termo '/' fator"
    p[0] = p[1] * p[3]
    
def p_fator_INT(p):
    "fator : INT"
    p[0] = p[1]
    
def p_fator_aexp(p):
    "fator : '(' aexp ')'"
    p[0] = p[2]
    
def p_error(p):
    print("Syntax error!")
    
parser = yacc.yacc()
res = 0

for line in sys.stdin:
    res = parser.parse(line)
    print(res)