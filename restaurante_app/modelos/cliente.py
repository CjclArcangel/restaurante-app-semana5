# modelos/cliente.py
# Modulo del modelo Cliente.
# Representa a una persona que consume en el restaurante.
# Registra sus datos y lleva un historial de los platos
# que pidio junto con el total acumulado a pagar.


class Cliente:
    """Representa a un cliente que consume en el restaurante."""

    def __init__(self, cedula, nombre, correo):
        self.cedula = cedula        # cedula de identidad
        self.nombre = nombre        # nombre completo
        self.correo = correo        # correo electronico
        self.historial = []         # nombres de platos pedidos
        self.total = 0.0            # monto total acumulado

    def agregar_plato(self, nombre_plato, precio):
        """Agrega un plato al historial y suma su precio al total."""
        self.historial.append(nombre_plato)
        self.total += precio

    def ver_historial(self):
        """Imprime los platos pedidos por el cliente."""
        if not self.historial:
            print("  " + self.nombre + " no ha pedido nada aun.")
            return
        print("  Pedidos de " + self.nombre + ":")
        for plato in self.historial:
            print("    - " + plato)
        print("  Total: $" + str(round(self.total, 2)))

    def actualizar_correo(self, nuevo_correo):
        """Actualiza el correo del cliente."""
        self.correo = nuevo_correo

    def __str__(self):
        return (f"{self.cedula} | {self.nombre} | {self.correo} "
                f"| platos pedidos: {len(self.historial)} "
                f"| total: ${self.total:.2f}")
