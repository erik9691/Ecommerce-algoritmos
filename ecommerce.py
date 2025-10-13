# =================== FUNCIONES AUXILIARES ===================

def esNumero(texto):
 
    numeros = "0123456789"
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter not in numeros:
            return False
    return True

def aMinusculas(texto):

    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for caracter in texto:
        encontrado = False
        i = 0
        while i < len(mayusculas) and not encontrado:
            if caracter == mayusculas[i]:
                resultado = resultado + minusculas[i]
                encontrado = True
            i = i + 1
        
        if not encontrado:
            resultado = resultado + caracter
    
    return resultado

def aMayusculas(texto):
    # Reemplaza .upper() - convierte texto a mayúsculas
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for caracter in texto:
        encontrado = False
        i = 0
        while i < len(minusculas) and not encontrado:
            if caracter == minusculas[i]:
                resultado = resultado + mayusculas[i]
                encontrado = True
            i = i + 1
        
        if not encontrado:
            resultado = resultado + caracter
    
    return resultado

def quitarPuntos(texto):
  
    resultado = ""
    for caracter in texto:
        if caracter != ".":
            resultado = resultado + caracter
    return resultado

def esNumeroDecimal(texto):
    # Verifica si es número decimal (puede tener un punto)
    textoSinPuntos = quitarPuntos(texto)
    return esNumero(textoSinPuntos)

# =================== LISTAS PARALELAS ===================

# Productos
productosId = ["id0", "id1", "id2", "id3"]
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosCategoria = ["Vestimenta", "Vestimenta", "Tecnología", "Tecnología"]
productosPrecio = [15.00, 45.00, 499.99, 75.50]
productosStock = [50, 30, 10, 40]
productosVendidos = [0, 0, 0, 0]
productosRecaudacion = [0, 0,  0, 0]

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

def validarDNI(dni):
    if len(dni) == 8:
        return True
    return False

def mostrarProductos():
    print("\n=== PRODUCTOS DISPONIBLES ===")
    for i in range(len(productosNombre)):
        print(f"[{i}] {productosNombre[i]} - ${productosPrecio[i]} (Stock: {productosStock[i]})")

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

# =================== FUNCIONES DE CARGA ===================

def cargarProducto():
    print("\n=== CARGAR PRODUCTO ===")
    nombre = input("Nombre del producto: ")
    
    # Verificar duplicados
    productoExiste = False
    for i in range(len(productosNombre)):
        if aMinusculas(productosNombre[i]) == aMinusculas(nombre):
            productoExiste = True
    
    if productoExiste:
        print("❌ Ya existe un producto con ese nombre")
    else:
        categoria = input("Categoría: ")
        
        precio = 0
        while precio <= 0:
            precioInput = input("Precio: $")
            if esNumeroDecimal(precioInput):
                precio = float(precioInput)
                if precio <= 0:
                    print("❌ El precio debe ser mayor a 0")
            else:
                print("❌ Ingrese un precio válido")
        
        stock = -1
        while stock < 0:
            stockInput = input("Stock inicial: ")
            if esNumero(stockInput):
                stock = int(stockInput)
                if stock < 0:
                    print("❌ El stock no puede ser negativo")
            else:
                print("❌ Ingrese un número válido")

        nuevoId = f"id{len(productosId)}"
        productosId.append(nuevoId)
        productosNombre.append(nombre)
        productosCategoria.append(categoria)
        productosPrecio.append(precio)
        productosStock.append(stock)
        productosVendidos.append(0)
        productosRecaudacion.append(0)
        
        print(f"✅ Producto '{nombre}' agregado")

def cargarCliente():
    print("\n=== CARGAR CLIENTE ===")
    dni = input("DNI (8 dígitos): ")
    
    if validarDNI(dni):
        dniNumero = int(dni)
        clienteExiste = False
        
        for i in range(len(clienteDni)):
            if clienteDni[i] == dniNumero:
                clienteExiste = True
        
        if clienteExiste:
            print("❌ Cliente ya existe")
        else:
            clienteDni.append(dniNumero)
            clienteRecaudacion.append(0)
            clienteCompras.append(0)
            print("✅ Cliente agregado")
    else:
        print("❌ DNI inválido")

