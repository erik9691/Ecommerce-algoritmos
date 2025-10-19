# =================== IMPORTS ===================

import random

# =================== LISTAS PARALELAS ===================

# Productos
productosId = ["id0", "id1", "id2", "id3"]
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosCategoria = ["Vestimenta", "Vestimenta", "Tecnología", "Tecnología"]
productosPrecio = [15.00, 45.00, 499.99, 75.50]
productosStock = [50, 30, 10, 40]
productosVendidos = [0, 0, 0, 0]
productosRecaudacion = [0, 0, 0, 0]

# Compras
comprasId = []
comprasDni = []
comprasProductoId = []
comprasCantidad = []
comprasTotal = []
comprasMedioPago = []

# Clientes
clienteDni = []
clienteRecaudacion = []
clienteCompras = []

# Cupones
cuponesCodigo = ["6852", "4182", "2186", "5742"]
cuponesDescuento = [15, 25, 30, 40]

# =================== FUNCIONES AUXILIARES  ===================

def esNumero(texto):
    numeros = "0123456789"
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter not in numeros:
            return False
    return True

def validarDNI(dni):
    if esNumero(dni) and len(dni) == 8 and int(dni) > 0:
        return True
    else:
        return False
    
def copiarLista(lista):
    copia = []
    for elemento in lista:
        copia.append(elemento)
    return copia

def ordenamientoSeleccion(lista, mayor_a_menor = False, listasParalelas = []):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if mayor_a_menor:
                if lista[i] < lista[j]:
                    if len(listasParalelas) > 0:
                        for listaParalela in listasParalelas:
                            aux = listaParalela[i]
                            listaParalela[i] = listaParalela[j]
                            listaParalela[j] = aux
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if lista[i] > lista[j]:
                    if len(listasParalelas) > 0:
                        for listaParalela in listasParalelas:
                            aux = listaParalela[i]
                            listaParalela[i] = listaParalela[j]
                            listaParalela[j] = aux
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

def calcularPorcentajes(lista):
    # Devuelve una lista con el porcentaje que representa cada elemento del total
    total = 0
    porcentajes = []
    for valor in lista:
        total += valor
    for valor in lista:
        if valor == 0:
            porcentajes.append(0)
        else:
            porcentajes.append((valor / total) * 100)
    return porcentajes

def registrarCompra(dni, productoId, cantidad, medioPago, total):
    # Generar ID
    nuevoId = len(comprasId) + 1
    
    # Agregar compra
    comprasId.append(nuevoId)
    comprasDni.append(int(dni))
    comprasProductoId.append(productoId)
    comprasCantidad.append(cantidad)
    comprasTotal.append(total)
    comprasMedioPago.append(medioPago)
    
    # Actualizar cliente
    dniNum = int(dni)
    clienteExiste = False
    
    i = 0
    while i < len(clienteDni) and not clienteExiste:
        if clienteDni[i] == dniNum:
            clienteRecaudacion[i] = clienteRecaudacion[i] + total
            clienteCompras[i] = clienteCompras[i] + 1
            clienteExiste = True
        i = i + 1

    if not clienteExiste:
        clienteDni.append(dniNum)
        clienteRecaudacion.append(total)
        clienteCompras.append(1)
    
    # Actualizar producto
    i = 0
    productoEncontrado = False
    while i < len(productosId) and not productoEncontrado:
        if productosId[i] == productoId:
            productosStock[i] = productosStock[i] - cantidad
            productosVendidos[i] = productosVendidos[i] + cantidad
            productosRecaudacion[i] = productosRecaudacion[i] + total
            productoEncontrado = True
        i = i + 1

