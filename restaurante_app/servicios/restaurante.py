# servicios/restaurante.py
# Modulo del servicio Restaurante.
# Es la clase principal del sistema. Gestiona el menu y
# los clientes, procesa pedidos descontando stock y calcula
# la recaudacion total del dia.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase central que administra el menu, los clientes y los pedidos."""

    def __init__(self, nombre, slogan):
        self.nombre = nombre        # nombre del restaurante
        self.slogan = slogan        # frase del negocio
        self.menu = []              # lista de objetos Producto
        self.clientes = []          # lista de objetos Cliente
        self.recaudacion = 0.0      # total recaudado en el dia

    # gestion del menu

    def agregar_producto(self, producto):
        """Incorpora un producto al menu."""
        self.menu.append(producto)

    def mostrar_menu(self):
        """Imprime el menu completo del restaurante."""
        print("\nMenu de " + self.nombre)
        print("-" * 60)
        if not self.menu:
            print("El menu esta vacio.")
        for p in self.menu:
            print("  " + str(p))
        print("-" * 60)

    def buscar_producto(self, codigo):
        """Devuelve el producto con ese codigo, o None si no existe."""
        for p in self.menu:
            if p.codigo == codigo:
                return p
        return None

    # gestion de clientes

    def registrar_cliente(self, cliente):
        """Agrega un cliente al sistema."""
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        """Imprime la lista de clientes registrados."""
        print("\nClientes en " + self.nombre)
        print("-" * 60)
        if not self.clientes:
            print("No hay clientes registrados.")
        for c in self.clientes:
            print("  " + str(c))
        print("-" * 60)

    def buscar_cliente(self, cedula):
        """Devuelve el cliente con esa cedula, o None si no existe."""
        for c in self.clientes:
            if c.cedula == cedula:
                return c
        return None

    # procesamiento de pedidos

    def procesar_pedido(self, cedula, codigo_producto):
        """Registra el pedido de un cliente y descuenta stock."""
        cliente = self.buscar_cliente(cedula)
        producto = self.buscar_producto(codigo_producto)

        if cliente is None:
            print("Cliente no encontrado.")
            return
        if producto is None or not producto.esta_disponible():
            print("El producto no esta disponible.")
            return

        cliente.agregar_plato(producto.nombre, producto.precio)
        producto.reducir_stock()
        self.recaudacion += producto.precio

    def resumen_dia(self):
        """Muestra un resumen de lo que ocurrio en el dia."""
        agotados = sum(1 for p in self.menu if not p.esta_disponible())
        print("\nResumen del dia - " + self.nombre)
        print("  Slogan         : " + self.slogan)
        print("  Productos en menu  : " + str(len(self.menu)) +
              " (" + str(agotados) + " agotados)")
        print("  Clientes atendidos : " + str(len(self.clientes)))
        print("  Recaudacion total  : $" + str(round(self.recaudacion, 2)))

    def __str__(self):
        return self.nombre + " - " + self.slogan
