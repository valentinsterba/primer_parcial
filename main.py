from funciones import *

lista_pacientes = []
salir = False

while (salir == False):
    print("")
    print("¡Bienvenido a Clínica La Fuerza!")
    print("")
    print("Ingrese una de las siguientes opciones: ")
    print("1. Cargar Pacientes.")
    print("2. Mostrar Todos los Pacientes.")
    print("3. Buscar Pacientes por Número de Historia Clínica.")
    print("4. Ordenar Pacientes por Número de Historia Clínica.")
    print("5. Mostrar Paciente con Más Días de Internación.")
    print("6. Mostrar Paciente con Menos Días de Internación.")
    print("7. Cantidad de Pacientes con Más de 5 Días de Internación.")
    print("8. Promedio de Días de Internación de Todos los Pacientes.")
    print("9. Salir.")
    print("")


    opciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    opcion = input("Ingrese una de las opciones: ")
    opcion_valida = buscar_opcion(opcion, opciones)

    while (opcion_valida == False):
        opcion = input("Error. Ingrese una de las opciones posibles: ")
        opcion_valida = buscar_opcion(opcion, opciones)
    
    while (len(lista_pacientes) == 0) and (opcion != "1") and (opcion != "9"):
        opcion = input("Error. Cargue por lo menos un paciente (1) para acceder a otras opciones: ")

    match opcion:
        case "1":
            print("Opción Seleccionada: 1. Cargar Pacientes.")
            cantidad_a_ingresar = int(input("Ingrese la cantidad de pacientes a ingresar: "))
            cantidad_valida = validar_dato(cantidad_a_ingresar, 1)

            while (cantidad_valida == False):
                cantidad_a_ingresar = int(input("Error. Ingrese una cantidad mayor a 0: "))
                cantidad_valida = validar_dato(cantidad_a_ingresar, 1)
            
            for i in range(cantidad_a_ingresar):
                numero_historia = int(input("Ingrese su Número de Historia Clínica: "))
                historia_existente = verificar_historia_existente(lista_pacientes, numero_historia)

                while (historia_existente == True):
                    numero_historia = int(input("El número de historia clínica ingresado ya existe. Ingrese uno nuevo: "))
                    historia_existente = verificar_historia_existente(lista_pacientes, numero_historia)

                nombre_paciente = input("Ingrese su Nombre: ")
                nombre_paciente = nombre_paciente.capitalize()
                nombre_existente = verificar_nombre_existente(lista_pacientes, nombre_paciente)

                while (nombre_existente == True):
                    nombre_paciente = input("El nombre ingresado ya existe. Ingrese uno nuevo: ")
                    nombre_paciente = nombre_paciente.capitalize()
                    nombre_existente = verificar_nombre_existente(lista_pacientes, nombre_paciente)

                edad_paciente = int(input("Ingrese su Edad: "))
                edad_valida = validar_dato(edad_paciente, 1)

                while (edad_valida == False):
                    edad_paciente = int(input("Error. Ingrese una edad mayor a 0: "))
                    edad_valida = validar_dato(edad_paciente, 1)

                diagnostico_paciente = input("Ingrese su Diagnóstico: ")
                diagnostico_paciente = diagnostico_paciente.capitalize()

                dias_internacion = int(input("Ingrese los Días de Internación: "))
                dias_validos = validar_dato(dias_internacion, 1)

                while(dias_validos == False):
                    dias_internacion = int(input("Error. Ingrese una cantidad de días mayor a 0: "))
                    dias_validos = validar_dato(dias_internacion, 1)

                datos_paciente = [numero_historia, nombre_paciente, edad_paciente, diagnostico_paciente, dias_internacion]
                lista_pacientes.append(datos_paciente)

        case "2":
            print("Opción Seleccionada: 2. Mostrar Todos los Pacientes.")
            for i in range(len(lista_pacientes)):
                print(lista_pacientes[i])
        case "3":
            print("Opción Seleccionada: 3. Buscar Pacientes por Número de Historia Clínica.")
            numero_a_buscar = int(input("Ingrese el Número de Historia Clínica a Buscar: "))
            paciente_encontrado = buscar_historia(numero_a_buscar, lista_pacientes)
            print(paciente_encontrado)
        case "4":
            print("Opción Seleccionada: 4. Ordenar Pacientes por Número de Historia Clínica.")
            lista_ordenada = ordenar_pacientes(lista_pacientes)
            for i in range(len(lista_ordenada)):
                print(lista_ordenada[i])
        case "5":
            print("Opción Seleccionada: 5. Mostrar Paciente con Más Días de Internación.")
            mensaje_mas_dias = buscar_paciente_mas_dias(lista_pacientes)
            print(mensaje_mas_dias)
        case "6":
            print("Opción Seleccionada: 6. Mostrar Paciente con Menos Días de Internación.")
            mensaje_menos_dias = buscar_paciente_menos_dias(lista_pacientes)
            print(mensaje_menos_dias)
        case "7":
            print("Opción Seleccionada: 7. Cantidad de Pacientes con Más de 5 Días de Internación.")
            lista_mas_cinco_dias = buscar_mas_cinco_dias(lista_pacientes)
            cantidad_mas_cinco_dias = len(lista_mas_cinco_dias)
            print(f"Cantidad de Pacientes con Más de 5 Días: {cantidad_mas_cinco_dias}.")
            for i in range(len(lista_mas_cinco_dias)):
                print(lista_mas_cinco_dias[i])
        case "8":
            print("Opción Seleccionada: 8. Promedio de Días de Internación de Todos los Pacientes.")
            cantidad_pacientes = len(lista_pacientes)
            suma_dias = obtener_suma_dias(lista_pacientes)
            promedio_dias = calcular_promedio_dias(cantidad_pacientes, suma_dias)
            print(f"Promedio de Días de Internación: {promedio_dias} días.")
        case "9":
            print("¡Gracias por su visita!")
            salir = True