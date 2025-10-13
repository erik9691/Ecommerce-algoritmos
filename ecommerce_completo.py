

# =================== LISTAS PARALELAS ===================

# Listas de productos
productosId = ["id0", "id1", "id2", "id3"]
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosCategoria = ["Vestimenta", "Vestimenta", "Tecnología", "Tecnología"]
productosPrecio = [15.00, 45.00, 499.99, 75.50]
productosStock = [50, 30, 10, 40]
productosVendidos = [0, 0, 0, 0]
productosRecaudacion = [0, 0, 0, 0]

# Listas de compras
comprasId = []
comprasDni = []
comprasProductoId = []
comprasCantidad = []
comprasTotal = []
comprasMedioPago = []

# Listas de clientes
clienteDni = []
clienteRecaudacion = []
clienteCompras = []

# Listas de cupones
cuponesCodigo = ["6852", "4182", "2186", "5742"]
cuponesDescuento = [15, 25, 30, 40]

# =================== FUNCIONES AUXILIARES ===================

def validarDNI(dni):
    """Función para validar que el DNI sea un número entero válido"""
    if len(dni) == 8:
        return True
    return False

def listarProductos():
    """Función para mostrar el catálogo de productos"""
    print("\n=== CATÁLOGO DE PRODUCTOS ===")
    for i in range(len(productosNombre)):
        print(f"[{i}] {productosNombre[i]} | ID: {productosId[i]} | Precio: ${productosPrecio[i]} | Stock: {productosStock[i]}")

def registrarCompra(dni, productoId, cantidad, medioPago, total):
    """Función para registrar una compra en las listas paralelas"""
    # Generar ID de compra
    if len(comprasId) == 0:
        nuevo_id = 1
    else:
        nuevo_id = max([int(x) for x in comprasId if str(x).isdigit()]) + 1
    
    # Agregar a listas de compras
    comprasId.append(str(nuevo_id))
    comprasDni.append(int(dni))
    comprasProductoId.append(productoId)
    comprasCantidad.append(cantidad)
    comprasTotal.append(total)
    comprasMedioPago.append(medioPago)
    
    # Actualizar cliente
    dni_num = int(dni)
    cliente_existe = False
    
    i = 0
    while i < len(clienteDni) and not cliente_existe:
        if clienteDni[i] == dni_num:
            clienteRecaudacion[i] += total
            clienteCompras[i] += 1
            cliente_existe = True
        i += 1
    
    if not cliente_existe:
        clienteDni.append(dni_num)
        clienteRecaudacion.append(total)
        clienteCompras.append(1)
    
    # Actualizar producto
    i = 0
    producto_encontrado = False
    while i < len(productosId) and not producto_encontrado:
        if productosId[i] == productoId:
            productosStock[i] -= cantidad
            productosVendidos[i] += cantidad
            productosRecaudacion[i] += total
            producto_encontrado = True
        i += 1

# =================== FUNCIONES DE CARGA DE DATOS ===================

def cargarProducto():
    """Función para cargar un nuevo producto verificando duplicados"""
    print("\n=== CARGAR NUEVO PRODUCTO ===")
    
    nombre = input("Ingrese el nombre del producto: ")
    
    # Verificar si el nombre ya existe
    for i in range(len(productosNombre)):
        if productosNombre[i].lower() == nombre.lower():
            print(f"❌ Error: Ya existe un producto con el nombre '{nombre}'")
            return False
    
    # Generar nuevo ID
    nuevo_id = f"id{len(productosId)}"
    
    categoria = input("Ingrese la categoría del producto: ")
    
    precio = 0
    while precio <= 0:
        precio_input = input("Ingrese el precio del producto: ")
        if precio_input.replace(".", "").isdigit():
            precio = float(precio_input)
            if precio <= 0:
                print("❌ El precio debe ser mayor a 0")
        else:
            print("❌ Debe ingresar un precio válido")
    
    stock = -1
    while stock < 0:
        stock_input = input("Ingrese el stock inicial: ")
        if stock_input.isdigit():
            stock = int(stock_input)
            if stock < 0:
                print("❌ El stock no puede ser negativo")
        else:
            print("❌ Debe ingresar un número válido")
    
    # Agregar a las listas paralelas
    productosId.append(nuevo_id)
    productosNombre.append(nombre)
    productosCategoria.append(categoria)
    productosPrecio.append(precio)
    productosStock.append(stock)
    productosVendidos.append(0)
    productosRecaudacion.append(0)
    
    print(f"✅ Producto '{nombre}' cargado exitosamente con ID: {nuevo_id}")
    return True

