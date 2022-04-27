import re
import ply.lex as lex

tokens = ["ID", "INT", "PRINT", "READ", "DUMP"]
literals = ["+", "-", "*", "/", "(", ")", "="]

def t_PRINT(t):
    r'(print|PRINT)'
    return t

def t_READ(t):
    r'(read|READ)'
    return t

def t_DUMP(t):
    r'(dump|DUMP)'
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \n\t\r"

def t_error(t):
    print("Illegal Character: ", t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()