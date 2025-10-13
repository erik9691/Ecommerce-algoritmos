

# =================== LISTAS PARALELAS ===================

productosId = ["id0", "id1", "id2", "id3"]
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosCategoria = ["Vestimenta", "Vestimenta", "Tecnología", "Tecnología"]
productosPrecio = [15.40, 27.95, 683.00, 128.50]
productosStock = [46, 28, 9, 39]
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

# De menu.py - Listas paralelas para productos
productosId2 = [1, 2, 3, 4, 5, 6, 7]
productosNombre2 = ["Consola PS5", "Remera Algodon", "Pantalón Jean", "Auriculares BT", "Zapatillas", "Pijama", "Teclado electrico"]
productosCategoria2 = ["Gaming", "Ropa", "Ropa", "Tecnología", "Calzado", "Ropa", "Tecnología"]
productosPrecio2 = [120000, 5000, 8000, 15000, 25000, 3500, 12000]
productosStock2 = [10, 50, 30, 25, 20, 40, 15]
productosVendidos2 = [5, 25, 15, 12, 8, 30, 6]
productosRecaudacion2 = [600000, 125000, 120000, 180000, 200000, 105000, 72000]

# Listas paralelas para compras
comprasId2 = [1, 2, 3, 4, 5]
comprasDni2 = [12345678, 87654321, 11223344, 12345678, 55667788]
comprasProductoId2 = [1, 2, 3, 1, 4]
comprasCantidad2 = [2, 1, 2, 6, 1]
comprasTotal2 = [5000, 4500, 170000, 15000, 80000]
comprasMedioPago2 = ["Efectivo", "Tarjeta", "Tarjeta", "Efectivo", "Tarjeta"]

# Listas paralelas para clientes
clienteDni2 = [12345678, 87654321, 11223344, 55667788]
clienteRecaudacion2 = [20000, 4500, 170000, 80000]
clienteCompras2 = [2, 1, 1, 1]

# Listas paralelas para cupones
cuponesCodigo = [6852, 4182, 2186, 5742]
cuponesDescuento = [15, 25, 30, 40]

# De GestionarInventario.py
ProductosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
ProductosPrecio = [15.00, 45.00, 499.99, 75.50]
ProductosStock = [50, 30, 10, 40]

# =================== FUNCIONES DE VALIDACIÓN BÁSICA ===================

def esNumero(texto):
   

    numeros = "0123456789"
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter not in numeros:
            return False
    return True

def esNumeroDecimal(texto):
    # Verifica si es número decimal (puede tener un punto)
    puntoEncontrado = False
    for caracter in texto:
        if caracter == ".":
            if puntoEncontrado: 
                return False
            puntoEncontrado = True
        elif caracter < "0" or caracter > "9":
            return False
    return True

def aMinusculas(texto):
    
    resultado = ""
    for caracter in texto:
        if caracter == "A":
            resultado = resultado + "a"
        elif caracter == "B":
            resultado = resultado + "b"
        elif caracter == "C":
            resultado = resultado + "c"
        elif caracter == "D":
            resultado = resultado + "d"
        elif caracter == "E":
            resultado = resultado + "e"
        elif caracter == "F":
            resultado = resultado + "f"
        elif caracter == "G":
            resultado = resultado + "g"
        elif caracter == "H":
            resultado = resultado + "h"
        elif caracter == "I":
            resultado = resultado + "i"
        elif caracter == "J":
            resultado = resultado + "j"
        elif caracter == "K":
            resultado = resultado + "k"
        elif caracter == "L":
            resultado = resultado + "l"
        elif caracter == "M":
            resultado = resultado + "m"
        elif caracter == "N":
            resultado = resultado + "n"
        elif caracter == "O":
            resultado = resultado + "o"
        elif caracter == "P":
            resultado = resultado + "p"
        elif caracter == "Q":
            resultado = resultado + "q"
        elif caracter == "R":
            resultado = resultado + "r"
        elif caracter == "S":
            resultado = resultado + "s"
        elif caracter == "T":
            resultado = resultado + "t"
        elif caracter == "U":
            resultado = resultado + "u"
        elif caracter == "V":
            resultado = resultado + "v"
        elif caracter == "W":
            resultado = resultado + "w"
        elif caracter == "X":
            resultado = resultado + "x"
        elif caracter == "Y":
            resultado = resultado + "y"
        elif caracter == "Z":
            resultado = resultado + "z"
        else:
            resultado = resultado + caracter
    return resultado