def cargarCliente():
    """Función para cargar un nuevo cliente verificando duplicados"""
    print("\n=== CARGAR NUEVO CLIENTE ===")
    
    dni = input("Ingrese el DNI del cliente (8 dígitos): ")
    
    # Validar DNI
    if not validarDNI(dni):
        print("❌ DNI inválido. Debe tener 8 dígitos.")
        return False
    
    # Verificar si el DNI ya existe
    dni_numero = int(dni)
    for i in range(len(clienteDni)):
        if clienteDni[i] == dni_numero:
            print(f"❌ Error: Ya existe un cliente con DNI: {dni}")
            return False
    
    # Agregar a las listas paralelas
    clienteDni.append(dni_numero)
    clienteRecaudacion.append(0)
    clienteCompras.append(0)
    
    print(f"✅ Cliente con DNI {dni} cargado exitosamente")
    return True

def cargarCupon():
    """Función para cargar un nuevo cupón verificando duplicados"""
    print("\n=== CARGAR NUEVO CUPÓN ===")
    
    codigo = input("Ingrese el código del cupón (4 dígitos): ")
    
    # Verificar si el código ya existe
    if codigo in cuponesCodigo:
        print(f"❌ Error: Ya existe un cupón con el código: {codigo}")
        return False
    
    descuento = 0
    while descuento <= 0 or descuento > 100:
        descuento_input = input("Ingrese el porcentaje de descuento (1-100): ")
        if descuento_input.isdigit():
            descuento = int(descuento_input)
            if descuento <= 0 or descuento > 100:
                print("❌ El descuento debe estar entre 1 y 100")
        else:
            print("❌ Debe ingresar un número válido")
    
    # Agregar a las listas paralelas
    cuponesCodigo.append(codigo)
    cuponesDescuento.append(descuento)
    
    print(f"✅ Cupón {codigo} con {descuento}% de descuento cargado exitosamente")
    return True

def mostrarDatosCargados():
    """Función para mostrar todos los datos cargados"""
    print("\n=== DATOS CARGADOS EN EL SISTEMA ===")
    
    # Mostrar productos
    print(f"\n📦 PRODUCTOS ({len(productosId)} registros):")
    if len(productosId) == 0:
        print("   No hay productos cargados.")
    else:
        for i in range(len(productosId)):
            print(f"   [{i}] ID: {productosId[i]} | {productosNombre[i]} | ${productosPrecio[i]} | Stock: {productosStock[i]} | Cat: {productosCategoria[i]}")
    
    # Mostrar clientes
    print(f"\n👥 CLIENTES ({len(clienteDni)} registros):")
    if len(clienteDni) == 0:
        print("   No hay clientes cargados.")
    else:
        for i in range(len(clienteDni)):
            print(f"   DNI: {clienteDni[i]} | Facturación: ${clienteRecaudacion[i]} | Compras: {clienteCompras[i]}")
    
    # Mostrar cupones
    print(f"\n🎟️ CUPONES ({len(cuponesCodigo)} registros):")
    if len(cuponesCodigo) == 0:
        print("   No hay cupones cargados.")
    else:
        for i in range(len(cuponesCodigo)):
            print(f"   Código: {cuponesCodigo[i]} | Descuento: {cuponesDescuento[i]}%")
    
    # Mostrar compras
    print(f"\n🛒 COMPRAS REALIZADAS ({len(comprasId)} registros):")
    if len(comprasId) == 0:
        print("   No hay compras registradas.")
    else:
        for i in range(len(comprasId)):
            print(f"   ID: {comprasId[i]} | DNI: {comprasDni[i]} | Producto: {comprasProductoId[i]} | Cant: {comprasCantidad[i]} | Total: ${comprasTotal[i]} | Pago: {comprasMedioPago[i]}")
    
    print("================================================================")

