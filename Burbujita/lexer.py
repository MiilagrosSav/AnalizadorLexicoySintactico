import ply.lex as lex

# Lista de tokens: todos los nombres usados como palabras reservadas o símbolos
tokens = [
    'ORDENAMIENTO','PROGRAMA', 'FUNCION', 'ORDENAR', 'VECTOR', 'ARREGLO', 'ENTERO',
    'TAMANO', 'LONGITUD', 'MOSTRAR', 'I', 'J', 'TEMP', 'MIARREGLO', 'INICIAR', 'FIN', 'REPETIR', 'SI',

    'ASIGNACION', 'IGUAL', 'DIFERENTE', 'MAYOR', 'MENOR',
    'MAYORIGUAL', 'MENORIGUAL', 'MAS', 'MENOS',
    'PUNTOYCOMA', 'COMA', 'DOSPUNTOS',
    'PARIZQ', 'PARDER', 'CORCHETEIZQ', 'CORCHETEDER',

    'NUM5', 'NUM3', 'NUM2', 'NUM4', 'NUM1', 'NUM0'
]

# Reglas de símbolos
t_ASIGNACION  = r':='
t_IGUAL       = r'=='
t_DIFERENTE   = r'!='
t_MAYOR       = r'>'
t_MENOR       = r'<'
t_MAYORIGUAL  = r'>='
t_MENORIGUAL  = r'<='
t_MAS         = r'\+'
t_MENOS       = r'-'
t_PUNTOYCOMA  = r';'
t_COMA        = r','
t_DOSPUNTOS   = r':'
t_PARIZQ      = r'\('
t_PARDER      = r'\)'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'

# Ignorar espacios y tabs
t_ignore = ' \t'

# Palabras reservadas como funciones
def t_ORDENAMIENTO(t): r'OrdenamientoBurbuja'; return t
def t_PROGRAMA(t): r'programa'; return t
def t_FUNCION(t): r'función'; return t
def t_ORDENAR(t): r'ordenar'; return t
def t_VECTOR(t): r'vector'; return t
def t_ARREGLO(t): r'arreglo'; return t
def t_ENTERO(t): r'entero'; return t
def t_TAMANO(t): r'tamaño'; return t
def t_LONGITUD(t): r'longitud'; return t
def t_MOSTRAR(t): r'mostrar'; return t
def t_J(t): r'j'; return t
def t_TEMP(t): r'temp'; return t
def t_MIARREGLO(t): r'miArreglo'; return t
def t_INICIAR(t): r'iniciar'; return t
def t_I(t): r'i'; return t
def t_FIN(t): r'fin'; return t
def t_REPETIR(t): r'repetir'; return t
def t_SI(t): r'si'; return t

# Números específicos
def t_NUM5(t): r'5'; return t
def t_NUM4(t): r'4'; return t
def t_NUM3(t): r'3'; return t
def t_NUM2(t): r'2'; return t
def t_NUM1(t): r'1'; return t
def t_NUM0(t): r'0'; return t

# Comentarios
def t_COMMENT(t): r'//.*'; pass

# Conteo de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"[Error] Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()
