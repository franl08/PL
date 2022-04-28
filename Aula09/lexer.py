import ply.lex as lex

reserved = {  
    'var' : 'K_VAR',
    'print' : 'K_PRINT',
    'read' : 'K_READ'
}

tokens = ['INT', 'PRINT', 'SEP'] + list(reserved.values)

literals = ['+', '*', '-', '/', '(', ')', '=', ';'] 

t_ignore = ' \n\t\r'
t_SEP = r'%%'  # Temos de definir no lexer porque estamos a ignorar os espaços, então poderiam ser colocados espaços entre os dois chars caso a declaração fosse feita no parser

def t_INT(t):
    r'\d+'
    t.value = t.value
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID') # verifica se a palavra encontrada é reservada, caso seja -> associa a palavra ao token da palavra reservada
    return t

def t_error(t):
    print("Illegal Character!")
    
lexer = lex.lex()

