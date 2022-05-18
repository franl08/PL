import sys
from ply import yacc
from lexer import tokens

def p_lang(p):
    'lang : declarations statements'
    p[0] = p[1] + "START\n" + p[2] + "STOP\n"
    
def p_declarations_list(p):
    'declarations : declarations declaration'
    p[0] = p[1] + p[2]
    
def p_declarations_empty(p):
    'declarations : '
    p[0] = ''
    
def p_declaration_no_value(p):
    'declaration : VAR ID ";"'
    if p[2] not in p.parser.symtab:
        p.parser.symtab[p[2]] = {
            'type' : 'INT',
            'address' : p.parser.symcount
            }
        p[0] = 'PUSHI 0\n'
        p.parser.symcount += 1
    else:
        print(f"ERROR: Variable '{p[2]}' already defined.")
        p.parser.error = True

def p_declaration_with_value(p):
    'declaration : VAR ID "=" expression ";"'
    if p[2] not in p.parser.symtab:
        p.parser.symtab[p[2]] = {
            'type' : 'INT',
            'address' : p.parser.symcount
        }
        p[0] = p[4]
        p.parser.symcount += 1
    else:
        print(f"ERROR: Variable '{p[2]}' already defined.")
        p.parser.error = True
        
def p_statements_list(p):
    'statements : statement statements'
    p[0] = p[1] + p[2]
def p_statements_empty(p):
    'statements: '
    p[0] = ''
    
def p_statement_atrib(p):
    'statement : ID "=" expression ";"'
    if p[1] in p.parser.symtab:
        address = p.parser.symtab[p[1]]['address']
        p[0] = p[3] + f'STOREG {address}\n'
    else:
        print(f"ERROR: Undefined variable '{p[1]}'.")
        p.parser.error = True
        
def p_statement_print(p):
    'statement : PRINT expression ";"'
    p[0] = p[2] + 'WRITEI\n'
    
def p_statement_read(p):
    'statement : READ ID ";"'
    if p[2] in p.parser.symtab:
        address = p.parser.symtab[p[2]]['addresss']
        p[0] = 'READ\n' + 'ATOI\n' + f'STOREG {address}\n'
    else:
        print(f"ERROR: Undefined variable '{p[2]}'.")
        p.parser.error = True
        
def p_statement_if_then(p):
    'statement : IF "(" cond ")" THEN "{" statements "}"'
    p[0] = p[3] + f"JZ endif{p.parser.ifcount}\n" + p[7] + f"endif{p.parser.ifcount}:\n"
    p.parser.ifcount += 1
    
def p_statement_if_then_else(p):
    'statement : IF "(" cond ")" THEN "{" statements "}" ELSE "{" statements "}"'
    p[0] = p[3] + f'JZ else{p.parser.ifcount}\n' + p[7] + f'JUMP endif{p.parser.ifcount}\n' + f'else{p.parser.ifcount}:\n' + p[11] + f'endif{p.parser.ifcount}:\n'
    p.parser.ifcount += 1
    
def p_cond_or(p):
    'cond : cond OR cond2'
    p[0] = p[1] + p[3] + 'ADD\n' + p[1] + p[3] + 'MUL\n' + 'SUB\n'
    
def p_cond_cond2(p):
    'cond : cond2'
    p[0] = p[1]
    
def p_cond2_and(p):
    'cond2 : cond2 AND cond3'
    p[0] = p[1] + p[3] + 'MUL\n'
    
def p_cond2_cond3(p):
    'cond2 : cond3'
    p[0] = p[1]
    
def p_cond3_not(p):
    'cond3 : NOT cond3'
    p[0] = 'PUSHI 1\n' + p[2] + 'SUB\n'
    
def p_cond3_cond(p):
    'cond3 : "(" cond ")"'
    p[0] = p[2]
    
def p_relation_equals(p):
    'relation : expression EQUALS expression'
    p[0] = p[1] + p[3] + 'SUB\n' + 'NOT\n'
    
def p_relation_not_equals(p):
    'relation : expression NOTEQUALS expression'
    p[0] = p[1] + p[3] + 'SUB\n' + 'NOT\n' + 'NOT\n'
    
def p_relation_less(p):
    'relation : expressions LESS expression'
    p[0] = p[1] + p[3] + 'INF\n'

def p_relation_lessequal(p):
    'relation : expression LESSEQUAL expression'
    p[0] = p[1] + p[3] + 'INFEQ\n'
    
def p_relation_more(p):
    'relation : expression MORE expression'
    p[0] = p[1] + p[3] + 'SUP\n' 
    
def p_relation_moreequal(p):
    'relation : expression MOREEQUAL expression'
    p[0] = p[1] + p[3] + 'SUPEQ\n'
    
def p_expression_plus(p):
    'expression : expression "+" term'
    p[0] = p[1] + p[3] + 'ADD\n'
    
def p_expression_minus(p):
    'expression : expression "-" term'
    p[0] = p[1] + p[3] + 'SUB\n'
    
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
    
def p_term_mult(p):
    'term : term "*" factor'
    p[0] = p[1] + p[3] + 'MUL\n'
    
def p_term_div(p):
    'term : term "/" factor'
    p[0] = p[1] + p[3] + 'DIV\n'

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    
def p_factor_expression(p):
    'factor : "(" expression ")"'
    p[0] = p[2]
    
def p_factor_INT(p):
    'factor : INT'
    p[0] = f'PUSHI {p[1]}\n'
    
def p_factor_ID(p):
    'factor : ID'
    if p[1] in p.parser.symtab:
        address = p.parser.symtab[p[1]]['address']
        p[0] = f'PUSHG {address}\n'
    else:
        print(f"ERROR: Undefined variable '{p[1]}'.")
        p.parser.error = True    
            
def p_error(p):
    print('Syntax Error!')
    p.parser.error = True
        
parser = yacc.yacc()

parser.symtab = {}
parser.symcount = 0
parser.error = False
parser.ifcount = 0

f = open(sys.argv[1], 'r')
content = f.read()

result = parser.parse(content)
print(result)

f.close()