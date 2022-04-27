import re
import ply.lex as lex

tokens = ["CBEGIN", "CEND", "TEXT"]

states = [
    ("comment", "exclusive")
]

def t_ANY_CBEGIN(t): # any indica que é para qualquer estado em que se encontre
    r'/\*'
    t.lexer.push_state("comment") # cria uma stack interna e acrescenta este estado à sua stack    
    
def t_comment_CEND(t):
    r'\*/'
    t.lexer.pop_state()
    
def t_comment_TEXT(t):
    r'(.|\n)'

def t_TEXT(t):
    r'(.|\n)'
    print(t.value, end='')
    
def t_comment_error(t):
    print("Illegal character!")
    
def t_error(t):
    print("Illegal character!")
    
lexer = lex.lex()

f = open("comments_inside.txt", "r")
content = f.read()

lexer.input(content)
for tok in lexer:
    pass

print()

f.close()