def ejecutarPruebasCarga():
    """Función para ejecutar pruebas de carga de al menos 3 registros"""
    print("\n=== EJECUTANDO PRUEBAS DE CARGA AUTOMÁTICA ===")
    
    # Prueba 1: Cargar 3 productos adicionales
    print("\n--- Cargando 3 productos de prueba ---")
    productos_prueba = [
        ["Zapatillas Deportivas", "Calzado", 85.99, 25],
        ["Tablet Android", "Tecnología", 299.50, 15], 
        ["Campera Invierno", "Vestimenta", 120.00, 20]
    ]
    
    for producto in productos_prueba:
        nuevo_id = f"id{len(productosId)}"
        productosId.append(nuevo_id)
        productosNombre.append(producto[0])
        productosCategoria.append(producto[1])
        productosPrecio.append(producto[2])
        productosStock.append(producto[3])
        productosVendidos.append(0)
        productosRecaudacion.append(0)
        print(f"   ✅ Producto cargado: {producto[0]} (ID: {nuevo_id})")
    
    # Prueba 2: Cargar 3 clientes de prueba
    print("\n--- Cargando 3 clientes de prueba ---")
    clientes_prueba = [11111111, 22222222, 33333333]
    
    for dni in clientes_prueba:
        if dni not in clienteDni:
            clienteDni.append(dni)
            clienteRecaudacion.append(0)
            clienteCompras.append(0)
            print(f"   ✅ Cliente cargado con DNI: {dni}")
        else:
            print(f"   ⚠️ Cliente {dni} ya existe (prueba de duplicados)")
    
    # Prueba 3: Cargar 3 cupones de prueba
    print("\n--- Cargando 3 cupones de prueba ---")
    cupones_prueba = [
        ["1111", 10],
        ["2222", 20],
        ["3333", 35]
    ]
    
    for cupon in cupones_prueba:
        if cupon[0] not in cuponesCodigo:
            cuponesCodigo.append(cupon[0])
            cuponesDescuento.append(cupon[1])
            print(f"   ✅ Cupón cargado: {cupon[0]} con {cupon[1]}% descuento")
        else:
            print(f"   ⚠️ Cupón {cupon[0]} ya existe (prueba de duplicados)")
    
    print("\n🎉 ¡Pruebas de carga completadas exitosamente!")
    print(f"   📦 Total productos: {len(productosId)}")
    print(f"   👥 Total clientes: {len(clienteDni)}")
    print(f"   🎟️ Total cupones: {len(cuponesCodigo)}")

def menuCargaDatos():
    """Función para el menú de gestión de datos"""
    continuar_menu = True
    while continuar_menu:
        print("\n=== MENÚ GESTIÓN DE DATOS ===")
        print("[1] Cargar Producto")
        print("[2] Cargar Cliente")  
        print("[3] Cargar Cupón")
        print("[4] Mostrar Datos Cargados")
        print("[5] Ejecutar Pruebas de Carga")
        print("[6] Volver al Menú Principal")
        print("Seleccione opción: ", end="")
        
        opcion = input()
        
        if opcion == "1":
            cargarProducto()
        elif opcion == "2":
            cargarCliente()
        elif opcion == "3":
            cargarCupon()
        elif opcion == "4":
            mostrarDatosCargados()
        elif opcion == "5":
            ejecutarPruebasCarga()
        elif opcion == "6":
            continuar_menu = False
        else:
            print("❌ Opción inválida. Seleccione una opción del 1 al 6.")
        
        input("\nPresione Enter para continuar...")

# =================== FUNCIÓN MENÚ PRINCIPAL ===================

