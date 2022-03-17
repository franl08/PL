import re
import ply.lex as lex

tokens = ["beginsum", "endsum", "beginmul", "endmul", "equal", "number"]

states = (
    ('mul', 'exclusive'),
    ('soma', 'exclusive')
)

def t_ANY_beginsum(t):
    r'soma_on'
    t.lexer.push_state('soma')
    
def t_ANY_endsum(t):
    r'soma_off'
    t.lexer.pop_state()
    
def t_ANY_beginmul(t):
    r'mul_on'
    t.lexer.push_state('mul')

def t_ANY_endmul(t):
    r'mul_off'
    t.lexer.pop_state()
    
def t_ANY_equal(t):
    r'='
    print("Current result:", lexer.count)
    
def t_mul_number(t):
    r'\d+'
    # print("* ", t.value, end='')
    lexer.count *= int (t.value)
    
def t_soma_number(t):
    r'\d+'
    # print("+ ", t.value, end='')
    lexer.count += int (t.value)
    
def t_ANY_pass(t):
    r'(.|\n)'
    
def t_ANY_error(t):
    r'(.|\n)'
    print("Illegal character!")


lexer = lex.lex()
lexer.count = 0

f = open("on_off.txt", "r")
content = f.read()

lexer.input(content)
for tok in lexer:
    pass

f.close()