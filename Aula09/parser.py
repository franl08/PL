# Criação de linguagem para a VM da UC
import ply.yacc as yacc
import sys
from lexer import tokens

def p_lang(p):
    "lang : declarations SEP statements"
    p[0] = p[1] + "START\n" + p[2] + "STOP\n"
    
def p_declarations_list(p):
    "declarations : declarations declaration"
    p[0] = p[1] + p[2]
    
def p_declarations_empty(p):
    "declarations : "
    p[0] = ""
    
def p_declaration_no_value(p):
    "declaration : K_VAR ID ';'"
    if p[2] not in p.parser.symtab[p[2]]:
        p[0] = f"PUSHI 0\n"
        p.parser.symtab[p[2]] = {"address" : p.parser.symcount, "type" : "INT"}
        p.parser.symcount += 1
    else:
        print(f"ERROR: Variable {p[2]} is already defined.")
        p.parser.error = True
        p[0] = ''
    
def p_declaration_with_value(p):
    "declaration : K_VAR ID '=' exp ';'"
    if p[2] not in p.parser.symtab[p[2]]:
        p[0] = p[4]
        p.parser.symtab[p[2]] = {"address" : p.parser.symcount, "type" : "INT"}
        p.parser.symcount += 1
    else:
        print(f"ERROR: Variable {p[2]} is already defined.")
        p.parser.error = True
        p[0] = ''
    
def p_statements_list(p):
    "statements : statements statement"
    p[0] = p[1] + p[2]
    
def p_statements_empty(p):
    "statements : "
    p[0] = ''
    
def p_statement_print(p):
    "statement : K_PRINT exp ';'"
    p[0] = p[2] + "WRITEI\n"
    
def p_statement_read(p):
    "statement : READ ID ';'"
    if p[2] in p.parser.symtab:
        address = p.parser.symtab[p[2]]["address"]
        p[0] = "READ\n" + "ATOI\n" + f"STOREG {address}\n"
    else:
        print(f"ERROR: Undeclared variable {p[2]}.")
    
def p_statement_assign(p):
    "statement : ID '=' exp ';'"
    if p[1] in p.parser.symtab:
        address = p.parser.symtab[p[1]]["address"]
        p[0] = p[3] + f"STOREG {address}\n"
    else:
        print(f"ERROR: Undeclared variable {p[1]}.")
    
def p_exp(p):
    "exp : aexp"
    p[0] = p[1]
    
def p_aexp_termo(p):
    "aexp : termo"
    p[0] = p[1]
    
def p_aexp_add(p):
    "aexp : aexp '+' termo"
    p[0] = p[1] + p[3] + "ADD\n"
    
def p_aexp_sub(p):
    "aexp : aexp '-' termo"
    p[0] = p[1] + p[3] + "SUB\n"
    
def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]
    
def p_termo_mult(p):
    "termo : termo '*' fator"
    p[0] = p[1] + p[3] + "MUL\n"
    
def p_termo_div(p):
    "termo : termo '/' fator"
    p[0] = p[1] + p[3] + "DIV\n"
    
def p_fator_INT(p):
    "fator : INT"
    p[0] = f"PUSHI {p[1]}\n"
    
def p_fator_ID(p):
    "fator : ID"
    if p[1] in p.parser.symtab:
        address = p.parser.symtab[p[1]]["address"]
        p[0] = f"PUSHG {address}\n"
    else:
        print(f"ERROR: Undeclared variable {p[1]}.")
        p.parser.error = True
        p[0] = ''
    
def p_fator_aexp(p):
    "fator : '(' aexp ')'"
    p[0] = p[2]
    
    
def p_error(p):
    print("Syntax error!")
    p.parser.error = True
    
parser = yacc.yacc()
parser.symtab = {}
parser.symcount = 0
parser.error = False

file = open(sys.argv[1], "r")

content = file.read()
result = parser.parse(content)

if not parser.error:
    print(result)

file.close()