def mostrarMenu():
    """Función que muestra el menú principal y gestiona la navegación"""
    continuar = True
    while continuar:
        print("\n================================================================")
        print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Com")
        print("================================================================")
        print("Bienvenido a la tienda virtual 🏪")
        print("[1] Comprar 💲")
        print("[2] Ver estadísticas totales 📈")
        print("[3] Ver estadísticas por producto 📊")
        print("[4] Buscar cliente por DNI 🙋")
        print("[5] Modificar Stock 📦")
        print("[6] Cupones 🎟️")
        print("[7] Gestión de Datos 📝")
        print("[8] Salir ❌")
        print("================================================================")
        print("Seleccione opción: ", end="")
        
        opcion = input()
        
        if opcion == "1":
            comprar()
        elif opcion == "2":
            verEstadisticas()
        elif opcion == "3":
            verEstadisticaProducto()
        elif opcion == "4":
            buscarCliente()
        elif opcion == "5":
            gestionarInventario()
        elif opcion == "6":
            mostrarCupones()
        elif opcion == "7":
            menuCargaDatos()
        elif opcion == "8":
            continuar = not salir()
        else:
            print("\n❌ Opción inválida. Por favor, seleccione una opción del 1 al 8.")
            input("Presione Enter para continuar...")

# =================== FUNCIÓN COMPRAR ===================

def comprar():
    """Función para realizar compras"""
    print("\n================================================================")
    print("- - - -💸 Compra 💸- - - -")
    
    # Solicitar DNI
    dni = input("Ingrese su DNI: ")
    if not validarDNI(dni):
        print("❌ DNI inválido. Debe tener 8 dígitos.")
        input("Presione Enter para continuar...")
        return
    
    # Solicitar medio de pago
    print("Medios de pago disponibles:")
    print("[1] Efectivo")
    print("[2] Tarjeta")
    medio_opcion = input("Seleccione medio de pago (1 o 2): ")
    
    if medio_opcion == "1":
        medio_pago = "Efectivo"
    elif medio_opcion == "2":
        medio_pago = "Tarjeta"
    else:
        print("❌ Medio de pago inválido.")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar productos
    print("\n- - - -🛒 Productos 🛒- - - -")
    listarProductos()
    
    # Seleccionar producto
    producto_input = input("\nSeleccione producto (número): ")
    if producto_input.isdigit():
        producto_indice = int(producto_input)
        if producto_indice < 0 or producto_indice >= len(productosNombre):
            print("❌ Producto no válido.")
            input("Presione Enter para continuar...")
            return
    else:
        print("❌ Debe ingresar un número válido.")
        input("Presione Enter para continuar...")
        return
    
    # Verificar stock
    if productosStock[producto_indice] <= 0:
        print("❌ Producto sin stock.")
        input("Presione Enter para continuar...")
        return
    
    # Solicitar cantidad
    cantidad_input = input(f"Ingrese la cantidad de {productosNombre[producto_indice]} a comprar: ")
    if cantidad_input.isdigit():
        cantidad = int(cantidad_input)
        if cantidad <= 0 or cantidad > productosStock[producto_indice]:
            print(f"❌ Cantidad inválida. Stock disponible: {productosStock[producto_indice]}")
            input("Presione Enter para continuar...")
            return
    else:
        print("❌ Debe ingresar un número válido.")
        input("Presione Enter para continuar...")
        return
    
    # Calcular subtotal
    subtotal = productosPrecio[producto_indice] * cantidad
    
    # Aplicar cupón
    descuento = 0
    aplicar_cupon = input("\n¿Desea aplicar cupones🎟️(s/n)?: ").lower()
    
    if aplicar_cupon == 's':
        codigo_cupon = input("Ingrese su cupón (0 para cancelar): ")
        if codigo_cupon != "0":
            if codigo_cupon in cuponesCodigo:
                indice_cupon = cuponesCodigo.index(codigo_cupon)
                descuento = cuponesDescuento[indice_cupon]
                print(f"✅ Cupón aplicado: {descuento}% de descuento")
            else:
                print("❌ Cupón inválido")
    
    # Calcular total final
    monto_descuento = subtotal * (descuento / 100)
    total = subtotal - monto_descuento
    
    # Mostrar resumen
    print(f"\n=== RESUMEN DE COMPRA ===")
    print(f"Producto: {productosNombre[producto_indice]}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${productosPrecio[producto_indice]}")
    print(f"Subtotal: ${subtotal}")
    if descuento > 0:
        print(f"Descuento ({descuento}%): -${monto_descuento}")
    print(f"Total: ${total}")
    print(f"Medio de pago: {medio_pago}")
    
    confirmacion = input("\n¿Confirmar compra? (s/n): ").lower()
    
    if confirmacion == 's':
        registrarCompra(dni, productosId[producto_indice], cantidad, medio_pago, total)
        print("\n================================================================")
        print("Compra exitosa ✔️")
        print("================================================================")
    else:
        print("Compra cancelada.")
    
    input("Presione Enter para continuar...")

