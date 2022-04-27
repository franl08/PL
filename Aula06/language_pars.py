import ply.yacc as yacc
from language_lex import tokens # do ficheiro language_lex importa a variável tokens


def p_grammar(p):
    """
    
    lisp : sexp
    
    sexp : NUM
         | PAL
         | '(' sexp_lista ')'
         
    sexp_lista : 
               | sexp sexp_lista
    
    """
    
def p_error(p):
    print("Syntax error")
    
parser = yacc.yacc()

import sys
for line in sys.stdin:
    parser.parse(line)