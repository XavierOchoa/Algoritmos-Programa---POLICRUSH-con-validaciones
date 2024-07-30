import random
import os

detalleCompra = [[], [], [], [], [], [], [], []]

def menuOpciones():
    while True:
        try:
            print("¿Qué acción desea realizar?")
            print('*  1) Registrar pedidos')
            print('*  2) Mostrar pedidos')
            print('*  3) Mostrar detalle de un pedido')
            print('*  4) Salir del sistema')
            opcion = int(input("Ingrese la opción: "))
            if opcion in [1, 2, 3, 4]:
                return opcion
            else:
                os.system('cls')
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            os.system('cls')
            print("Entrada inválida. Ingrese un número.")

def validar_nombre_apellido(valor):    
    if len(valor) < 3 or len(valor) > 10:
        return False
    
    for char in valor:
        if char >= '0' and char <= '9':
            return False
    return True

def validar_telefono(valor):    
    if len(valor) > 10:
        return False
    
    for char in valor:
        if char < '0' or char > '9':
            return False
    return True

def validar_dependencia(valor):    
    if len(valor) < 5 or len(valor) > 15:
        return False
    
    for char in valor:
        if char >= '0' and char <= '9':
            return False
    return True

def validar_nombre_policrush(valor):    
    if len(valor) < 3 or len(valor) > 10:
        return False
    
    for char in valor:
        if char >= '0' and char <= '9':
            return False
    return True

def validar_celular_policrush(valor):    
    if len(valor) > 10:
        return False
    
    for char in valor:
        if char < '0' or char > '9':
            return False
    return True

def validar_opcion_regalo(opcion):    
    return opcion in [1, 2, 3, 4]

def validar_codigo_pedido(codigo):    
    return codigo.isdigit() and 1 <= len(codigo) <= 4

def ingresarPedido():
    while True:
        nombre_cliente = input("Nombre: ")
        if validar_nombre_apellido(nombre_cliente):
            break
        print("Nombre inválido. Debe tener entre 3 y 10 caracteres y no debe contener números.")
    
    while True:
        apellido_cliente = input("Apellido: ")
        if validar_nombre_apellido(apellido_cliente):
            break
        print("Apellido inválido. Debe tener entre 3 y 10 caracteres y no debe contener números.")
    
    while True:
        telefono_cliente = input("Teléfono: ")
        if validar_telefono(telefono_cliente):
            break
        print("Teléfono inválido. Debe contener solo números y no más de 10 dígitos.")
    
    while True:
        nombre_policrush = input("Nombre: ")
        if validar_nombre_policrush(nombre_policrush):
            break
        print("Nombre de policrush inválido. Debe tener entre 3 y 10 caracteres y no debe contener números.")
    
    while True:
        lugar_policrush = input("Dependencia: ")
        if validar_dependencia(lugar_policrush):
            break
        print("Dependencia inválida. Debe tener entre 5 y 15 caracteres y no debe contener números.")
    
    while True:
        celular_policrush = input("Teléfono: ")
        if validar_celular_policrush(celular_policrush):
            break
        print("Teléfono de policrush inválido. Debe contener solo números y no más de 10 dígitos.")
    
    detalleCompra[0].append(nombre_cliente)
    detalleCompra[1].append(apellido_cliente)
    detalleCompra[2].append(telefono_cliente)
    detalleCompra[3].append(nombre_policrush)
    detalleCompra[4].append(lugar_policrush)
    detalleCompra[5].append(celular_policrush)
    detalleCompra[6].append(random.randrange(1000, 9999))

    print("\n-------- Selección del regalo --------\n")
    print("1) Opción 1: Poliflor + Polipeluche = $2.50")
    print("2) Opción 2: Poliflor + Policarta = $1.50")
    print("3) Opción 3: Poliflor + Polillavero = $2.00")
    print("4) Opción 4: Poliflor + Polivaso = $2.75")

    while True:
        try:
            opcion = int(input("Ingrese la opción: "))
            if validar_opcion_regalo(opcion):
                break
            else:
                print("Opción inválida. Debe ser un número entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    if opcion == 1:
        detalleCompra[7].append(2.50 + (0.1 * 2.50))
    elif opcion == 2:
        detalleCompra[7].append(1.50 + (0.1 * 1.50))
    elif opcion == 3:
        detalleCompra[7].append(2.00 + (0.1 * 2.00))
    elif opcion == 4:
        detalleCompra[7].append(2.75 + (0.1 * 2.75))

    print("\n-------- Pedido registrado con éxito --------\n")

def mostrarPedido(i):
    print("\t\n\n Datos del cliente")
    print("\t\t\t * Nombre:", detalleCompra[0][i])
    print("\t\t\t * Apellido:", detalleCompra[1][i])
    print("\t\t\t * Teléfono:", detalleCompra[2][i])
    print("\t\t\n Datos de la entrega")
    print("\t\t\t * Nombre:", detalleCompra[3][i])
    print("\t\t\t * Dependencia:", detalleCompra[4][i])
    print("\t\t\t * Teléfono:", detalleCompra[5][i])
    print("\t\t\n Datos del pago")
    print("\t\t\t * Código del pedido:", detalleCompra[6][i])
    print("\t\t\t * Pago final: $", detalleCompra[7][i])

print("------------ MI POLICRUSH -------------")
print("\n\t\t *** Bienvenido(a) ***\n")
opcion = menuOpciones()
while opcion != 4:
    if opcion == 1:
        print("\n----- Nuevo pedido -----")
        ingresarPedido()
        opcion = menuOpciones()
    elif opcion == 2:
        if len(detalleCompra[0]) == 0:
            print("-------------------------------------\n")
            print("No existen pedidos registrados\n")
            print("-------------------------------------\n")
            opcion = menuOpciones()
        else:
            print("\n------- Detalle de todos los pedidos ----------\n")
            for i in range(len(detalleCompra[0])):
                print("-------------------------------------")
                print("Detalle del pedido", i + 1)
                mostrarPedido(i)
                print("-------------------------------------")
            opcion = menuOpciones()
    elif opcion == 3:
        while True:
            try:
                codigo = input("\n Ingrese el código del pedido: ")
                if validar_codigo_pedido(codigo):  
                    codigo = int(codigo)
                    if codigo in detalleCompra[6]:
                        dato = detalleCompra[6].index(codigo)
                        for i in range(len(detalleCompra[0])):
                            if i == dato:
                                print("\t\t\t\n Pedido encontrado")
                                print("-------------------------------------")
                                print("Detalle")
                                mostrarPedido(i)
                                print("-------------------------------------")
                        break
                    else:
                        print("\n\n ******* ERROR *****\n")
                        print("No existe ese código de pedido registrado\n")
                else:
                    print("Código inválido. Debe ser un número con hasta 4 dígitos.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    opcion = menuOpciones()

print("Muchas gracias")