def cargarCupon():
    print("\n=== CARGAR CUPÓN ===")
    codigo = input("Código del cupón: ")
    
    if codigo in cuponesCodigo:
        print("❌ Cupón ya existe")
    else:
        descuento = 0
        while descuento <= 0 or descuento > 100:
            descInput = input("Descuento (1-100): ")
            if esNumero(descInput):
                descuento = int(descInput)
                if descuento <= 0 or descuento > 100:
                    print("❌ Descuento debe estar entre 1 y 100")
            else:
                print("❌ Ingrese un número válido")
        
        cuponesCodigo.append(codigo)
        cuponesDescuento.append(descuento)
        print("✅ Cupón agregado")

def mostrarDatos():
    print(f"\n=== RESUMEN DEL SISTEMA ===")
    print(f"Productos: {len(productosId)}")
    print(f"Clientes: {len(clienteDni)}")
    print(f"Cupones: {len(cuponesCodigo)}")
    print(f"Compras: {len(comprasId)}")
    
    if len(productosId) > 0:
        print("\nProductos:")
        for i in range(len(productosId)):
            print(f"  {productosNombre[i]} - ${productosPrecio[i]}")

def ejecutarPruebas():
    print("\n=== EJECUTANDO PRUEBAS ===")
    
    # 3 productos de prueba
    productosTest = [
        ["Zapatillas", "Calzado", 85.99, 25],
        ["Tablet", "Tecnología", 299.50, 15], 
        ["Campera", "Vestimenta", 120.00, 20]
    ]
    
    for producto in productosTest:
        nuevoId = f"id{len(productosId)}"
        productosId.append(nuevoId)
        productosNombre.append(producto[0])
        productosCategoria.append(producto[1])
        productosPrecio.append(producto[2])
        productosStock.append(producto[3])
        productosVendidos.append(0)
        productosRecaudacion.append(0)
        print(f"✅ {producto[0]} agregado")
    
    # 3 clientes de prueba
    clientesTest = [11111111, 22222222, 33333333]
    for dni in clientesTest:
        if dni not in clienteDni:
            clienteDni.append(dni)
            clienteRecaudacion.append(0)
            clienteCompras.append(0)
            print(f"✅ Cliente {dni} agregado")
    
    # 3 cupones de prueba
    cuponesTest = [["1111", 10], ["2222", 20], ["3333", 30]]
    for cupon in cuponesTest:
        if cupon[0] not in cuponesCodigo:
            cuponesCodigo.append(cupon[0])
            cuponesDescuento.append(cupon[1])
            print(f"✅ Cupón {cupon[0]} agregado")
    
    print("Pruebas completadas")

# =================== FUNCIONES PRINCIPALES ===================

