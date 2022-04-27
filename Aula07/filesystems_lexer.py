import ply.lex as lex

tokens = ["ID"]

literals = ["{", "}", ","]

t_ID = r"[\-\.\w]+"

t_ignore = " \n\t\r"
    
def t_error(t):
    print("Illegal Character: ", t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()