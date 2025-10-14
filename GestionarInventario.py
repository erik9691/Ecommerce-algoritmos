
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosPrecio = [15.00, 45.00, 499.99, 75.50]
productosStock = [50, 30, 10, 40]

def gestionarStock():
    
    print("\n--- GESTIÓN DE INVENTARIO Y PRECIOS ---")

    print("--- PRODUCTOS ACTUALES ---")
    for i in range(len(productosNombre)):
        print(f"[{i+1}] {productosNombre[i]} | Precio: ${productosPrecio[i]} | Stock: {productosStock[i]}")
     
    opcion=int(input("Seleccione el producto a modificar:__"))
    
    if opcion > len(productosNombre):
        print("⛝ OPCION NO VALIDA ⛝")
        gestionarStock()
    else:
        opcion=opcion-1
        print("-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-")
        print('\033[1m\033[4m' f"Edición del producto: {productosNombre[opcion]} | Stock: {productosStock[opcion]} | Precio: {productosPrecio[opcion]}" '\033[0m')
        print("")
        print("⚒---⚒︎---⚒---⚒---⚒---⚒---⚒---⚒---⚒---⚒---⚒---⚒")
        print("[1] Modificar Stock")
        print("[2] Modificar Precio")
        print("[3] ATRAS")
        print("")
        ajuste=int(input("Ingrese el ajuste deseado: "))
       

        if ajuste == 1:
            print(f"-----AJUSTANDO STOCK {productosNombre[opcion]} ({productosStock[opcion]})-------")
            ajusteStock=int(input("Ingrese + o - para modificar el stock: "))
            nuevoStock= productosStock[opcion] + ajusteStock
            if nuevoStock < 0:
                print("⛝       Cambio no realizado       ⛝ ")
                print("X---X---X---EL STOCK DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
                return gestionarStock()
            
            else:
                productosStock[opcion]=nuevoStock
                print("-----------------------------------------------")
                print(f"Nuevo Stock de {productosNombre[opcion]} | Stock actualizado: {productosStock[opcion]}")
                print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
                return gestionarStock()
        
        if ajuste == 2:
            print(f"-----AJUSTANDO PRECIO {productosNombre[opcion]} (${productosPrecio[opcion]})-------")
            ajustePrecio=int(input("Ingrese el nuevo precio del producto: $"))
            if ajustePrecio<=0:
                print("X---X---X---EL PRECIO DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
                print("⛝       Cambio no realizado       ⛝ ")
                gestionarStock()
            else:    
                productosPrecio[opcion]=ajustePrecio
                print("--------------------------------------------------")
                print(f"Nuevo Precio de {productosNombre[opcion]} | Precio actualizado: ${productosPrecio[opcion]}")
                print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
                gestionarStock()
        
        if ajuste == 3:
            gestionarStock()
            
        else:
            print("⛝ OPCION NO VALIDA ⛝")
            gestionarStock()
            
gestionarStock()

