import re
import ply.lex as lex

tokens = ["CBEGIN", "CEND", "TEXT"]

# comment = False

def t_CBEGIN(t):
    r'/\*'
    # global comment # necessário indicar que pretendemos aceder à variável global comment
    # comment = True
    t.lexer.states.append("comment")
        
def t_CEND(t):
    r'\*/'
    # global comment
    # comment = False
    t.lexer.states = t.lexer.states[:-1]
    
def t_TEXT(t):
    r'(.|\n)'
    #if not comment:
    if t.lexer.states == ["INITIAL"]:
        print(t.value, end='') # t.value obtém o caractere que deu match
    
def t_error(t):
    print("Illegal character!")
    
lexer = lex.lex()
lexer.states = ["INITIAL"]

f = open("comments_inside.txt", "r")
content = f.read()

lexer.input(content)
for tok in lexer:
    pass
print()
f.close()