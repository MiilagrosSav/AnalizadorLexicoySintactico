from lexer import lexer
from parser import parser

# Leer el contenido del archivo
with open('entrada.txt', 'r', encoding='utf-8') as file:
    data = file.read()

print("Analizando tokens...")
lexer.input(data)
for tok in lexer:
    print(tok)

print("\nAnalizando sintaxis...")
parser.parse(data)