# =================== FUNCIÓN PARA CARGAR DATOS ===================

def cargarProducto():
    print("\n=== CARGAR PRODUCTO ===")
    
    # Pedir nombre del producto
    nombre = input("Nombre del producto: ")
    
    # VERIFICACIÓN PARA EVITAR DUPLICADOS 
    productoExiste = False
    i = 0
    while i < len(productosNombre):
        if aMinusculas(productosNombre[i]) == aMinusculas(nombre):
            productoExiste = True
        i = i + 1
    
    if productoExiste:
        print("❌ ERROR: Ya existe un producto con ese nombre")
        print("No se puede cargar el producto duplicado")
    else:
        # Si no existe, pedir resto de datos
        categoria = input("Categoría: ")
        
        # Validar precio
        precio = 0
        while precio <= 0:
            precioTexto = input("Precio: $")
            if esNumeroDecimal(precioTexto):
                precio = float(precioTexto)
                if precio <= 0:
                    print("❌ El precio debe ser mayor a 0")
            else:
                print("❌ Ingrese un precio válido (solo números)")
        
        # Validar stock
        stock = -1
        while stock < 0:
            stockTexto = input("Stock inicial: ")
            if esNumero(stockTexto):
                stock = int(stockTexto)
                if stock < 0:
                    print("❌ El stock no puede ser negativo")
            else:
                print("❌ Ingrese un número válido para el stock")
        
        # Generar ID automático
        nuevoId = "PROD" + str(len(productosId) + 1)
        
        # CARGAR EN LISTAS PARALELAS - Requisito Semana 2
        productosId.append(nuevoId)
        productosNombre.append(nombre)
        productosCategoria.append(categoria)
        productosPrecio.append(precio)
        productosStock.append(stock)
        
        print("✅ Producto cargado exitosamente!")
        print(f"ID asignado: {nuevoId}")

# =================== FUNCIÓN PARA MOSTRAR DATOS ===================

def mostrarProductos():
    print("\n=== PRODUCTOS CARGADOS ===")
    
    if len(productosId) == 0:
        print("No hay productos cargados")
    else:
        print("Lista de todos los productos:")
        print("-" * 80)
        print("ID\t\tNOMBRE\t\t\tCATEGORÍA\tPRECIO\t\tSTOCK")
        print("-" * 80)
        
        i = 0
        while i < len(productosId):
            print(f"{productosId[i]}\t\t{productosNombre[i]}\t\t{productosCategoria[i]}\t\t${productosPrecio[i]}\t\t{productosStock[i]}")
            i = i + 1
        
        print("-" * 80)
        print(f"Total de productos: {len(productosId)}")

