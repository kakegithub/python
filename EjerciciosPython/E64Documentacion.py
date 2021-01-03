# Documentacion y pruebas


'''def areaTriangulo(base,altura):

    """
    Calcula el area de un triangulo dado

    >>> areaTriangulo(3,6)
    'El area del triangulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El area del triangulo es: 10.0'

    >>> areaTriangulo(9,3)
    'El area del triangulo es: 13.5'

    """
    return "El area del triangulo es: " + str((base*altura)/2)

#import doctest # Modulo para hacer pruebas
#doctest.testmod() # Si no pasa nada la funcion funciona '''

def comprobarEmail(mailUsuario):
    """ 
        La funcion comprobarEmail() evalua un mail recibido
        en busca de la @.
        Si tiene una @ es correcto
        Si tiene mas de una @ es incorrecto
        Si la @ esta al final es incorrecto

    >>> comprobarEmail("juan@cursos.es")
    TRUE
    
    >>> comprobarEmail("juancursos.es@")
    FALSE
    
    >>> comprobarEmail("juancursos.es")
    FALSE

    >>> comprobarEmail("juan@cursos@.es")
    FALSE
    
    """

    arroba=mailUsuario.count('@')
    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True


import doctest
doctest.testmod()

