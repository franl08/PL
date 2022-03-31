import ply.lex as lex

tokens = ['INT']

literals = ['+', '*', '-', '/', '(', ')']

t_ignore = ' \n\t\r'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal Character!")
    
lexer = lex.lex()