# =================== FUNCIÓN SALIR ===================

def salir():
    """Función para salir del programa con confirmación del usuario"""
    print("\n================================================================")
    print("- - - - -❌ Salir ❌- - - - -")
    print("¿Está seguro que quiere salir (S/N)?: ", end="")
    
    confirmacion = input().upper()
    
    if confirmacion == 'S' or confirmacion == 'SI':
        print("\n================================================================")
        print("Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿Exit⦿")
        print("¡Gracias por visitar nuestra tienda! 👋")
        print("================================================================")
        return True
    else:
        print("\n✅ Regresando al menú principal...")
        input("Presione Enter para continuar...")
        return False

# =================== FUNCIÓN BUSCAR CLIENTE ===================

def buscarCliente():
    """Función para buscar cliente por DNI y mostrar su historial de compras"""
    print("\n================================================================")
    print("- - - - -🪪 Búsqueda clientes por DNI 🪪- - - - -")
    print("Ingrese el DNI del cliente: ", end="")
    
    dni_input = input()
    
    # Validar DNI
    if validarDNI(dni_input):
        # Buscar cliente en la lista
        cliente_encontrado = False
        indice_cliente = -1
        dni_num = int(dni_input)
        
        i = 0
        while i < len(clienteDni) and not cliente_encontrado:
            if clienteDni[i] == dni_num:
                cliente_encontrado = True
                indice_cliente = i
            i += 1
        
        if cliente_encontrado:
            # Mostrar información del cliente
            print(f"\n- - - - - Cliente ({dni_input}) - - - - -")
            print(f"Pagos totales: ${clienteRecaudacion[indice_cliente]}")
            print(f"Cantidad de compras: {clienteCompras[indice_cliente]}")
            print("\nProductos comprados:")
            
            # Contar productos comprados por este cliente
            productos_del_cliente = {}
            
            for i in range(len(comprasDni)):
                if comprasDni[i] == dni_num:
                    producto_id = comprasProductoId[i]
                    cantidad = comprasCantidad[i]
                    
                    # Buscar nombre del producto
                    nombre_producto = "Producto no encontrado"
                    j = 0
                    producto_encontrado = False
                    while j < len(productosId) and not producto_encontrado:
                        if productosId[j] == producto_id:
                            nombre_producto = productosNombre[j]
                            producto_encontrado = True
                        j += 1
                    
                    if nombre_producto in productos_del_cliente:
                        productos_del_cliente[nombre_producto] += cantidad
                    else:
                        productos_del_cliente[nombre_producto] = cantidad
            
            # Mostrar productos y cantidades
            if productos_del_cliente:
                for producto, cantidad in productos_del_cliente.items():
                    print(f"{producto}: {cantidad} unidades")
            else:
                print("No hay productos comprados registrados.")
        else:
            print(f"❌ No se encontró ningún cliente con DNI: {dni_input}")
    else:
        print("❌ DNI inválido. Debe ser un número de 8 dígitos.")
    
    print("================================================================")
    input("Presione Enter para continuar...")

# =================== FUNCIÓN ESTADÍSTICAS ===================

