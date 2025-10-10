
ProductosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
ProductosPrecio = [15.00, 45.00, 499.99, 75.50]
ProductosStock = [50, 30, 10, 40]

def gestionar_inventario():
    
    print("\n--- GESTIÓN DE INVENTARIO Y PRECIOS ---")

    print("--- PRODUCTOS ACTUALES ---")
    for i in range(len(ProductosNombre)):
        print(f"[{i+1}] {ProductosNombre[i]} | Precio: ${ProductosPrecio[i]} | Stock: {ProductosStock[i]}")
     
    opcion=int(input("Seleccione el producto a modificar:__"))
    
    if opcion > len(ProductosNombre):
        print("⛝ OPCION NO VALIDA ⛝")
        gestionar_inventario()
    else:
        opcion=opcion-1
        print("-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-")
        print('\033[1m\033[4m' f"Edición del producto: {ProductosNombre[opcion]} | Stock: {ProductosStock[opcion]} | Precio: {ProductosPrecio[opcion]}" '\033[0m')
        print("")
        print("⚒---⚒︎---⚒---⚒---⚒---⚒---⚒---⚒---⚒---⚒---⚒---⚒")
        print("[1] Modificar Stock")
        print("[2] Modificar Precio")
        print("[3] ATRAS")
        print("")
        ajuste=int(input("Ingrese el ajuste deseado: "))
       

        if ajuste == 1:
            print(f"-----AJUSTANDO STOCK {ProductosNombre[opcion]} ({ProductosStock[opcion]})-------")
            ajusteStock=int(input("Ingrese + o - para modificar el stock: "))
            nuevoStock= ProductosStock[opcion] + ajusteStock
            if nuevoStock < 0:
                print("⛝       Cambio no realizado       ⛝ ")
                print("X---X---X---EL STOCK DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
                return gestionar_inventario()
            
            else:
                ProductosStock[opcion]=nuevoStock
                print("-----------------------------------------------")
                print(f"Nuevo Stock de {ProductosNombre[opcion]} | Stock actualizado: {ProductosStock[opcion]}")
                print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
                return gestionar_inventario()
        
        if ajuste == 2:
            print(f"-----AJUSTANDO PRECIO {ProductosNombre[opcion]} (${ProductosPrecio[opcion]})-------")
            ajustePrecio=int(input("Ingrese el nuevo precio del producto: $"))
            if ajustePrecio<=0:
                print("X---X---X---EL PRECIO DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
                print("⛝       Cambio no realizado       ⛝ ")
                gestionar_inventario()
            else:    
                ProductosPrecio[opcion]=ajustePrecio
                print("--------------------------------------------------")
                print(f"Nuevo Precio de {ProductosNombre[opcion]} | Precio actualizado: ${ProductosPrecio[opcion]}")
                print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
                gestionar_inventario()
        
        if ajuste == 3:
            gestionar_inventario()
            
        else:
            print("⛝ OPCION NO VALIDA ⛝")
            gestionar_inventario()
            
gestionar_inventario()

