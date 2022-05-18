from re import T
import ply.lex as lex

reserved = {
    'var' : 'VAR',
    'print' : 'PRINT',
    'read' : 'READ',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE'
}

tokens = ['ID', 'INT', 'EQUALS', 'NOTEQUALS', 'LESS', 'LESSEQUAL', 'MORE', 'MOREEQUAL'] + list(reserved.values())
literals = ['=', '+', '-', '*', '/', ';', '(', ')', '{', '}']

t_ignore = ' \n\t\r'

t_EQUALS = r'=='
t_NOTEQUALS = r'!='
t_LESSEQUAL = r'<='
t_MOREEQUAL = r'>='
t_LESS = r'<'
t_MORE = r'>'

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t 

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t 

def t_error(t):
    print('Illegal character: ' + t.value[0])
    
lexer = lex.lex()
