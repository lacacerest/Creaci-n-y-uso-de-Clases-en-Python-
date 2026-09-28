class InventarioTienda:

    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):

        if precio <= 0:
            print("Error: el precio debe ser positivo.")
            return

        if cantidad <= 0:
            print("Error: la cantidad debe ser positiva.")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        self.productos.append(producto)

        print("Producto agregado correctamente.")

    def vender_producto(self, nombre, cantidad):

        if cantidad <= 0:
            print("Error: la cantidad debe ser positiva.")
            return

        for producto in self.productos:

            if producto["nombre"] == nombre:

                if cantidad <= producto["cantidad"]:
                    producto["cantidad"] -= cantidad
                    print("Venta realizada correctamente.")
                else:
                    print("Error: no hay suficiente stock.")

                return

        print("Error: el producto no existe.")

    def mostrar_inventario(self):

        if len(self.productos) == 0:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print("Nombre:", producto["nombre"])
            print("Precio: $", producto["precio"])
            print("Cantidad:", producto["cantidad"])
            print("-------------------------------")

    def producto_mas_caro(self):

        if len(self.productos) == 0:
            return None

        producto_caro = self.productos[0]

        for producto in self.productos:

            if producto["precio"] > producto_caro["precio"]:
                producto_caro = producto

        return producto_caro["nombre"], producto_caro["precio"]