def comprar():
    print("\n=== COMPRAR ===")
    
    # DNI
    dni = input("Ingrese su DNI: ")
    if validarDNI(dni):
        # Medio de pago
        print("[1] Efectivo [2] Tarjeta")
        medio = input("Medio de pago: ")
        if medio == "1":
            medioPago = "Efectivo"
        elif medio == "2":
            medioPago = "Tarjeta"
        else:
            medioPago = ""

        if medioPago != "":
            # Mostrar productos
            mostrarProductos()
            
            # Seleccionar producto
            prodInput = input("Seleccione producto (número): ")
            if esNumero(prodInput):
                productoIndice = int(prodInput)
                if productoIndice >= 0 and productoIndice < len(productosNombre):
                    if productosStock[productoIndice] > 0:
                        # Cantidad
                        cantInput = input(f"Cantidad de {productosNombre[productoIndice]}: ")
                        if esNumero(cantInput):
                            cantidad = int(cantInput)
                            if cantidad > 0 and cantidad <= productosStock[productoIndice]:
                                # Calcular total
                                subtotal = productosPrecio[productoIndice] * cantidad
                                descuento = 0
                                
                                # Cupón
                                usarCupon = input("¿Usar cupón? (s/n): ")
                                if aMinusculas(usarCupon) == "s":
                                    codigo = input("Código del cupón: ")
                                    if codigo in cuponesCodigo:
                                        indiceCupon = cuponesCodigo.index(codigo)
                                        descuento = cuponesDescuento[indiceCupon]
                                        print(f"Cupón aplicado: {descuento}% descuento")
                                    else:
                                        print("Cupón inválido")
                                
                                total = subtotal * (100 - descuento) / 100
                                
                                # Confirmar
                                print(f"\nResumen: {productosNombre[productoIndice]} x{cantidad}")
                                print(f"Subtotal: ${subtotal}")
                                if descuento > 0:
                                    print(f"Descuento: {descuento}%")
                                print(f"Total: ${total}")
                                
                                confirmar = input("Confirmar compra (s/n): ")
                                if aMinusculas(confirmar) == "s":
                                    registrarCompra(dni, productosId[productoIndice], cantidad, medioPago, total)
                                    print("✅ Compra realizada")
                                else:
                                    print("Compra cancelada")
                            else:
                                print(f"❌ Cantidad inválida. Stock: {productosStock[productoIndice]}")
                        else:
                            print("❌ Debe ingresar un número")
                    else:
                        print("❌ Sin stock")
                else:
                    print("❌ Producto no válido")
            else:
                print("❌ Debe ingresar un número")
        else:
            print("❌ Opción inválida")
    else:
        print("❌ DNI inválido")
    
    input("Enter para continuar...")

def verEstadisticas():
    print("\n=== ESTADÍSTICAS ===")
    
    if len(clienteRecaudacion) == 0:
        print("No hay ventas registradas")
    else:
        # Facturación total
        totalFacturado = sum(clienteRecaudacion)
        clientesTotal = len(clienteDni)
        print(f"1. Facturación total: ${totalFacturado}")
        print(f"   Clientes distintos: {clientesTotal}")

        # Por producto
        print("\n2. Facturación por producto:")
        for i in range(len(productosId)):
            clientesProducto = 0
            for j in range(len(comprasProductoId)):
                if comprasProductoId[j] == productosId[i]:
                    dniCompra = comprasDni[j]
                    yaContado = False
                    for k in range(j):
                        if comprasDni[k] == dniCompra and comprasProductoId[k] == productosId[i]:
                            yaContado = True
                    if not yaContado:
                        clientesProducto = clientesProducto + 1

            print(f"   {productosNombre[i]}: ${productosRecaudacion[i]} ({clientesProducto} clientes)")
        
        # Cliente con mayor compra
        if len(clienteRecaudacion) > 0:
            maxCompra = max(clienteRecaudacion)
            indiceMax = clienteRecaudacion.index(maxCompra)
            print(f"\n3. Cliente con mayor facturación:")
            print(f"   DNI: {clienteDni[indiceMax]} - ${maxCompra}")

        # Detalle por cliente
        print(f"\n4. Detalle por cliente:")
        for i in range(len(clienteDni)):
            medioPrincipal = "N/A"
            efectivoCount = 0
            tarjetaCount = 0

            for j in range(len(comprasDni)):
                if comprasDni[j] == clienteDni[i]:
                    if comprasMedioPago[j] == "Efectivo":
                        efectivoCount = efectivoCount + 1
                    else:
                        tarjetaCount = tarjetaCount + 1

            if efectivoCount >= tarjetaCount:
                medioPrincipal = "Efectivo"
            else:
                medioPrincipal = "Tarjeta"

            print(f"   DNI: {clienteDni[i]} | ${clienteRecaudacion[i]} | {medioPrincipal}")

    input("Enter para continuar...")

def verEstadisticaProducto():
    print("\n=== ESTADÍSTICAS POR PRODUCTO ===")
    mostrarProductos()
    
    prodInput = input("Seleccione producto: ")
    if esNumero(prodInput):
        indice = int(prodInput)
        if indice >= 0 and indice < len(productosNombre):
            # Contar clientes únicos
            productoId = productosId[indice]
            clientesUnicos = []
            comprasCount = 0
            
            for i in range(len(comprasProductoId)):
                if comprasProductoId[i] == productoId:
                    comprasCount = comprasCount + 1
                    dni = comprasDni[i]
                    if dni not in clientesUnicos:
                        clientesUnicos.append(dni)

            print(f"\nEstadísticas de {productosNombre[indice]}:")
            print(f"Facturación: ${productosRecaudacion[indice]}")
            print(f"Clientes: {len(clientesUnicos)}")
            print(f"Compras: {comprasCount}")
            print(f"Unidades vendidas: {productosVendidos[indice]}")
        else:
            print("❌ Producto inválido")
    else:
        print("❌ Número inválido")
    
    input("Enter para continuar...")

