import re
import ply.lex as lex

tokens = ["CBEGIN", "CEND", "TEXT"]

# comment = False

def t_CBEGIN(t):
    r'/\*'
    # global comment # necessário indicar que pretendemos aceder à variável global comment
    # comment = True
    t.lexer.comment = True
    t.lexer.count += 1
    
def t_CEND(t):
    r'\*/'
    # global comment
    # comment = False
    t.lexer.comment = False
    
def t_TEXT(t):
    r'(.|\n)'
    #if not comment:
    if not t.lexer.comment:
        print(t.value, end='') # t.value obtém o caractere que deu match
    
def t_error(t):
    print("Illegal character!")
    
lexer = lex.lex()
lexer.comment = False # acresecenta uma variável ao estado do lexer
lexer.count = 0

f = open("comments.txt", "r")
content = f.read()

lexer.input(content)
for tok in lexer:
    pass
print()
print()
print("Number of comments: ", lexer.count)
f.close()