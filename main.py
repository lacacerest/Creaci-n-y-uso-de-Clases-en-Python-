from InventarioTienda import InventarioTienda

nombre_tienda = input("Ingresa el nombre de la tienda: ")

tienda = InventarioTienda(nombre_tienda)

while True:

    print("Tienda:", tienda.nombre_tienda)
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Consultar producto más caro")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:

        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad: "))

        tienda.agregar_producto(nombre, precio, cantidad)

    elif opcion == 2:

        nombre = input("Nombre del producto a vender: ")
        cantidad = int(input("Cantidad a vender: "))

        tienda.vender_producto(nombre, cantidad)

    elif opcion == 3:

        tienda.mostrar_inventario()

    elif opcion == 4:

        resultado = tienda.producto_mas_caro()

        if resultado is None:
            print("No hay productos en el inventario.")
        else:
            nombre, precio = resultado

            print("Producto:", nombre)
            print("Precio: $", precio)

    elif opcion == 5:

        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")

