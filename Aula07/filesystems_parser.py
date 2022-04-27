# gera um ficheiro em batch que quando corrido gera o sistema de ficheiros
import ply.yacc as yacc
from filesystems_lexer import tokens

def p_fs(p):
    "fs : dir"
    p[0] = p[1]
    
def p_dir_vazia(p):
    "dir : ID '{' '}'"
    p[0] = f"mkdir {p[1]}\n"
    
def p_dir_conteudo(p):
    "dir : ID '{' conteudo '}'"
    p[0] = f"mkdir {p[1]}\ncd {p[1]}\n{p[3]}cd ..\n"
    
def p_conteudo_unico(p):
    "conteudo : elem"
    p[0] = p[1]
    
def p_conteudo_lista(p):
    "conteudo : conteudo ',' elem"
    p[0] = p[1] + p[3] # concatena os dois conjuntos de instruções
    
def p_elem_id(p):
    "elem : ID"
    p[0] = f"touch {p[1]}\n"
    
def p_elem_dir(p):
    "elem : dir"
    p[0] = p[1]
    
def p_error(p):
    print("Syntax error!")

parser = yacc.yacc()    
    
f = open("filesystems.txt", "r")
content = f.read()

res = parser.parse(content)

print(res)

f.close()