# main.py
# Punto de arranque del programa.
# Crea los objetos del sistema, los registra en el servicio
# principal y ejecuta los metodos para demostrar el
# funcionamiento del restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # crear el servicio principal
    restaurante = Restaurante(
        "Sabores del Puerto",
        "Cocina fresca del Pacifico"
    )
    print(restaurante)

    # crear productos con stock del dia
    p1 = Producto("E01", "Ceviche de concha",      "Entrada",  5.50, 10)
    p2 = Producto("E02", "Empanadas de viento",    "Entrada",  2.00,  8)
    p3 = Producto("F01", "Seco de carne",          "Fuerte",   6.50,  5)
    p4 = Producto("F02", "Corvina al vapor",       "Fuerte",   8.00,  3)
    p5 = Producto("B01", "Agua de jamaica",        "Bebida",   1.50, 15)
    p6 = Producto("P01", "Mousse de maracuya",     "Postre",   3.00,  4)

    # agregar productos al menu
    for producto in [p1, p2, p3, p4, p5, p6]:
        restaurante.agregar_producto(producto)

    # reponer stock de un producto
    p2.reponer_stock(5)

    # mostrar el menu al inicio del dia
    restaurante.mostrar_menu()

    # crear clientes
    c1 = Cliente("0921001122", "Carlos Javier Cedeno Leiton", "carlos@correo.com")
    c2 = Cliente("0922003344", "Mariela Suarez",              "mariela@correo.com")
    c3 = Cliente("0923005566", "Hector Bone",                 "hector@correo.com")

    # registrar clientes en el sistema
    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)
    restaurante.registrar_cliente(c3)

    # procesar pedidos
    restaurante.procesar_pedido("0921001122", "E01")
    restaurante.procesar_pedido("0921001122", "F02")
    restaurante.procesar_pedido("0921001122", "B01")

    restaurante.procesar_pedido("0922003344", "E02")
    restaurante.procesar_pedido("0922003344", "F01")
    restaurante.procesar_pedido("0922003344", "P01")

    restaurante.procesar_pedido("0923005566", "F02")
    restaurante.procesar_pedido("0923005566", "B01")

    # actualizar correo de un cliente
    c2.actualizar_correo("mariela.suarez@correo.com")

    # mostrar historial de pedidos de cada cliente
    print("\nHistorial de pedidos:")
    c1.ver_historial()
    c2.ver_historial()
    c3.ver_historial()

    # mostrar clientes con resumen
    restaurante.mostrar_clientes()

    # buscar un cliente por cedula
    print("\nBusqueda por cedula 0922003344:")
    encontrado = restaurante.buscar_cliente("0922003344")
    if encontrado:
        print("  " + str(encontrado))

    # mostrar menu con stock actualizado
    print("\nEstado del menu tras los pedidos:")
    restaurante.mostrar_menu()

    # resumen del dia
    restaurante.resumen_dia()


if __name__ == "__main__":
    main()
