import ply.lex as lex

resultado_lexema = []

# Palabras reservadas
reserved = {
    'HTML':'HTML',
    'HEAD': 'HEAD',
    'TITLE': 'TITLE',
    'BODY': 'BODY',
    'P': 'P',
    'PHP':'PHP',
    'ECHO':'ECHO',
}

# Tokenss
tokens = [
    'IDENTIFICADOR',
    #'CADENA',
    
    # Simbolos
    'DIV',
    'INTERROGACION',
    'MAYORQUE',
    'MENORQUE',
    
    # Otros
    'PUNTOCOMA',
    'COMSIMP',
    'COMDOB',
    'COMMENT',
]+ list(reserved.values())


# Expresiones regulares para tokens simples
#t_STRING = r'\"([^\\\n]|(\\.))*?\"'
#t_CADENA = r'<p>([^<]*)<\/p>'



t_DIV = r'/'
t_INTERROGACION = r'\?'
t_PUNTOCOMA = r';'

t_COMSIMP = r'\''
t_COMDOB = r'\''
t_MAYORQUE = r'>'
t_MENORQUE = r'<'

# Regla para identificadores
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z]*'
    if t.value.upper() in reserved: 
        t.type = reserved[t.value.upper()]  
    else:
        t.type = 'IDENTIFICADOR'  
    return t

# Regla para comentarios
def t_COMMENT(t):
    r'//.*'
    pass

# Ignorar caracteres como espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Carácter inválido '%s' en la posición %d" % (t.value[0], t.lexpos))
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

# Construir el analizador léxico
lexer = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)