def verEstadisticas():
    """Función para mostrar estadísticas generales"""
    print("\n================================================================")
    print("- - - - -📈 ESTADÍSTICAS DE VENTAS 📊- - - - -")
    
    # Facturación total
    facturacion_total = sum(clienteRecaudacion)
    clientes_totales = len(clienteDni)
    
    print(f"1. Facturación total: ${facturacion_total}")
    print(f"   Personas distintas que compraron: {clientes_totales}")
    
    # Facturación por producto (ordenado por facturación)
    print("\n2. Facturación total por producto (Ordenado por Facturación):")
    
    # Crear lista de productos con su facturación y clientes
    productos_stats = []
    for i in range(len(productosId)):
        # Contar clientes únicos que compraron este producto
        clientes_producto = set()
        for j in range(len(comprasProductoId)):
            if comprasProductoId[j] == productosId[i]:
                clientes_producto.add(comprasDni[j])
        
        productos_stats.append({
            'nombre': productosNombre[i],
            'recaudacion': productosRecaudacion[i],
            'clientes': len(clientes_producto)
        })
    
    # Ordenar por recaudación (mayor a menor)
    for i in range(len(productos_stats)):
        for j in range(i + 1, len(productos_stats)):
            if productos_stats[i]['recaudacion'] < productos_stats[j]['recaudacion']:
                productos_stats[i], productos_stats[j] = productos_stats[j], productos_stats[i]
    
    for producto in productos_stats:
        print(f"   - {producto['nombre']} ${producto['recaudacion']} (comprado por {producto['clientes']} clientes)")
    
    # Cliente con compra más alta
    if clienteRecaudacion:
        max_compra = max(clienteRecaudacion)
        indice_max = clienteRecaudacion.index(max_compra)
        print(f"\n3. Cliente con la compra más alta:")
        print(f"   - DNI: {clienteDni[indice_max]}")
        print(f"   - Total de facturación: ${max_compra}")
    
    # Listado detallado por cliente
    print(f"\n4. Listado completo detallado de facturación por cliente:")
    
    # Crear lista de clientes con su información
    clientes_detalle = []
    for i in range(len(clienteDni)):
        # Buscar medio de pago más usado por el cliente
        medios_cliente = []
        for j in range(len(comprasDni)):
            if comprasDni[j] == clienteDni[i]:
                medios_cliente.append(comprasMedioPago[j])
        
        medio_principal = "N/A"
        if medios_cliente:
            # Contar medios de pago
            efectivo_count = medios_cliente.count("Efectivo")
            tarjeta_count = medios_cliente.count("Tarjeta")
            medio_principal = "Efectivo" if efectivo_count >= tarjeta_count else "Tarjeta"
        
        clientes_detalle.append({
            'dni': clienteDni[i],
            'facturacion': clienteRecaudacion[i],
            'medio_pago': medio_principal
        })
    
    # Ordenar por facturación (mayor a menor)
    for i in range(len(clientes_detalle)):
        for j in range(i + 1, len(clientes_detalle)):
            if clientes_detalle[i]['facturacion'] < clientes_detalle[j]['facturacion']:
                clientes_detalle[i], clientes_detalle[j] = clientes_detalle[j], clientes_detalle[i]
    
    for cliente in clientes_detalle:
        print(f"   - DNI: {cliente['dni']} | Total Facturado: ${cliente['facturacion']} | Tipo de Pago: {cliente['medio_pago']}")
    
    print("================================================================")
    input("Presione Enter para continuar...")

# =================== FUNCIÓN ESTADÍSTICAS POR PRODUCTO ===================

def verEstadisticaProducto():
    """Función para ver estadísticas de un producto específico"""
    print("\n================================================================")
    print("- - - - -📈 Estadísticas por producto 📊 - - - - -")
    
    # Mostrar productos
    listarProductos()
    
    producto_input = input("\nSeleccione producto (número): ")
    if producto_input.isdigit():
        producto_indice = int(producto_input)
        if producto_indice < 0 or producto_indice >= len(productosNombre):
            print("❌ Producto no válido.")
            input("Presione Enter para continuar...")
            return
    else:
        print("❌ Debe ingresar un número válido.")
        input("Presione Enter para continuar...")
        return
    
    producto_id = productosId[producto_indice]
    nombre_producto = productosNombre[producto_indice]
    
    # Contar clientes únicos y compras
    clientes_producto = set()
    compras_count = 0
    
    for i in range(len(comprasProductoId)):
        if comprasProductoId[i] == producto_id:
            clientes_producto.add(comprasDni[i])
            compras_count += 1
    
    print(f"\n- - - - - Estadísticas para producto {nombre_producto} - - - - -")
    print(f"Facturación total: ${productosRecaudacion[producto_indice]}")
    print(f"Cantidad de clientes: {len(clientes_producto)}")
    print(f"Cantidad de compras: {compras_count}")
    print(f"Unidades vendidas: {productosVendidos[producto_indice]}")
    print(f"Stock restante: {productosStock[producto_indice]}")
    print("================================================================")
    
    input("Presione Enter para continuar...")

