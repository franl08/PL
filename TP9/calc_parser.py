import ply.yacc as yacc
import sys
from calc_lexer import tokens

def p_prog(p):
    "prog : comandos"

def p_comandos_vazio(p):
    "comandos : "
    
def p_comandos_varios(p):
    "comandos : comandos comando"
    
def p_comando_atrib(p):
    "comando : ID '=' exp"
    p.parser.tabela_ids[p[1]] = p[3]
    
def p_comando_print(p):
    "comando : PRINT exp"
    print(p[2])
    
def p_comando_read(p):
    "comando : READ ID"
    r = int(input()) # permite ler do input e faz parse para um inteiro
    p.parser.tabela_ids[p[2]] = r
    
def p_comando_dump(p):
    "comando : DUMP"
    print(p.parser.tabela_ids)

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
    p[0] = p[1] + p[3]
    
def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]
    
def p_termo_mult(p):
    "termo : termo '*' fator"
    p[0] = p[1] * p[3] # na realidade, cálculos como estes não seriam feitos no próprio Python mas sim em linguagem máquina
    
def p_termo_div(p):
    "termo : termo '/' fator"
    p[0] = p[1] // p[3]
    
def p_fator_INT(p):
    "fator : INT"
    p[0] = int(p[1])
    
def p_fator_ID(p):
    "fator : ID"
    if p[1] not in p.parser.tabela_ids:
        print(f"Error! Variable {p[1]} is not defined.")
        exit()
    p[0] = p.parser.tabela_ids[p[1]]
    
def p_fator_aexp(p):
    "fator : '(' aexp ')'"
    p[0] = p[2]
    
def p_error(p):
    print("Syntax error!")
    
parser = yacc.yacc()

parser.tabela_ids = {} # na realidade nunca iremos guardar o valor da variável mas sim o seu endereço, tipo, etc...

for line in sys.stdin:
    res = parser.parse(line)
