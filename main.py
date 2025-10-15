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

# =================== FUNCIONES  ===================
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
        for i in range(len(productosId)):
            print(f"- {productosNombre[i]} ({productosId[i]}): ${productosRecaudacion[i]}")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    elif opcionNum == "3":
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
    print(f"- - - - - Estadísticas para {productosNombre[productoNum]} - - - - -")
    print(f"Facturación total: ${productosRecaudacion[productoNum]}")
    print(f"Cantidad de compras: {productosVendidos[productoNum]}")
    print("================================================================")
    input("Presione Enter para continuar...")
    return verEstadisticaProducto()
    
def verEstadisticaCliente():
    #Pantalla inicial con clientes
    print("================================================================")
    print("- - - - - 📈 VENTAS POR CLIENTE 📊 - - - - -")
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
        print("[6] Cupones 🎟️")
        print("[7] Salir ❌")
        print("Seleccione opción: ", end="")
        
        opcion = input()

        if opcion == "1":
            print("\n[Función Comprar - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "2":
            verEstadisticas()
        elif opcion == "3":
            verEstadisticaProducto()
        elif opcion == "4":
            verEstadisticaCliente()
        elif opcion == "5":
            gestionarProductos()
        elif opcion == "6":
            print("\n[Función Cupones - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "7":
            if salir():
                break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione una opción del 1 al 7.")
            input("Presione Enter para continuar...")

# =================== PROGRAMA PRINCIPAL ===================

print("Iniciando E-Commerce...")
mostrarMenu()