# =================== FUNCIÓN GESTIONAR INVENTARIO ===================

def gestionarInventario():
    """Función para gestionar stock y precios"""
    print("\n================================================================")
    print("- - - - -📦 Modificar Stock 📦- - - - -")
    
    # Mostrar productos
    listarProductos()
    
    producto_input = input("\nSeleccione producto (número): ")
    if producto_input.isdigit():
        producto_indice = int(producto_input)
        if producto_indice < 0 or producto_indice >= len(productosNombre):
            print("❌ Producto no válido.")
            input("Presione Enter para continuar...")
            return
    else:
        print("❌ Debe ingresar un número válido.")
        input("Presione Enter para continuar...")
        return
    
    nombre_producto = productosNombre[producto_indice]
    
    print(f"\n- - - - - Stock de {nombre_producto} - - - - -")
    print(f"Stock actual: {productosStock[producto_indice]}")
    print(f"Precio actual: ${productosPrecio[producto_indice]}")
    
    print("\n[1] Modificar Stock")
    print("[2] Modificar Precio")
    print("[3] Volver")
    
    opcion = input("Seleccione opción: ")
    
    if opcion == "1":
        cambio_input = input(f"Modifique el stock de {nombre_producto} (+ para añadir, - para restar): ")
        # Verificar si es un número (incluyendo negativos)
        es_numero = False
        if cambio_input.startswith('-') and cambio_input[1:].isdigit():
            es_numero = True
            cambio = int(cambio_input)
        elif cambio_input.isdigit():
            es_numero = True
            cambio = int(cambio_input)
        elif cambio_input.startswith('+') and cambio_input[1:].isdigit():
            es_numero = True
            cambio = int(cambio_input)
        
        if es_numero:
            nuevo_stock = productosStock[producto_indice] + cambio
            
            if nuevo_stock < 0:
                print("❌ El stock no puede ser negativo.")
            else:
                productosStock[producto_indice] = nuevo_stock
                print(f"✅ Stock actualizado a: {nuevo_stock}")
        else:
            print("❌ Debe ingresar un número válido.")
    
    elif opcion == "2":
        precio_input = input(f"Ingrese el nuevo precio para {nombre_producto}: $")
        # Verificar si es un número decimal válido
        es_precio_valido = False
        if precio_input.replace(".", "").isdigit():
            nuevo_precio = float(precio_input)
            es_precio_valido = True
        
        if es_precio_valido:
            if nuevo_precio <= 0:
                print("❌ El precio debe ser mayor a 0.")
            else:
                productosPrecio[producto_indice] = nuevo_precio
                print(f"✅ Precio actualizado a: ${nuevo_precio}")
        else:
            print("❌ Debe ingresar un número válido.")
    
    elif opcion == "3":
        return
    
    else:
        print("❌ Opción inválida.")
    
    print("================================================================")
    input("Presione Enter para continuar...")

# =================== FUNCIÓN CUPONES ===================

def mostrarCupones():
    """Función para mostrar cupones disponibles"""
    print("\n================================================================")
    print("- - - - -🎟️ Cupones 🎟️- - - - -")
    
    if len(cuponesCodigo) == 0:
        print("No hay cupones disponibles.")
    else:
        for i in range(len(cuponesCodigo)):
            print(f"[{i+1}] {cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")
    
    print("================================================================")
    input("Presione Enter para continuar...")

# =================== PROGRAMA PRINCIPAL ===================

def main():
    """Función principal que ejecuta el programa"""
    print("Iniciando sistema E-Commerce...")
    mostrarMenu()

if __name__ == "__main__":
    main()