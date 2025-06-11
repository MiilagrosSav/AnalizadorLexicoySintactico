import ply.yacc as yacc
from lexer import tokens

precedence = ()

def p_programa(p):
    '''programa : PROGRAMA ORDENAMIENTO PUNTOYCOMA funcion INICIAR bloque FIN'''
    print("✔ Programa válido")

def p_funcion(p):
    '''funcion : FUNCION ORDENAR PARIZQ parametro PARDER declaraciones cuerpo_funcion'''
    pass

def p_parametro(p):
    '''parametro : VECTOR ARREGLO'''
    pass

def p_declaraciones(p):
    '''declaraciones : ENTERO I PUNTOYCOMA
                    | ENTERO J PUNTOYCOMA
                    | ENTERO TEMP PUNTOYCOMA
                    | declaracion_tamano
                    | declaraciones ENTERO I PUNTOYCOMA
                    | declaraciones ENTERO J PUNTOYCOMA
                    | declaraciones ENTERO TEMP PUNTOYCOMA
                    | declaraciones declaracion_tamano'''
    pass

def p_declaracion_tamano(p):
    '''declaracion_tamano : ENTERO TAMANO ASIGNACION LONGITUD PARIZQ ARREGLO PARDER PUNTOYCOMA'''
    pass

def p_cuerpo_funcion(p):
    '''cuerpo_funcion : bucle_principal mostrar_arreglo FIN'''
    pass

def p_mostrar_arreglo(p):
    '''mostrar_arreglo : MOSTRAR PARIZQ ARREGLO PARDER PUNTOYCOMA'''
    pass

def p_bucle_principal(p):
    '''bucle_principal : REPETIR PARIZQ inicializacion condicion incremento PARDER bucle_secundario'''
    pass

def p_inicializacion(p):
    '''inicializacion : I ASIGNACION NUM0 PUNTOYCOMA'''
    pass

def p_condicion(p):
    '''condicion : I MENOR TAMANO MENOS NUM1 PUNTOYCOMA'''
    pass

def p_incremento(p):
    '''incremento : I ASIGNACION I MAS NUM1'''
    pass

def p_bucle_secundario(p):
    '''bucle_secundario : REPETIR PARIZQ init_j cond_j inc_j PARDER bloque_si'''
    pass

def p_init_j(p):
    '''init_j : J ASIGNACION NUM0 PUNTOYCOMA'''
    pass

def p_cond_j(p):
    '''cond_j : J MENOR TAMANO MENOS I MENOS NUM1 PUNTOYCOMA'''
    pass

def p_inc_j(p):
    '''inc_j : J ASIGNACION J MAS NUM1'''
    pass

def p_bloque_si(p):
    '''bloque_si : SI PARIZQ condicion_arreglos PARDER bloque_intercambio FIN FIN FIN'''
    pass

def p_condicion_arreglos(p):
    '''condicion_arreglos : acceso_arreglo MAYOR acceso_arreglo_siguiente'''
    pass

def p_acceso_arreglo(p):
    '''acceso_arreglo : ARREGLO CORCHETEIZQ J CORCHETEDER'''
    pass

def p_acceso_arreglo_siguiente(p):
    '''acceso_arreglo_siguiente : ARREGLO CORCHETEIZQ J MAS NUM1 CORCHETEDER'''
    pass

def p_bloque_intercambio(p):
    '''bloque_intercambio : asignacion_temp asignacion_arr1 asignacion_arr2'''
    pass

def p_asignacion_temp(p):
    '''asignacion_temp : TEMP ASIGNACION acceso_arreglo PUNTOYCOMA'''
    pass

def p_asignacion_arr1(p):
    '''asignacion_arr1 : acceso_arreglo ASIGNACION acceso_arreglo_siguiente PUNTOYCOMA'''
    pass

def p_asignacion_arr2(p):
    '''asignacion_arr2 : acceso_arreglo_siguiente ASIGNACION TEMP PUNTOYCOMA'''
    pass

def p_bloque(p):
    '''bloque : declaracion_arreglo llamada_ordenar'''
    pass

def p_declaracion_arreglo(p):
    '''declaracion_arreglo : VECTOR MIARREGLO ASIGNACION CORCHETEIZQ NUM5 COMA NUM3 COMA NUM2 COMA NUM4 COMA NUM1 CORCHETEDER PUNTOYCOMA'''
    pass

def p_llamada_ordenar(p):
    '''llamada_ordenar : ORDENAR PARIZQ MIARREGLO PARDER PUNTOYCOMA'''
    pass

def p_error(p):
    if p:
        print(f"[✘] Error de sintaxis en: {p.type} → {p.value}")
    else:
        print("[✘] Error de sintaxis: entrada incompleta")

parser = yacc.yacc(debug=True)