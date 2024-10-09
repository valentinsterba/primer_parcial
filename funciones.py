def buscar_opcion(opcion: str, opciones: list) -> bool:
    '''
    Busca la lista de opciones posibles para saber si la opción ingresada por el usuario existe.\n
    Parámetros: opcion (str), opciones (list).\n
    Retorno: opcion_encontrada (bool).
    '''
    opcion_encontrada = False
    for i in range(len(opciones)):
        if (opciones[i] == opcion):
            opcion_encontrada = True
    return opcion_encontrada

def validar_dato(dato: int, minimo: int) -> bool:
    '''
    Verifica que el dato ingresado por el usuario no sea menor a un mínimo pasado como parámetro por defecto.\n
    Parámetros: dato (int), minimo (int).\n
    Retorno: dato_valido (bool).
    '''
    if (dato < minimo):
        dato_valido = False
    else:
        dato_valido = True
    return dato_valido

def verificar_historia_existente(lista_pacientes: list[list], numero_historia: int) -> bool:
    '''
    Verifica que la historia clínica ingresada por el usuario no exista ya en el sistema.\n
    Parámetros: lista_pacientes (list[list]), numero_historia (int).\n
    Retorno: historia_existente (bool).
    '''
    historia_existente = False
    for i in range(len(lista_pacientes)):
        for j in range(1):
            if (lista_pacientes[i][0] == numero_historia):
                historia_existente = True
    return historia_existente

def verificar_nombre_existente(lista_pacientes: list[list], nombre_paciente: str) -> bool:
    '''
    Verifica que el nombre ingresado por el usuario no exista ya en el sistema.\n
    Parámetros: lista_pacientes (list[list]), nombre_paciente (str).\n
    Retorno: nombre_existente (bool).
    '''
    nombre_existente = False
    for i in range(len(lista_pacientes)):
        for j in range(1):
            if (lista_pacientes[i][1] == nombre_paciente):
                nombre_existente = True
    return nombre_existente

def buscar_historia(numero_historia: int, lista_pacientes: list[list]) -> str:
    '''
    Verifica si hay un paciente con el número de historia clínica ingresado por el usuario.\n
    Parámetros: numero_historia (int), lista_pacientes (list[list]).\n
    Retorno: mensaje (str).
    '''
    mensaje = f"No se encontró un paciente con {numero_historia} como número de historia clínica."
    for i in range(len(lista_pacientes)):
        for j in range(1):
            if (lista_pacientes[i][j] == numero_historia):
                mensaje = f"¡Paciente Encontrado!\nDatos: {lista_pacientes[i]}"
    return mensaje

def ordenar_pacientes(lista_pacientes: list[list]) -> list[list]:
    '''
    Ordena los pacientes en orden ascendente según sus números de historia clínica.\n
    Parámetro: lista_pacientes (list[list]).\n
    Retorno: lista_pacientes (list[list]).
    '''
    for i in range(len(lista_pacientes)):
        for j in range(len(lista_pacientes) - 1 - i):
            if (lista_pacientes[j][0] > lista_pacientes[j+1][0]):
                auxiliar = lista_pacientes[j]
                lista_pacientes[j] = lista_pacientes[j+1]
                lista_pacientes[j+1] = auxiliar
    return lista_pacientes

def buscar_paciente_mas_dias(lista_pacientes: list[list]) -> str:
    '''
    Busca el paciente con más días de internación.\n
    Parámetro: lista_pacientes (list[list]).\n
    Retorno: mensaje (str).
    '''
    flag_primero = True
    for i in range(len(lista_pacientes)):
        for j in range(len(lista_pacientes[i])):
            if (flag_primero == True):
                cantidad_mas_dias = lista_pacientes[i][4]
                paciente_mas_dias = lista_pacientes[i]
                flag_primero = False
            else:
                if (lista_pacientes[i][4] > cantidad_mas_dias):
                    cantidad_mas_dias = lista_pacientes[i][4]
                    paciente_mas_dias = lista_pacientes[i]
    
    mensaje = f"Paciente con Más Días de Internación: {paciente_mas_dias}"
    return mensaje

def buscar_paciente_menos_dias(lista_pacientes: list[list]) -> str:
    '''
    Busca el paciente con menos días de internación.\n
    Parámetro: lista_pacientes (list[list]).\n
    Retorno: mensaje (str).
    '''
    flag_primero = True

    for i in range(len(lista_pacientes)):
        for j in range(len(lista_pacientes[i])):
            if (flag_primero == True):
                cantidad_menos_dias = lista_pacientes[i][4]
                paciente_menos_dias = lista_pacientes[i]
                flag_primero = False
            else:
                if (lista_pacientes[i][4] < cantidad_menos_dias):
                    cantidad_menos_dias = lista_pacientes[i][4]
                    paciente_menos_dias = lista_pacientes[i]
    
    mensaje = f"Paciente con Menos Días de Internación: {paciente_menos_dias}"
    return mensaje

def buscar_mas_cinco_dias(lista_pacientes: list[list]) -> list[list]:
    '''
    Busca los pacientes que tienen más de cinco días de internación.\n
    Parámetro: lista_pacientes (list[list]).\n
    Retorno: lista_mas_cinco_dias (list[list]).
    '''
    lista_mas_cinco_dias = []

    for i in range(len(lista_pacientes)):
        for j in range(1):
            if (lista_pacientes[i][4] > 5):
                lista_mas_cinco_dias.append(lista_pacientes[i])
    
    return lista_mas_cinco_dias

def obtener_suma_dias(lista_pacientes: list[list]) -> int:
    '''
    Obtiene la suma de los días de internación de los pacientes.\n
    Parámetro: lista_pacientes (list[list]).\n
    Retorno: suma_dias (int).
    '''
    suma_dias = 0
    for i in range(len(lista_pacientes)):
        for j in range(1):
            suma_dias += lista_pacientes[i][4]
    
    return suma_dias

def calcular_promedio_dias(cantidad_pacientes: int, suma_dias: int) -> float:
    '''
    Calcula el promedio de días de internación.\n
    Parámetros: cantidad_pacientes (int), suma_dias (int).\n
    Retorno: promedio (float).
    '''
    promedio = suma_dias / cantidad_pacientes
    return promedio