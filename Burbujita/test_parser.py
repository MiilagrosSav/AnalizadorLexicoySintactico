# Solo sintaxis
# test_parser.py
from parser import parser

with open('entrada.txt', 'r', encoding='utf-8') as file:
    data = file.read()

result = parser.parse(data)
print("Análisis sintáctico completado.")