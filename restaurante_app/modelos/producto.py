# modelos/producto.py
# Modulo del modelo Producto.
# Representa un plato o bebida que el restaurante tiene
# en su menu. Cada producto lleva un stock del dia para
# saber cuantas unidades quedan disponibles.


class Producto:
    """Representa un plato o bebida del menu del restaurante."""

    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo        # identificador del producto
        self.nombre = nombre        # nombre del plato o bebida
        self.categoria = categoria  # Entrada, Fuerte, Bebida o Postre
        self.precio = precio        # precio en dolares
        self.stock = stock          # unidades disponibles para ese dia

    def reducir_stock(self):
        """Descuenta una unidad del stock al registrar un pedido."""
        if self.stock > 0:
            self.stock -= 1

    def reponer_stock(self, cantidad):
        """Agrega unidades al stock del producto."""
        self.stock += cantidad

    def esta_disponible(self):
        """Retorna True si todavia hay unidades disponibles."""
        return self.stock > 0

    def __str__(self):
        estado = "disponible" if self.esta_disponible() else "agotado"
        return (f"{self.codigo} | {self.nombre} | {self.categoria} "
                f"| ${self.precio:.2f} | stock: {self.stock} | {estado}")