def mostrarTodosLosProductos():
    print("\n=== TODOS LOS PRODUCTOS DEL SISTEMA ===")
    
    # Mostrar productos principales
    print("\n--- PRODUCTOS PRINCIPALES ---")
    if len(productosNombre) > 0:
        i = 0
        while i < len(productosNombre):
            print(f"ID: {productosId[i]} | {productosNombre[i]} | Stock: {productosStock[i]} | Precio: ${productosPrecio[i]}")
            i = i + 1
    else:
        print("No hay productos principales")
    
    # Mostrar productos del menú (productosId2)
    print("\n--- PRODUCTOS DEL CATÁLOGO COMPLETO ---")
    if len(productosNombre2) > 0:
        i = 0
        while i < len(productosNombre2):
            print(f"ID: {productosId2[i]} | {productosNombre2[i]} | {productosCategoria2[i]} | Stock: {productosStock2[i]} | Precio: ${productosPrecio2[i]}")
            i = i + 1
    else:
        print("No hay productos en el catálogo")
    
    # Mostrar productos de inventario
    print("\n--- PRODUCTOS DE INVENTARIO ---")
    if len(ProductosNombre) > 0:
        i = 0
        while i < len(ProductosNombre):
            print(f"{i+1}. {ProductosNombre[i]} | Precio: ${ProductosPrecio[i]} | Stock: {ProductosStock[i]}")
            i = i + 1
    else:
        print("No hay productos en inventario")

# =================== FUNCIÓN PARA CARGAR DATOS DE PRUEBA ===================

def cargarDatosPrueba():
    print("\n=== CARGANDO 3 REGISTROS DE PRUEBA ===")
    
    # Datos de prueba - Requisito: al menos 3 registros
    datosPrueba = [
        ["Remera Algodón", "Vestimenta", 25.50, 50],
        ["Pantalón Jean", "Vestimenta", 65.00, 30],
        ["Auriculares Bluetooth", "Tecnología", 89.99, 15]
    ]
    
    # Cargar cada producto de prueba
    for datos in datosPrueba:
        nombre = datos[0]
        categoria = datos[1]
        precio = datos[2]
        stock = datos[3]
        
        # Verificar duplicados antes de cargar
        productoExiste = False
        i = 0
        while i < len(productosNombre):
            if aMinusculas(productosNombre[i]) == aMinusculas(nombre):
                productoExiste = True
            i = i + 1
        
        if not productoExiste:
            nuevoId = "PROD" + str(len(productosId) + 1)
            productosId.append(nuevoId)
            productosNombre.append(nombre)
            productosCategoria.append(categoria)
            productosPrecio.append(precio)
            productosStock.append(stock)
            print(f"✅ {nombre} cargado exitosamente")
        else:
            print(f"❌ {nombre} ya existe, no se carga")
    
    print("Carga de datos de prueba completada")

# =================== FUNCIÓN DE COMPRAS ===================

