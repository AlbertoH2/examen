import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import lexer

# Resultado del análisis
resultado_gramatica = []

def p_html(p):
    '''html : etiqueta_html'''
    p[0] = p[1]

def p_etiqueta_html(p):
    '''etiqueta_html : MENORQUE HTML MAYORQUE etiqueta_head body MENORQUE DIV HTML MAYORQUE'''
    p[0] = ("Etiqueta HTML encontrada")

def p_etiqueta_head(p):
    '''etiqueta_head : MENORQUE HEAD MAYORQUE title MENORQUE DIV HEAD MAYORQUE'''
    p[0] = ("Etiqueta HEAD encontrada")

def p_title(p):
    '''title : MENORQUE TITLE MAYORQUE IDENTIFICADOR MENORQUE DIV TITLE MAYORQUE'''
    p[0] = ("Título encontrado")

def p_body(p):
    '''body : MENORQUE BODY MAYORQUE etiqueta_php MENORQUE DIV BODY MAYORQUE'''
    p[0] = ("Cuerpo HTML encontrado")

def p_etiqueta_php(p):
    '''etiqueta_php : MENORQUE INTERROGACION PHP ECHO COMSIMP MENORQUE P MAYORQUE IDENTIFICADOR MENORQUE DIV P MAYORQUE COMSIMP PUNTOCOMA INTERROGACION MAYORQUE'''
    p[0] = ("Etiqueta PHP encontrada")

# Regla para manejar errores
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintáctico de tipo {} en el valor {}".format(str(t.type), str(t.value))
    else:
        resultado = "Error sintáctico: Token inválido"
    print(resultado)
    resultado_gramatica.append(resultado)

# Instanciamos el analizador sintáctico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    
    # Realizar el análisis sintáctico en el código completo
    parser.parse(data)

    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa el dato >>> ')
        except EOFError:
            continue
        if not s:  
            continue
        
        gram = parser.parse(s)
        print("Resultado ", gram)
        prueba_sintactica(s)
