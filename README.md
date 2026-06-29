# Sistema de Gestion de Restaurante

Estudiante: Carlos Javier Cedeño Leiton
Asignatura: Programacion Orientada a Objetos
Semana: 4

---

## Descripcion del sistema

El proyecto es un sistema basico de gestion para el restaurante "Sabores del
Puerto", desarrollado en Python aplicando Programacion Orientada a Objetos.

El sistema permite registrar productos en el menu con un stock disponible para
el dia, procesar los pedidos de cada cliente descontando unidades del stock y
acumulando el monto en su historial, buscar productos y clientes por su
identificador, reponer stock de un producto, y al final del dia obtener un
resumen con la recaudacion total y el estado del menu.

La idea central no es construir una aplicacion grande sino demostrar como
separar responsabilidades entre archivos usando modulos, como comunicarlos
con importaciones y como aplicar los conceptos fundamentales de la POO.

---

## Estructura del proyecto

```
restaurante_app/
    modelos/
        __init__.py
        producto.py      - clase Producto
        cliente.py       - clase Cliente
    servicios/
        __init__.py
        restaurante.py   - clase Restaurante
    main.py              - punto de arranque del programa
```

### Descripcion de cada archivo

- modelos/producto.py: define la clase Producto, que representa un plato o
  bebida del menu. Tiene atributos de codigo, nombre, categoria, precio y
  stock del dia. Sus metodos permiten reducir o reponer el stock y consultar
  si el producto esta disponible.

- modelos/cliente.py: define la clase Cliente, que representa a una persona
  que consume en el restaurante. Guarda cedula, nombre, correo, un historial
  de platos pedidos y el total acumulado. Permite agregar platos, ver el
  historial y actualizar el correo.

- servicios/restaurante.py: define la clase Restaurante, que es el nucleo del
  sistema. Administra el menu y los clientes, procesa pedidos conectando ambos
  modelos, lleva la recaudacion del dia y muestra el resumen final.

- main.py: es el punto de arranque. Crea los objetos, los registra en el
  servicio y ejecuta los metodos para mostrar el funcionamiento completo.

---

## Conceptos de POO aplicados

- Clases: Producto, Cliente y Restaurante.
- Constructor __init__: inicializa los atributos de cada objeto al momento
  de crearlo.
- Atributos: definidos segun el contexto real del negocio (stock, historial
  de platos, recaudacion, slogan del restaurante, etc.).
- Metodos: gestionan la informacion y las operaciones de cada clase.
- Metodo especial __str__: implementado en las tres clases para representar
  cada objeto como texto al imprimirlo en consola.
- Importaciones entre archivos: main.py importa desde modelos y servicios;
  restaurante.py importa los modelos Producto y Cliente.

---

## Como ejecutar el programa

Desde la carpeta raiz del repositorio:

```
python restaurante_app/main.py
```

El programa muestra el menu al inicio del dia, el historial de pedidos de
cada cliente, la lista de clientes con sus totales, el resultado de una
busqueda, el estado del menu con el stock actualizado y el resumen del dia.

---

## Reflexion sobre la organizacion modular

Organizar el codigo en modulos separados, donde cada archivo tiene una
responsabilidad clara, hace que el sistema sea mas facil de entender y de
mantener. En este proyecto los modelos representan las entidades del problema
(un plato, un cliente), el servicio concentra la logica del negocio (como
procesar un pedido o calcular la recaudacion) y main.py solo se encarga de
arrancar el programa.

Esa division permite que cada parte evolucione de manera independiente. Si se
necesita cambiar como se maneja el stock, se modifica solo producto.py sin
afectar al resto. Eso reduce errores y hace el codigo mas facil de escalar,
que son ventajas concretas de programar con Programacion Orientada a Objetos
y con una buena organizacion modular.