def comprar():
    print("\n=== COMPRAR PRODUCTOS ===")
    
    # Mostrar productos disponibles
    print("Productos disponibles:")
    print("-" * 60)
    print("ID\t\tPRODUCTO\t\tPRECIO\t\tSTOCK")
    print("-" * 60)
    
    i = 0
    while i < len(productosId):
        if productosStock[i] > 0:
            print(f"{productosId[i]}\t\t{productosNombre[i]}\t\t${productosPrecio[i]}\t\t{productosStock[i]}")
        i = i + 1
    
    # Seleccionar producto
    producto_id = input("\nIngrese el ID del producto: ")
    
    # Buscar producto
    producto_encontrado = False
    indice_producto = -1
    
    i = 0
    while i < len(productosId):
        if productosId[i] == producto_id:
            producto_encontrado = True
            indice_producto = i
            break
        i = i + 1
    
    if not producto_encontrado:
        print("❌ Producto no encontrado")
        return
    
    if productosStock[indice_producto] <= 0:
        print("❌ Producto sin stock")
        return
    
    # Solicitar cantidad
    cantidad_input = input(f"Cantidad de {productosNombre[indice_producto]} (Stock disponible: {productosStock[indice_producto]}): ")
    
    if esNumero(cantidad_input):
        cantidad = int(cantidad_input)
        if cantidad <= 0 or cantidad > productosStock[indice_producto]:
            print("❌ Cantidad inválida")
            return
    else:
        print("❌ Debe ingresar un número válido")
        return
    
    # Solicitar DNI
    dni = input("Ingrese su DNI (8 dígitos): ")
    if not validarDNI(dni):
        print("❌ DNI inválido")
        return
    
    # Calcular total
    subtotal = productosPrecio[indice_producto] * cantidad
    descuento = 0
    
    # Aplicar cupón
    usar_cupon = input("¿Desea usar un cupón? (s/n): ")
    if aMinusculas(usar_cupon) == "s":
        codigo_cupon = input("Ingrese el código del cupón: ")
        
        # Buscar cupón
        i = 0
        cupon_encontrado = False
        while i < len(cuponesCodigo):
            if str(cuponesCodigo[i]) == codigo_cupon:
                descuento = cuponesDescuento[i]
                cupon_encontrado = True
                print(f"✅ Cupón aplicado: {descuento}% de descuento")
                break
            i = i + 1
        
        if not cupon_encontrado:
            print("❌ Cupón inválido")
    
    # Calcular total final
    monto_descuento = subtotal * (descuento / 100)
    total = subtotal - monto_descuento
    
    # Mostrar resumen
    print(f"\n=== RESUMEN DE COMPRA ===")
    print(f"Producto: {productosNombre[indice_producto]}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${productosPrecio[indice_producto]}")
    print(f"Subtotal: ${subtotal}")
    if descuento > 0:
        print(f"Descuento ({descuento}%): -${monto_descuento}")
    print(f"Total: ${total}")
    
    # Confirmar compra
    confirmar = input("\n¿Confirmar compra? (s/n): ")
    if aMinusculas(confirmar) == "s":
        # Actualizar stock
        productosStock[indice_producto] = productosStock[indice_producto] - cantidad
        productosVendidos[indice_producto] = productosVendidos[indice_producto] + cantidad
        productosRecaudacion[indice_producto] = productosRecaudacion[indice_producto] + total
        
        # Registrar compra
        nuevo_id_compra = len(comprasId)
        comprasId.append(nuevo_id_compra)
        comprasDni.append(int(dni))
        comprasProductoId.append(producto_id)
        comprasCantidad.append(cantidad)
        comprasTotal.append(total)
        comprasMedioPago.append("Efectivo")  # Por simplificar
        
        print("✅ Compra realizada exitosamente!")
    else:
        print("Compra cancelada")

# =================== FUNCIONES DE ERIK.PY ===================

def verEstadisticaProducto():
    print("Datos de productos cargados:")
    
    i = 0
    while i < len(productosId):
        print("ID: " + str(productosId[i]) + " | Nombre: " + str(productosNombre[i]) + " | Vendidos: " + str(productosVendidos[i]) + " | Recaudación: $" + str(productosRecaudacion[i]))
        i = i + 1
        
    print("Buscar producto por ID (presione enter para cancelar):")
    
    busqueda = input()
    
    if busqueda == "":
        return
    
    i = 0
    encontrado = False
    
    while i < len(productosId):
        if str(productosId[i]) == busqueda:
            encontrado = True
            print("Producto encontrado:")
            print("ID: " + str(productosId[i]))
            print("Nombre: " + str(productosNombre[i]))
            print("Cantidad vendida: " + str(productosVendidos[i]))
            print("Recaudación total: $" + str(productosRecaudacion[i]))
            break
        i = i + 1
    
    if not encontrado:
        print("Producto no encontrado")

def verEstadisticasCliente():
    print("Estadísticas por cliente:")
    print("DNI | Recaudación | Cantidad de compras")
    
    i = 0
    while i < len(clienteDni):
        recaudacion = 0
        cantidad_compras = 0
        
        j = 0
        while j < len(comprasDni):
            if comprasDni[j] == clienteDni[i]:
                recaudacion = recaudacion + comprasTotal[j]
                cantidad_compras = cantidad_compras + 1
            j = j + 1
        
        print(str(clienteDni[i]) + " | $" + str(recaudacion) + " | " + str(cantidad_compras))
        i = i + 1

