class Login:
    def __init__(self, usuario, contraseña):
            self.usuario = usuario
            self.contraseña = contraseña

    def login(self):
        if self.usuario == "Usuario" and self.contraseña == "Admin":
            return True
        else:
            return False
        
class Tiendita:
    def __init__(self):
        self.productos = {
            "Coca-cola 600ML $16": 16,
            "Sabritas $20": 20,
            "Garrafon de Agua $50": 50,
            "Pan Bimbo $45": 45,
            "Tortillas $22": 22,
            "Fabuloso $30": 30,
            "Cloro $20": 20,
            "Cepillo de dientes $17": 17,
            "Leche $26": 26,
            "Mazapan $7": 7
        }
        self.total = 0
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)
        precio = self.productos[producto]
        self.total += precio

    def eliminar_producto(self, producto):
        self.carrito.remove(producto)
        precio = self.productos[producto]
        self.total -= precio

    def comprar(self):
        if len(self.carrito) == 0:
            return False
        else:
            compra = "Su compra ha sido procesada.\nTotal a pagar: $" + str(self.total) + "\nCarrito de compras: " + "\n".join(self.carrito)
            self.carrito.clear()
            self.total = 0
            return compra