personas = []
ganancia = 0

def crear_edificio(filas, columnas):
    edificio = [[0 for _ in range(columnas)] for _ in range(filas)]
    num_dpto = 1
    for i in range(filas):
        for j in range(columnas):
            edificio[i][j] = num_dpto
            num_dpto += 1
    return edificio

def mostrar_edificio(edificio):
    filas = len(edificio)
    columnas = len(edificio[0])
    
    for i in range(filas):
        for j in range(columnas):
            print(str(edificio[i][j]).rjust(2), end='\t')
        print()

def reservar_asiento(edificio, fila, columna):
    if edificio[fila][columna] == 'x':
        print('El asiento ya está ocupado.')
        return False
    else:
        edificio[fila][columna] = 'x'
    
        return True

filas = 10
columnas = 4
edificio = crear_edificio(filas, columnas)

def mostrar_dptos_disponibles(edificio):
    print('Dptos disponibles:')
    print(" A  B  C  D") 
    for i in range(filas):
        for j in range(columnas):
            print(str(edificio[i][j]).rjust(2), end=' ')

        print()

def seleccionar_dpto(fila, columna):
    venta = 0
    global ganancia
    global acont
    global bcont
    global ccont
    global dcont
    ganancia = 0
    acont = 0
    bcont = 0
    ccont = 0
    dcont = 0
    run = (input("Ingrese el RUN de la persona que ocupará el dpto sin puntos ni guión: "))
    runstr = str(run)
    
    if len(runstr) != 9:
        print ("Run Incorrecto")
        return
    if fila < 1 or fila > filas or columna < 1 or columna > columnas:
        print('¡Depto inválido!')
        
    else:
        fila -= 1
        columna -= 1
        reservar_asiento(edificio, fila, columna)
    if columna == 0:
        venta = 3800
        acont = acont + 1
    elif columna == 1:
        venta =  3000
        bcont = bcont + 1
    elif columna == 2:
        venta =  2800
        ccont = ccont + 1
    elif columna == 3:
        venta =  3500
        dcont = dcont + 1
    
    ganancia = ganancia + venta
    personas.append([run])
    print("Dpto comprado!.")
    return

def ganancias():
    global ganancia
    global acont
    global bcont
    global ccont
    global dcont
    print ("Tipo departamento || Cantidad|| Total")
    print (f"Tipo A            || {acont}       || {3800 * acont} UF")
    print (f"Tipo B            || {bcont}       || {3000 * bcont} UF")
    print (f"Tipo C            || {ccont}       || {2800 * ccont} UF")
    print (f"Tipo D            || {dcont}       || {3500 * dcont} UF")
    print (f"Total             || {acont+bcont+ccont+dcont}       ||{ganancia} UF")
    return

def listado():
    personas.sort()
    for i in range(len(personas)):
        print(f"Rut:{personas[i]}")
    return

def menu_principal():
    salir = 1
    while (salir):
        print("----- MENÚ -----")
        print("1. Mostrar deptos disponibles")
        print("2. Reservar Dpto")
        print("3. Listado Personas")
        print("4. Ganancias")
        print("5. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            mostrar_dptos_disponibles(edificio)
        elif opcion == 2:
            fila = int(input('Ingrese el número de piso de 1 a 10: '))
            columna = int(input('Ingrese el tipo de departamento ingresando el número de departamento de 1 a 4 siendo A, B, C, D respectivamente : '))
            seleccionar_dpto(fila, columna)
        elif opcion == 3:
            listado()
        elif opcion == 4:
            ganancias()
        elif opcion == 5:
            print("Nombre: Andres Quiroz Ayala")
            print("Fecha: 10/07/2023")
            print("¡Hasta luego!")
            exit()
        else:
            print('Opción inválida. Intente nuevamente.')
# Ciclo principal del programa
menu_principal()
    
