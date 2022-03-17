import re
import ply.lex as lex

tokens = ["CBEGIN", "CEND", "TEXT"]

states = [
    ("comment", "exclusive")
]

def t_CBEGIN(t):
    r'/\*'
    t.lexer.begin("comment")
    t.lexer.counter +=1
    
def t_comment_CEND(t):
    r'\*/'
    t.lexer.begin("INITIAL")
    
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
lexer.counter = 0

f = open("comments.txt", "r")
content = f.read()

lexer.input(content)
for tok in lexer:
    pass

print()
print()
print("Number of comments: ", lexer.counter)

f.close()