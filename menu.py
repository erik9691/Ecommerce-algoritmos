# E-Commerce - Sistema de Tienda Virtual
# Trabajo Práctico de Introducción a la Algoritmia
# Autores: Acuña Laura, Baldanti Juana, Berot Erik, Pastor Bernardo

# Listas paralelas para productos
productosId = [1, 2, 3, 4, 5, 6, 7]
productosNombre = ["Consola PS5", "Remera Algodon", "Pantalón Jean", "Auriculares BT", "Zapatillas", "Pijama", "Teclado electrico"]
productosCategoria = ["Gaming", "Ropa", "Ropa", "Tecnología", "Calzado", "Ropa", "Tecnología"]
productosPrecio = [120000, 5000, 8000, 15000, 25000, 3500, 12000]
productosStock = [10, 50, 30, 25, 20, 40, 15]
productosVendidos = [5, 25, 15, 12, 8, 30, 6]
productosRecaudacion = [600000, 125000, 120000, 180000, 200000, 105000, 72000]

# Listas paralelas para compras
comprasId = [1, 2, 3, 4, 5]
comprasDni = [12345678, 87654321, 11223344, 12345678, 55667788]
comprasProductoId = [1, 2, 3, 1, 4]
comprasCantidad = [2, 1, 2, 6, 1]
comprasTotal = [5000, 4500, 170000, 15000, 80000]
comprasMedioPago = ["Efectivo", "Tarjeta", "Tarjeta", "Efectivo", "Tarjeta"]

# Listas paralelas para clientes
clienteDni = [12345678, 87654321, 11223344, 55667788]
clienteRecaudacion = [20000, 4500, 170000, 80000]
clienteCompras = [2, 1, 1, 1]

# Listas paralelas para cupones
cuponesCodigo = [6852, 4182, 2186, 5742]
cuponesDescuento = [15, 25, 30, 40]

def validarDNI(dni):
    """Función para validar que el DNI sea un número entero válido"""
    if len(dni) == 8:
        return True
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
        print("[4] Buscar cliente por DNI 🙋")
        print("[5] Modificar Stock 📦")
        print("[6] Cupones 🎟️")
        print("[7] Salir ❌")
        print("Seleccione opción: ", end="")
        
        opcion = input()
        
        if opcion == "1":
            print("\n[Función Comprar - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "2":
            print("\n[Función Ver estadísticas totales - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            print("\n[Función Ver estadísticas por producto - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "4":
            buscarCliente()
        elif opcion == "5":
            print("\n[Función Modificar Stock - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "6":
            print("\n[Función Cupones - En desarrollo]")
            input("Presione Enter para continuar...")
        elif opcion == "7":
            if salir():
                break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione una opción del 1 al 7.")
            input("Presione Enter para continuar...")

def salir():
    """Función para salir del programa con confirmación del usuario"""
    print("\n================================================================")
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

def buscarCliente():
    """Función para buscar cliente por DNI y mostrar su historial de compras"""
    print("\n================================================================")
    print("- - - - -🪪 Búsqueda clientes por DNI 🪪- - - - -")
    print("Ingrese el DNI del cliente: ", end="")
    
    dni_input = input()
    
    # Validar DNI
    if not validarDNI(dni_input):
        print("❌ DNI inválido. Debe ser un número de 8 dígitos.")
        input("Presione Enter para continuar...")
        return
    
    # Buscar cliente en la lista
    cliente_encontrado = False
    indice_cliente = -1
    
    for i in range(len(clienteDni)):
        if str(clienteDni[i]) == dni_input:
            cliente_encontrado = True
            indice_cliente = i
            break
    
    if not cliente_encontrado:
        print(f"❌ No se encontró ningún cliente con DNI: {dni_input}")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar información del cliente
    print(f"\n- - - - - Cliente ({dni_input}) - - - - -")
    print(f"Pagos totales: ${clienteRecaudacion[indice_cliente]}")
    print(f"Cantidad de compras: {clienteCompras[indice_cliente]}")
    print("\nProductos comprados:")
    
    # Contar productos comprados por este cliente
    productos_del_cliente = {}
    
    for i in range(len(comprasDni)):
        if comprasDni[i] == int(dni_input):
            producto_id = comprasProductoId[i]
            cantidad = comprasCantidad[i]
            
            # Buscar nombre del producto
            for j in range(len(productosId)):
                if productosId[j] == producto_id:
                    nombre_producto = productosNombre[j]
                    break
            
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
    
    print("================================================================")
    input("Presione Enter para continuar...")

# Programa principal
if __name__ == "__main__":
    mostrarMenu()
