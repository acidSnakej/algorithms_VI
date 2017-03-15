# Edite el codigo fuente para llamar a la funcion correspondiente
def aprobado():
    """
        funcion para saber si un estudiante pasa el semestre o no,
        se evalua el promedio y la cantidad de fallas del estudiante.
        si el porcentaje de fallas es superior a 80 pierde la materia apesar
        de tener un buen promedio
    """
    lista_notas = []
    lista_fallas = []
    verificador = True
    contador = 0
    while(verificador):
        print 'Ingrese por favor la nota del corte %d' % (contador+1)
        nota_corte = int(input())
        lista_notas.append(nota_corte)
        print 'Ingrese por favor la cantidad de fallas del corte %d' % (contador+1)
        fallas_corte = int(input())
        lista_fallas.append(fallas_corte)
        contador += 1
        if contador > 2:
            verificador = False
    
    promedio = (lista_notas[0] + lista_notas[1] + lista_notas[2]) / 3
    
    if promedio < 3:
        print 'No alcanza el promedio para aprobar esta materia'
    else:
        porcentaje_fallas = ((lista_fallas[0] + lista_fallas[1] + lista_fallas[2]) * 100 ) / 45
        if porcentaje_fallas <= 80:
            print 'Paso el semestre'
        else:
            print 'perdio el semestre'

def ordenar():
    """
        Funcion usada para ordenar dos numeros de menor a mayor
    """
    print 'Por favor ingrese el primer numero: '
    numero_1 = int(input())
    print 'Ingrese el segundo numero: '
    numero_2 = int(input())
    lista_numeros = [numero_1, numero_2]
    lista_ordenada = sorted(lista_numeros)
    print 'La lista ordenada es: '
    print lista_ordenada

def par_o_impar():
    """
        Funcion para saber si un numero es par o impar
    """
    print 'ingrese el numero: '
    numero = int(input())
    division = numero % 2
    if division != 0:
        print 'Este numero impar'
    else:
        print 'Este numero par'

def menor_o_mayor():
    print 'Ingrese el primer numero : '
    numero_1 = int(input())
    print 'Ingrese el segundo numero: '
    numero_2 = int(input())
    if numero_1 > numero_2:
        print 'El primer numero es mayor que el segundo'
    else:
        print 'El segundo numero es mayor que el primero'
# Ejemplo
#menor_o_mayor()