def gestionarStock(producto):
    print("================================================================")
    print(f"-----AJUSTANDO STOCK {productosNombre[producto]} ({productosStock[producto]})-------")
    ajusteStock=int(input("Ingrese un número positivo para sumar stock y uno negativo para restar: "))
    nuevoStock= productosStock[producto] + ajusteStock
    if nuevoStock < 0:
        print("⛝       Cambio no realizado       ⛝ ")
        print("================================================================")
        print("X---X---X---EL STOCK DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarStock()
    else:
        productosStock[producto]=nuevoStock
        print("================================================================")
        print(f"Nuevo Stock de {productosNombre[producto]} | Stock actualizado: {productosStock[producto]}")
        print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarProductos()
    
def gestionarPrecio(producto):
    print("================================================================")
    print(f"-----AJUSTANDO PRECIO {productosNombre[producto]} (${productosPrecio[producto]})-------")
    ajustePrecio=int(input("Ingrese el nuevo precio del producto: $"))
    if ajustePrecio<=0:
        print("================================================================")
        print("X---X---X---EL PRECIO DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
        print("⛝       Cambio no realizado       ⛝ ")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarPrecio()
    else:    
        productosPrecio[producto]=ajustePrecio
        print("================================================================")
        print(f"Nuevo Precio de {productosNombre[producto]} | Precio actualizado: ${productosPrecio[producto]}")
        print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarProductos()

# =================== FUNCIONES PRINCIPALES  ===================

def Comprar():
    print("================================================================")
    print("- - - - - 💸 COMPRA 💸 - - - - -")

    # Sugerir un producto aleatorio
    if len(productosNombre) > 0:
        random_index = random.randint(0, len(productosNombre) - 1)
        print("================================================================")
        print(f"💡 Producto recomendado de hoy: {productosNombre[random_index]} — ${productosPrecio[random_index]} ({productosStock[random_index]} en stock)")
        print("================================================================")

    # DNI
    print("Ingrese 0 para volver al menu")
    dni = input("Ingrese su DNI: ")
    if dni == "0":
        return
    elif validarDNI(dni):
        # Medio de pago
        medioPago = ""
        while True:
            print("================================================================")
            print("- - - - - MEDIO DE PAGO - - - - -")
            print("[0] Volver")
            print("[1] Efectivo")
            print("[2] Tarjeta")
            medio = input("Medio de pago: ")

            if medio == "0":
                return Comprar()
            elif medio == "1":
                medioPago = "Efectivo"
                break
            elif medio == "2":
                medioPago = "Tarjeta"
                break
            else:
                print("================================================================")
                print("❌ Opción inválida")

        # Mostrar productos
        prodInput = ""
        productoIndice = ""
        while True:
            print("================================================================")
            print("- - - - - PRODUCTOS DISPONIBLES - - - - -")
            for i in range(len(productosNombre)):
                print(f"[{i}] {productosNombre[i]} - ${productosPrecio[i]}")

            prodInput = input("Seleccione producto (número): ")
            if esNumero(prodInput):
                productoIndice = int(prodInput)

            if esNumero(prodInput) and productoIndice >= 0 and productoIndice < len(productosNombre):
                if productosStock[productoIndice] > 0:
                    break
                else:
                    print("================================================================")
                    print("❌ Sin stock")
            else:
                print("================================================================")
                print("❌ Producto no válido")
        
        # Cantidad
        cantidad = ""
        while True:
            print("================================================================")
            print(f"- - - - - CANTIDAD DE PRODUCTO - - - - -")

            cantInput = input(f"Cantidad de {productosNombre[productoIndice]}: ")
            if esNumero(cantInput):
                cantidad = int(cantInput)
            
            if esNumero(cantInput) and cantidad > 0 and cantidad <= productosStock[productoIndice]:
                break
            else:
                print("================================================================")
                print(f"❌ Cantidad inválida. Max: {productosStock[productoIndice]}")

        # Calcular subtotal
        subtotal = productosPrecio[productoIndice] * cantidad
        descuento = 0
        
        # Cupón
        while True:
            print("================================================================")
            print(f"- - - - - CUPÓN - - - - -")
            usarCupon = input("¿Usar cupón? (S/N): ")
            if usarCupon.upper() == "S":
                while True:
                    print("Ingrese 0 para cancelar ingreso de cupón")
                    codigo = input("Código del cupón: ")
                    print("================================================================")
                    if codigo == "0":
                        break
                    elif codigo in cuponesCodigo:
                        indiceCupon = cuponesCodigo.index(codigo)
                        descuento = cuponesDescuento[indiceCupon]
                        print(f"Cupón aplicado: {descuento}% descuento")
                        break
                    else:
                        print("Cupón inválido")
                break
            elif usarCupon.upper() == "N":
                break
            else:
                print("================================================================")
                print("❌ Opción inválida")
        
        # Calcular total
        total = subtotal * (100 - descuento) / 100

        # Confirmar
        print("================================================================")
        print(f"- - - - - CONFIRMACIÓN DE COMPRA - - - - -")
        print(f"Resumen: {productosNombre[productoIndice]} x{cantidad}")
        print(f"Subtotal: ${subtotal}")
        if descuento > 0:
            print(f"Descuento: {descuento}%")
        print(f"Total: ${total}")
        
        confirmar = input("Confirmar compra (S/N): ")
        if confirmar.upper() == "S":
            registrarCompra(dni, productosId[productoIndice], cantidad, medioPago, total)
            print("================================================================")
            print("✅ Compra realizada")
        else:
            print("================================================================")
            print("Compra cancelada")
    else:
        print("================================================================")
        print("❌ DNI inválido")
        return Comprar()
    
    print("================================================================")
    input("Presione Enter para continuar...")

def verEstadisticas():
    #Pantalla inicial con opciones
    print("================================================================")
    print("- - - - - 📈 ESTADÍSTICAS DE VENTAS 📊 - - - - -")
    print("[0] Volver")
    print("[1] Facturación total")
    print("[2] Facturación por producto")
    print("[3] Cliente con mayor compra")
    opcionNum = input("Seleccione una opción: ")

    #Mostrar estadistica de acuerdo a numero seleccionado
    if opcionNum == "0":
        return
    print("================================================================")
    if opcionNum == "1":
        dineroTotal = 0
        for producto in productosRecaudacion:
            dineroTotal += producto
        print(f"Facturación total: ${dineroTotal}")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    elif opcionNum == "2":
        print("Facturación total por producto (Ordenado por Facturación):")
        # Ordenar listas por facturación
        recaudacionOrdenado = copiarLista(productosRecaudacion)
        idOrdenado = copiarLista(productosId)
        nombreOrdenado = copiarLista(productosNombre)
        ordenamientoSeleccion(recaudacionOrdenado,True,[idOrdenado,nombreOrdenado])
        # Calcular porcentaje de facturacion
        recaudacionOrdenadoPorcent = calcularPorcentajes(recaudacionOrdenado)
        for i in range(len(productosId)):
            print(f"- {nombreOrdenado[i]} ({idOrdenado[i]}): ${recaudacionOrdenado[i]} ({recaudacionOrdenadoPorcent[i]}%)")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    elif opcionNum == "3":
        if len(comprasDni) == 0:
            print("No hay clientes registrados")
            print("================================================================")
            input("Presione Enter para continuar...")
            return verEstadisticas()
        dniCompraMax = comprasDni[0]
        cantCompraMax = comprasTotal[0]
        for i in range(len(comprasId)):
            if comprasTotal[i] > cantCompraMax:
                cantCompraMax = comprasTotal[i]
                dniCompraMax = comprasDni[i]
        print("Cliente con la compra más alta:")
        print(f"- DNI: {dniCompraMax}")
        print(f"- Total de la compra: ${cantCompraMax}")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()

def verEstadisticaProducto():
    #Pantalla inicial con productos
    print("================================================================")
    print("- - - - - 📈 ESTADÍSTICAS POR PRODUCTO 📊 - - - - -")
    print("[0] Volver")
    for i in range(len(productosId)):
        print(f"[{i+1}] {productosNombre[i]} ({productosId[i]})")
    productoNum = int(input("Seleccione un producto: ")) - 1

    #Si presiona 0 salir de funcion
    if productoNum == (-1):
        return
    
    print("================================================================")
    
    #Segunda pantalla con estadísticas para producto seleccionado
    print(f"- - - - - ESTADÍSTICAS PARA {productosNombre[productoNum]} - - - - -")
    print(f"Facturación total: ${productosRecaudacion[productoNum]}")
    print(f"Cantidad de compras: {productosVendidos[productoNum]}")
    print("================================================================")
    input("Presione Enter para continuar...")
    return verEstadisticaProducto()
    
def verEstadisticaCliente():
    #Pantalla inicial con clientes
    print("================================================================")
    print("- - - - - 📈 VENTAS POR CLIENTE 📊 - - - - -")
    
    if len(comprasDni) == 0:
        print("No hay clientes registrados")
        print("================================================================")
        input("Presione Enter para continuar...")
        return
    
    print("[0] Volver")
    for i in range(len(clienteDni)):
        print(f"[{i+1}] {clienteDni[i]}")
    clienteNum = int(input("Seleccione un cliente: ")) - 1

    #Si presiona 0 salir de funcion
    if clienteNum == (-1):
        return
    
    dniSelect = clienteDni[clienteNum]
    print("================================================================")
    
    #Segunda pantalla con estadísticas de todas las compras, filtrado por el cliente seleccionado
    print(f"- - - - - Cliente ({dniSelect}) - - - - -")
    print(f"Pagos totales: ${clienteRecaudacion[clienteNum]}")
    print(f"Cantidad de compras: {clienteCompras[clienteNum]}")
    print("\nProductos comprados:")
    for i in range(len(comprasId)):
        if comprasDni[i] == dniSelect:
            print(f"- Producto: {comprasProductoId[i]} | Cantidad comprado: {comprasCantidad[i]} | Total Facturado: ${comprasTotal[i]} | Tipo de Pago: {comprasMedioPago[i]}")
    print("================================================================")
    input("Presione Enter para continuar...")
    return verEstadisticaCliente()



def gestionarProductos():
    print("================================================================")
    print("--- GESTIÓN DE INVENTARIO Y PRECIOS ---")
    
    print("[0] Volver")
    for i in range(len(productosNombre)):
        print(f"[{i+1}] {productosNombre[i]} | Precio: ${productosPrecio[i]} | Stock: {productosStock[i]}")
     
    opcion=int(input("Seleccione el producto a modificar: "))
    
    if opcion == 0:
        return
    elif opcion > len(productosNombre):
        print("================================================================")
        print("⛝ OPCION NO VALIDA ⛝")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarProductos()
    else:
        opcion = opcion-1
        print("================================================================")
        print('\033[1m\033[4m' f"Edición del producto: {productosNombre[opcion]} | Stock: {productosStock[opcion]} | Precio: {productosPrecio[opcion]}" '\033[0m')
        print("[0] Volver")
        print("[1] Modificar Stock")
        print("[2] Modificar Precio")
        ajuste=int(input("Ingrese el ajuste deseado: "))
       
        if ajuste == 0:
            return gestionarProductos()
        elif ajuste == 1:
            gestionarStock(opcion)
        elif ajuste == 2:
            gestionarPrecio(opcion)
        else:
            print("================================================================")
            print("⛝ OPCION NO VALIDA ⛝")
            print("================================================================")
            input("Presione Enter para continuar...")
            return gestionarProductos()

def gestionarCupones():
    print("================================================================")
    print("- - - - - 🎟️ GESTIÓN DE CUPONES 🎟️ - - - - -")

    print("[0] Volver")
    print("[1] Ver cupones")
    print("[2] Borrar cupón")
    print("[3] Modificar cupón")
    print("[4] Agregar cupón")

    opcionNum = input("Seleccione una opción: ")

    if opcionNum == "0":
        return
    elif opcionNum == "1":
        print("================================================================")
        print("- - - - - CUPONES ACTUALES - - - - -")
        if len(cuponesCodigo) == 0:
            print("No hay cupones disponibles.")
        else:
            for i in range(len(cuponesCodigo)):
                print(f"{cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarCupones()
    elif opcionNum == "2":
        print("================================================================")
        print("- - - - - BORRAR CUPÓN - - - - -")
        if len(cuponesCodigo) == 0:
            print("No hay cupones disponibles.")
            print("================================================================")
            input("Presione Enter para continuar...")
            return gestionarCupones()
        else:
            print("[0] Volver")
            for i in range(len(cuponesCodigo)):
                print(f"[{i+1}]{cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")

            borrarNum = input("Seleccione un cupón para borrar: ")

            if borrarNum == "0":
                return gestionarCupones()        
    elif opcionNum == "3":
        print("================================================================")
        print("- - - - - MODIFICAR CUPÓN - - - - -")
        if len(cuponesCodigo) == 0:
            print("No hay cupones disponibles.")
            print("================================================================")
            input("Presione Enter para continuar...")
            return gestionarCupones()
        else:
            print("[0] Volver")
            for i in range(len(cuponesCodigo)):
                print(f"[{i+1}]{cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")

            modificarNum = input("Seleccione un cupón para modificar: ")

            if modificarNum == "0":
                return gestionarCupones()
    elif opcionNum == "4":
        print("================================================================")
        print("- - - - - AGREGAR CUPÓN - - - - -")
        print("Ingrese 0 para cancelar ingreso")
        codigo = input("Ingrese el código del cupón (4 dígitos): ")
        
        if codigo == "0":
            return gestionarCupones()
        elif codigo in cuponesCodigo:
            print("================================================================")
            print("❌ Cupón ya existe")
        else:
            descuento = 0
            while descuento <= 0 or descuento > 100:
                descInput = input("Descuento (1-100): ")
                if esNumero(descInput):
                    descuento = int(descInput)
                    if descuento <= 0 or descuento > 100:
                        print("================================================================")
                        print("❌ Descuento debe estar entre 1 y 100")
                else:
                    print("================================================================")
                    print("❌ Ingrese un número válido")
            
            cuponesCodigo.append(codigo)
            cuponesDescuento.append(descuento)
            print("================================================================")
            print("✅ Cupón agregado")


    

def salir():
    """Función para salir del programa con confirmación del usuario"""
    print("================================================================")
    print("- - - - -❌ Salir ❌- - - - -")
    print("¿Está seguro que quiere salir (S/N)?: ", end="")
    
    confirmacion = input().upper()
    
    if confirmacion == 'S' or confirmacion == 'SI':
        print("\n================================================================")
        print("Exit⦿")
        print("¡Gracias por visitar nuestra tienda! 👋")
        print("================================================================")
        return True
    else:
        print("\n✅ Regresando al menú principal...")
        input("Presione Enter para continuar...")
        return False

def mostrarMenu():
    """Función que muestra el menú principal y gestiona la navegación"""
    while True:
        print("================================================================")
        print("E-Commerce⦿")
        print("================================================================")
        print("Bienvenido a la tienda virtual 🏪")
        print("[1] Comprar 💲")
        print("[2] Ver estadísticas totales 📈")
        print("[3] Ver estadísticas por producto 📊")
        print("[4] Ver estadísticas por cliente 🙋")
        print("[5] Gestionar Productos 📦")
        print("[6] Gestionar Cupones 🎟️")
        print("[7] Salir ❌")
        print("Seleccione opción: ", end="")
        
        opcion = input()

        if opcion == "1":
            Comprar()
        elif opcion == "2":
            verEstadisticas()
        elif opcion == "3":
            verEstadisticaProducto()
        elif opcion == "4":
            verEstadisticaCliente()
        elif opcion == "5":
            gestionarProductos()
        elif opcion == "6":
            gestionarCupones()
        elif opcion == "7":
            if salir():
                break
        else:
            print("================================================================")
            print("❌ Opción inválida. Por favor, seleccione una opción del 1 al 7.")
            print("================================================================")
            input("Presione Enter para continuar...")

# =================== PROGRAMA PRINCIPAL ===================

print("Iniciando E-Commerce...")
mostrarMenu()