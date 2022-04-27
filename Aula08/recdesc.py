# Não é código funcional, mas sim para compreender o funcionamento de um recursivo descendente
# O processamento de tokens pode ser feito com base no lexer do ply
import ply.lex as lex


def recL():
    if ps.type in {'pal', 'num', '('}:
        recS()
    else:
        exit(1) # na tabela, podemos definir os números de erro
        
def recS():
    if ps.type == 'pal':
        recT('pal')
    elif ps.type == 'num':
        recT('num')
    elif ps.type == '(':
        recT('(')
        recSL()
        recT(')')
    else:
        exit(2)
        
def recSL():
    if ps.type in {'pal', 'num', '('}:
        recS()
        recSL()
    elif ps.type == ')':
        pass
    else:
        exit(3)
        
def recT(token):
    global ps
    if ps.type == token:
        ps = lexer.token() # vamos buscar o próximo símbolo
    else:
        exit(4)
    

lexer = lex.lex()
ps = lexer.token() # representativo do próximo símbolo