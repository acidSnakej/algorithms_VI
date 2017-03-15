# Edite el codigo fuente al final, llamando la funcion deseada
def approved():
    
    """
        Funcion que determina si un estudiante aprueba una materia por asistencia o no.
        Desactivar el codigo comentado apartir de la linea 16 hasta 23 para usar la funcion 
        ingresando datos, de igual manera se recomienda comentar las lineas 11 y 13 respectivamente
    """

    notes = [3.5, 4.0, 5.0]
    assistence = [0, 15, 8]  # Numero de fallas
    # notes = []
    # assistence = []
    
    cont = 0
    """
    while cont < 3:
        message_note = str('ingrese la nota del corte %d: ' % (cont+1))
        note = int(input(message_note))
        message_assist = str('Ingrese la cantidad total de asistencias del corte %d: ' % (cont+1))
        assist = int(input(message_assist))
        notes.append(int(note))
        assistence.append(int(note))
        cont += 1
    """
    prom = notes[0] + notes[1] + notes[2] / len(notes)
    if prom < 3.0:
        print 'Perdio la materia, no cumple con el promedio minimo para aprobar.'
    else:
        print 'Por promedio va pasando la materia, sin embargo, se va calcular la cantidad de fallas \n' \
              'Tenga en cuenta que si supera el 80% \ de fallas pierde.'
        # 45 es la cantidad total de horas en el semestre
        print 'Por favor espere.'
        if ( (assistence[0] + assistence[1] +assistence[2]) * 100 ) / 45 <= 80 :
            print 'Ha pasado el semestre, felicidades'
        else:
            print 'Infortunadamente ha perdido por fallas, su promedio fue %d' % prom

def high_low_number():
    """
        Funcion que determina que cual de los dos numeros es mayor, de igual manera 
        si se desea digitar manualmente los numeros quitar comentarios en la linea 48 a la 53
        y comentar la lista numbers prestablecida
    """
    numbers = [1, 4]
    # numbers = []
    i = 0
    """
    while i < 2:
        message = 'Escriba el numero: '
        num = int(input(message))
        numbers.append(num)
        i += 1
    """        
    if numbers[0] < numbers[1]:
        print 'El numero %d es mayor que el numero %d' % (numbers[1], numbers[0])
    else:
        print 'El numero %d es mayor que el numero %d' % (numbers[0], numbers[1])

def summation():
    """
        Funcion que muestra la sumatoria de 1 al 10.
    """
    i = 1
    summation = 0
    while i < 11:
        summation = i + summation
        i += 1
    print summation

def odd_or_even():
    """
        Funcion que determina si un numero es par o impar,
        si se desea usar ingresando el numero por favor descomente las lineas correspondientes
    """

    number = 200
    # message = print 'Ingrese el numero'
    # number = int(input(message))
    if number % 2 == 0:
        print 'El numero %d es par' % number
    else:
        print 'El numero %d es impar' % number

def simple_order():
    """
        Funcion que ordena una lista de dos elementos de menor a mayor, esto es lo mas basico de ordenamiento
        si desea ingresar los numeros manualmente por favor descomente las lineas correspondientes
    """

    numbers = [123, 4]

    if numbers[0] > numbers[1]:
        aux = numbers[0]
        numbers[0] = numbers[1]
        numbers[1] = aux
        print 'el orden es:'
        print numbers
    else:
        
        aux = numbers[1]
        numbers[1] = numbers[0]
        numbers[0] = aux
        print 'el orden es:'
        print numbers
# para ver un ejemplo descomente la linea siguiente
# simple_order()