def verEstadisticas():
    recaudacionTotal = 0
    
    i = 0
    while i < len(comprasTotal):
        recaudacionTotal = recaudacionTotal + comprasTotal[i]
        i = i + 1
    
    cantidadCompras = len(comprasTotal)
    
    print("========== ESTADÍSTICAS GENERALES ==========")
    print("Recaudación total: $" + str(recaudacionTotal))
    print("Cantidad total de compras: " + str(cantidadCompras))
    print("")
    
    verEstadisticasCliente()
    print("")
    verEstadisticaProducto()

# =================== FUNCIONES DE MENU.PY ===================

def validarDNI(dni):
    contador = 0
    i = 0
    while i < len(dni):
        if dni[i] >= '0' and dni[i] <= '9':
            contador = contador + 1
        i = i + 1
    
    if contador == len(dni) and len(dni) == 8:
        return True
    else:
        return False

def buscarCliente():
    print("===== BUSCAR CLIENTE POR DNI =====")
    dni_input = input("Ingrese el DNI del cliente: ")
    
    if not validarDNI(dni_input):
        print("DNI inválido. Debe tener 8 dígitos.")
        return
    
    dni_buscar = int(dni_input)
    encontrado = False
    posicion = -1
    
    i = 0
    while i < len(clienteDni2):
        if clienteDni2[i] == dni_buscar:
            encontrado = True
            posicion = i
            break
        i = i + 1
    
    if encontrado:
        print("Cliente encontrado:")
        print("DNI:", clienteDni2[posicion])
        print("Total gastado: $", clienteRecaudacion2[posicion])
        print("Cantidad de compras:", clienteCompras2[posicion])
        
        print("\nHistorial de compras del cliente:")
        i = 0
        while i < len(comprasDni2):
            if comprasDni2[i] == dni_buscar:
                print("- Compra ID:", comprasId2[i])
                print("  Producto ID:", comprasProductoId2[i])
                print("  Cantidad:", comprasCantidad2[i])
                print("  Total: $", comprasTotal2[i])
                print("  Medio de pago:", comprasMedioPago2[i])
                print("")
            i = i + 1
    else:
        print("Cliente no encontrado.")

def mostrarMenuCompleto():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Ver productos")
    print("2. Buscar cliente por DNI")
    print("3. Ver estadísticas")
    print("4. Gestionar inventario")
    print("5. Salir")

def salir():
    respuesta = input("¿Está seguro que desea salir? (s/n): ")
    if respuesta == "s" or respuesta == "S":
        print("¡Hasta luego!")
        return True
    else:
        return False

# =================== FUNCIONES DE CUPONES (DE ECOMMERCE.PY) ===================

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

def mostrarCupones():
    print("\n=== CUPONES DISPONIBLES ===")
    
    if len(cuponesCodigo) == 0:
        print("No hay cupones cargados")
    else:
        print("Lista de cupones:")
        print("-" * 40)
        print("CÓDIGO\t\tDESCUENTO")
        print("-" * 40)
        
        i = 0
        while i < len(cuponesCodigo):
            print(f"{cuponesCodigo[i]}\t\t{cuponesDescuento[i]}%")
            i = i + 1
        
        print("-" * 40)
        print(f"Total de cupones: {len(cuponesCodigo)}")



