#Estadistica producto + estadistica total
productosId = ["id0", "id1", "id2", "id3"]
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosCategoria = []
productosPrecio = []
productosStock = []
productosVendidos = [4, 2, 1, 1]
productosRecaudacion = [616, 559, 683, 514]

comprasId = [0, 1, 2, 3]
comprasDni = [123, 456, 789, 123]
comprasProductoId = ["id0", "id1", "id2", "id3"]
comprasCantidad = [4, 2, 1, 1]
comprasTotal = [616, 559, 683, 514]
comprasMedioPago = ["Efectivo", "Tarjeta", "Tarjeta", "Efectivo"]

# Listas de clientes
clienteDni = [123, 456, 789]
clienteRecaudacion = []
clienteCompras = []

def verEstadisticaProducto():
    #Pantalla inicial con productos
    print("- - - - - 📈 ESTADÍSTICAS POR PRODUCTO 📊 - - - - -")
    print("[0] Volver")
    for i in range(len(productosId)):
        print(f"[{i+1}] {productosNombre[i]} ({productosId[i]})")
    productoNum = int(input("Seleccione un producto: ")) - 1

    #Si presiona 0 salir de funcion
    if productoNum == (-1):
        return
    
    #Segunda pantalla con estadísticas para producto seleccionado
    print(f"- - - - - Estadísticas para {productosNombre[productoNum]} - - - - -")
    print(f"Facturación total: ${productosRecaudacion[productoNum]}")
    print(f"Cantidad de compras: {productosVendidos[productoNum]}")
    input("Presione cualquier tecla para volver")
    verEstadisticaProducto()

def verEstadisticasCliente():
    #Pantalla inicial con clientes
    print("- - - - - 📈 VENTAS POR CLIENTE 📊 - - - - -")
    print("[0] Volver")
    for i in range(len(clienteDni)):
        print(f"[{i+1}] {clienteDni[i]}")
    clienteNum = int(input("Seleccione un cliente: ")) - 1
    dniSelect = clienteDni[clienteNum]

    #Si presiona 0 salir de funcion
    if clienteNum == (-1):
        return

    #Segunda pantalla con estadísticas de todas las compras, filtrado por el cliente seleccionado
    print(f"Listado completo detallado de facturación de {dniSelect}:")
    for i in range(len(comprasId)):
        if comprasDni[i] == dniSelect:
            print(f"- Producto: {comprasProductoId[i]} | Cantidad comprado: {comprasCantidad[i]} | Total Facturado: ${comprasTotal[i]} | Tipo de Pago: {comprasMedioPago[i]}")
    input("Presione cualquier tecla para volver")
    verEstadisticasCliente()
    

def verEstadisticas():
    #Pantalla inicial con opciones
    print("- - - - - 📈 ESTADÍSTICAS DE VENTAS 📊 - - - - -")
    print("[0] Volver")
    print("[1] Facturación total")
    print("[2] Facturación por producto")
    print("[3] Cliente con mayor compra")
    print("[4] Facturación por cliente")
    opcionNum = input("Seleccione una opción: ")

    #Si presiona 0 salir de funcion
    if opcionNum == "0":
        return
    elif opcionNum == "1":
        dineroTotal = 0
        for producto in productosRecaudacion:
            dineroTotal += producto
        print(f"Facturación total: ${dineroTotal}")
        input("Presione cualquier tecla para volver")
        verEstadisticas()
    elif opcionNum == "2":
        print("Facturación total por producto (Ordenado por Facturación):")
        for i in range(len(productosId)):
            print(f"- {productosNombre[i]} ({productosId[i]}): ${productosRecaudacion[i]}")
        input("Presione cualquier tecla para volver")
        verEstadisticas()
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
        input("Presione cualquier tecla para volver")
        verEstadisticas()
    elif opcionNum == "4":
        verEstadisticasCliente()
        verEstadisticas()

verEstadisticas()