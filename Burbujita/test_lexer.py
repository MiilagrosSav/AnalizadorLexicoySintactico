
from lexer import lexer

with open("entrada.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("Analizando tokens...")
lexer.input(data)
for tok in lexer:
    print(tok)

print("Analisis lexico completo.")