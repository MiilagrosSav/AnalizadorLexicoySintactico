from parser import parser

with open("entrada.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("Analizando sintaxis...")
parser.parse(data)