def buscarCliente():
    print("\n=== BUSCAR CLIENTE ===")
    dniInput = input("DNI del cliente: ")
    
    if validarDNI(dniInput):
        dniNum = int(dniInput)
        clienteEncontrado = False
        indiceCliente = -1
        
        i = 0
        while i < len(clienteDni) and not clienteEncontrado:
            if clienteDni[i] == dniNum:
                clienteEncontrado = True
                indiceCliente = i
            i = i + 1

        if clienteEncontrado:
            print(f"\nCliente: {dniInput}")
            print(f"Total facturado: ${clienteRecaudacion[indiceCliente]}")
            print(f"Compras realizadas: {clienteCompras[indiceCliente]}")
            
            print("\nProductos comprados:")
            productosCliente = {}
            
            for i in range(len(comprasDni)):
                if comprasDni[i] == dniNum:
                    prodId = comprasProductoId[i]
                    cantidad = comprasCantidad[i]

                    nombreProducto = "Producto no encontrado"
                    j = 0
                    encontrado = False
                    while j < len(productosId) and not encontrado:
                        if productosId[j] == prodId:
                            nombreProducto = productosNombre[j]
                            encontrado = True
                        j = j + 1

                    if nombreProducto in productosCliente:
                        productosCliente[nombreProducto] = productosCliente[nombreProducto] + cantidad
                    else:
                        productosCliente[nombreProducto] = cantidad

            for producto in productosCliente:
                print(f"  {producto}: {productosCliente[producto]} unidades")
        else:
            print("❌ Cliente no encontrado")
    else:
        print("❌ DNI inválido")
    
    input("Enter para continuar...")

def salir():
    print("\n=== SALIR ===")
    respuesta = input("¿Está seguro? (S/N): ")
    if aMayusculas(respuesta) == "S":
        print("¡Gracias por usar el sistema!")
        confirmarSalida = True
    else:
        confirmarSalida = False
    return confirmarSalida

def menuCarga():
    continuar = True
    while continuar:
        print("\n=== GESTIÓN DE DATOS ===")
        print("[1] Cargar Producto")
        print("[2] Cargar Cliente") 
        print("[3] Cargar Cupón")
        print("[4] Mostrar Datos")
        print("[5] Ejecutar Pruebas")
        print("[6] Volver")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            cargarProducto()
        elif opcion == "2":
            cargarCliente()
        elif opcion == "3":
            cargarCupon()
        elif opcion == "4":
            mostrarDatos()
        elif opcion == "5":
            ejecutarPruebas()
        elif opcion == "6":
            continuar = False
        else:
            print("❌ Opción inválida")
        
        if opcion != "6":
            input("Enter para continuar...")

def mostrarMenu():
    continuar = True
    while continuar:
        print("\n" + "="*50)
        print("E-COMMERCE")
        print("="*50)
        print("[1] Comprar")
        print("[2] Ver estadísticas totales")
        print("[3] Ver estadísticas por producto")
        print("[4] Buscar cliente por DNI")
        print("[5] Gestión de datos")
        print("[6] Salir")
        print("="*50)
        
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            comprar()
        elif opcion == "2":
            verEstadisticas()
        elif opcion == "3":
            verEstadisticaProducto()
        elif opcion == "4":
            buscarCliente()
        elif opcion == "5":
            menuCarga()
        elif opcion == "6":
            continuar = not salir()
        else:
            print("❌ Opción inválida")
            input("Enter para continuar...")

# =================== PROGRAMA PRINCIPAL ===================

if __name__ == "__main__":
    print("Iniciando E-Commerce...")
    mostrarMenu()