def gestionar_inventario():
    print("===== GESTIÓN DE INVENTARIO =====")
    
    print("Productos disponibles:")
    i = 0
    while i < len(ProductosNombre):
        print(str(i+1) + ". " + ProductosNombre[i] + " - Precio: $" + str(ProductosPrecio[i]) + " - Stock: " + str(ProductosStock[i]))
        i = i + 1
    
    seleccion = input("Seleccione el número del producto a modificar (o presione Enter para volver): ")
    
    if seleccion == "":
        return
    
    # Validar que sea un número
    valido = True
    if seleccion == "":
        valido = False
    else:
        i = 0
        while i < len(seleccion):
            if seleccion[i] < '0' or seleccion[i] > '9':
                valido = False
                break
            i = i + 1
    
    if not valido:
        print("Selección inválida.")
        return
    
    indice = int(seleccion) - 1
    
    if indice < 0 or indice >= len(ProductosNombre):
        print("Número de producto inválido.")
        return
    
    print("Producto seleccionado:", ProductosNombre[indice])
    print("1. Modificar stock")
    print("2. Modificar precio")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nuevo_stock = input("Ingrese el nuevo stock: ")
        
        # Validar que sea un número
        valido = True
        if nuevo_stock == "":
            valido = False
        else:
            i = 0
            while i < len(nuevo_stock):
                if nuevo_stock[i] < '0' or nuevo_stock[i] > '9':
                    valido = False
                    break
                i = i + 1
        
        if valido:
            ProductosStock[indice] = int(nuevo_stock)
            print("Stock actualizado correctamente.")
        else:
            print("Stock inválido.")
    
    elif opcion == "2":
        nuevo_precio = input("Ingrese el nuevo precio: ")
        
        # Validar que sea un número decimal
        valido = True
        puntos = 0
        
        if nuevo_precio == "":
            valido = False
        else:
            i = 0
            while i < len(nuevo_precio):
                if nuevo_precio[i] == '.':
                    puntos = puntos + 1
                elif nuevo_precio[i] < '0' or nuevo_precio[i] > '9':
                    valido = False
                    break
                i = i + 1
            
            if puntos > 1:
                valido = False
        
        if valido:
            ProductosPrecio[indice] = float(nuevo_precio)
            print("Precio actualizado correctamente.")
        else:
            print("Precio inválido.")
    
    else:
        print("Opción inválida.")

# =================== FUNCIÓN PRINCIPAL ===================

def menuPrincipal():
    print("\n" + "="*50)
    print("E-COMMERCE - SEMANA 2")
    print("="*50)
    print("[1] 💲 Comprar productos")
    print("[2] Cargar producto")
    print("[3] Mostrar productos")  
    print("[4] Cargar datos de prueba")
    print("[5] Ver estadísticas")
    print("[6] Buscar cliente por DNI")
    print("[7] Gestionar inventario")
    print("[8] Cargar cupón")
    print("[9] Mostrar cupones")
    print("[10] Mostrar TODOS los productos")
    print("[11] Menú completo")
    print("[12] Salir")
    print("="*50)

def main():
    print("Iniciando Sistema E-Commerce...")
    print("Semana 2: Carga de Datos y Validaciones")
    
    continuar = True
    while continuar:
        menuPrincipal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            comprar()
        elif opcion == "2":
            cargarProducto()
        elif opcion == "3":
            mostrarProductos()
        elif opcion == "4":
            cargarDatosPrueba()
        elif opcion == "5":
            verEstadisticas()
        elif opcion == "6":
            buscarCliente()
        elif opcion == "7":
            gestionar_inventario()
        elif opcion == "8":
            cargarCupon()
        elif opcion == "9":
            mostrarCupones()
        elif opcion == "10":
            mostrarTodosLosProductos()
        elif opcion == "11":
            continuar2 = True
            while continuar2:
                mostrarMenuCompleto()
                opcion2 = input("Seleccione una opción: ")
                
                if opcion2 == "1":
                    mostrarTodosLosProductos()
                elif opcion2 == "2":
                    buscarCliente()
                elif opcion2 == "3":
                    verEstadisticas()
                elif opcion2 == "4":
                    gestionar_inventario()
                elif opcion2 == "5":
                    if salir():
                        continuar = False
                        continuar2 = False
                else:
                    print("Opción inválida")
        elif opcion == "12":
            print("¡Gracias por usar el sistema!")
            continuar = False
        else:
            print("❌ Opción inválida. Intente nuevamente.")
        
        if continuar:
            input("\nPresione Enter para continuar...")

# =================== PROGRAMA PRINCIPAL ===================

if __name__ == "__main__":
    main()