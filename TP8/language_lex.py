import ply.lex as lex

tokens = ["NUM", "PAL"]
literals = ['(', ')']

t_PAL = r'[a-zA-Z]'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \n\t\r'

def t_error(t):
    print("Illegal Character!")
    
lexer = lex.lex()
