# =================== SEMANA 2: FUNCIÓN CARGAR DATOS ===================

from datos import productosNombre, productosCategoria, productosPrecio, productosStock

def cargarProducto():
    """Función para cargar datos en listas paralelas con validación de duplicados"""
    print("\n=== CARGAR PRODUCTO ===")
    
    nombre = input("Nombre del producto: ")
    
    # VERIFICACIÓN PARA EVITAR DUPLICADOS - REQUISITO SEMANA 2
    productoExiste = False
    for i in range(len(productosNombre)):
        if productosNombre[i] == nombre:
            productoExiste = True
    
    if productoExiste:
        print("ERROR: Ya existe un producto con ese nombre")
    else:
        categoria = input("Categoría: ")
        precio = float(input("Precio: $"))
        stock = int(input("Stock: "))
        
        # CARGAR EN LISTAS PARALELAS
        productosNombre.append(nombre)
        productosCategoria.append(categoria)
        productosPrecio.append(precio)
        productosStock.append(stock)
        
        print("Producto cargado exitosamente")

def cargarDatosPrueba():
    """Carga 3 registros de prueba - REQUISITO SEMANA 2"""
    print("\n=== CARGANDO DATOS DE PRUEBA ===")
    
    # Al menos 3 registros
    datos = [
        ["Remera", "Ropa", 25.00, 10],
        ["Pantalón", "Ropa", 50.00, 5], 
        ["Zapatillas", "Calzado", 80.00, 8]
    ]
    
    for dato in datos:
        # Verificar duplicados
        existe = False
        for i in range(len(productosNombre)):
            if productosNombre[i] == dato[0]:
                existe = True
        
        if not existe:
            productosNombre.append(dato[0])
            productosCategoria.append(dato[1])
            productosPrecio.append(dato[2])
            productosStock.append(dato[3])
            print(f"Cargado: {dato[0]}")
        else:
            print(f"Ya existe: {dato[0]}")