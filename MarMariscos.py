import os

# Función para limpiar la pantalla de la terminal
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Función para agregar insumos al inventario (5 máximo)
def incluir_insumo(insumos):
    """
    Permite al usuario agregar insumos al diccionario insumos.
    Se puede guardar un máximo de 5 insumos y cada uno puede tener hasta 5 unidades.
    """
    limpiar_pantalla()
    max_insumos = 5
    while len(insumos) < max_insumos:
        nombre = input("Ingrese el nombre del insumo: ")
        codigo = str(len(insumos)).zfill(2)  # Código de 2 dígitos, ej. '01'
        cantidad = int(input(f"\n¿Cuántos '{nombre}' desea guardar? (máximo 5): "))

        if cantidad > 5:
            print("\nLa cantidad máxima permitida por insumo es 5.")
            continue

        insumos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"\nInsumo '{nombre}' con código {codigo} guardado correctamente.")

        continuar = input("\n¿Desea guardar otro insumo? (si/no): ").lower()
        if continuar != "si":
            break

# Función para mostrar el menú de platillos de comida
def consultar_platos():
    """
    Muestra el menú de platillos con precios y los que tienen descuento.
    """
    platos = [
        ("Pulpo a la gallega", 8000),
        ("Langosta al ajillo", 7500),
        ("Pescado entero frito", 5500),
        ("Coctel de mariscos", 10500),
        ("Sopa de mariscos", 7000),
        ("Arroz con mariscos", 5000),
        ("Tacos de pescado", 4500)
    ]
    
    con_descuento = ["Coctel de mariscos", "Sopa de mariscos", "Arroz con mariscos", "Tacos de pescado"]

    print("\n--- Menú de Platos ---")
    for i, (plato, precio) in enumerate(platos):
        descuento_texto = " (15% de descuento)" if plato in con_descuento else ""
        print(f"{i + 1}. {plato} - {precio} colones{descuento_texto}")


# Función para mostrar las bebidas disponibles
def consultar_bebidas():
    """
    Muestra la lista de bebidas con un precio fijo de 2000 colones cada una.
    """
    bebidas = [
        "Piña colada",
        "Mojito",
        "Cerveza artesanal",
        "Whisky con hielo",
        "Ron con Coca-Cola",
        "Margarita",
        "Gaseosa de naranja",
        "Agua tónica",
        "Refresco natural de tamarindo",
        "Limonada con hierbabuena"
    ]

    print("\n--- Menú de Bebidas (2000 colones cada una) ---")
    for i, bebida in enumerate(bebidas):
        print(f"{i + 1}. {bebida} - 2000 colones")

# Función para que el usuario seleccione un platillo del menú
def seleccionar_platillo():
    """
    Permite al usuario seleccionar un platillo del menú y calcula si tiene descuento.
    """
    platos = [
        ("Pulpo a la gallega", 8000),
        ("Langosta al ajillo", 7500),
        ("Pescado entero frito", 5500),
        ("Coctel de mariscos", 10500),
        ("Sopa de mariscos", 7000),
        ("Arroz con mariscos", 5000),
        ("Tacos de pescado", 4500)
    ]
    con_descuento = ["Coctel de mariscos", "Sopa de mariscos", "Arroz con mariscos", "Tacos de pescado"]

    consultar_platos()
    try:
        opcion = int(input("\nSeleccione el número del platillo que desea: ")) - 1
        if 0 <= opcion < len(platos):
            platillo, precio = platos[opcion]
            tiene_descuento = platillo in con_descuento
            print(f"\nUsted seleccionó: {platillo} - {precio} colones")
            return platillo, precio, tiene_descuento
        else:
            print("\nOpción inválida.")
    except ValueError:
        print("\nEntrada no válida.")
    return None, 0, False

# Función para que el usuario seleccione una bebida
def seleccionar_bebida():
    """
    Permite al usuario seleccionar una bebida del menú.
    """
    bebidas = [
        "Piña colada",
        "Mojito",
        "Cerveza artesanal",
        "Whisky con hielo",
        "Ron con Coca-Cola",
        "Margarita",
        "Gaseosa de naranja",
        "Agua tónica",
        "Refresco natural de tamarindo",
        "Limonada con hierbabuena"
    ]

    consultar_bebidas()
    try:
        opcion = int(input("\nSeleccione el número de la bebida que desea: ")) - 1
        if 0 <= opcion < len(bebidas):
            bebida = bebidas[opcion]
            print(f"\nUsted seleccionó: {bebida} - 2000 colones")
            return bebida, 2000
        else:
            print("\nOpción inválida.")
    except ValueError:
        print("\nEntrada no válida.")
    return None, 0

# Menú para empleados con opciones de inventario y consulta
def menu_empleados(insumos, platos):
    while True:
        print("\n--- Menú para Empleados ---")
        print("1. Agregar insumo")
        print("2. Ver menú con precios y descuentos")
        print("3. Consultar insumos")
        print("4. Modificar insumo")
        print("5. Borrar insumo")
        print("6. Agregar platillo")
        print("7. Modificar platillo")
        print("8. Borrar platillo")
        print("9. Salir")

        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                incluir_insumo(insumos)
            elif opcion == 2:
                consultar_platos()
            elif opcion == 3:
                print("\nLista de insumos disponibles:")
                for codigo, insumo in insumos.items():
                    print(f"Código {codigo}: {insumo['nombre']} - Cantidad: {insumo['cantidad']}")
            elif opcion == 4:
                modificar_insumo(insumos)
            elif opcion == 5:
                borrar_insumo(insumos)
            elif opcion == 6:
                agregar_platillo(platos)
            elif opcion == 7:
                modificar_platillo(platos)
            elif opcion == 8:
                borrar_platillo(platos)
            elif opcion == 9:
                break
            else:
                print("\nOpción inválida. Intente de nuevo.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
            
# Menú para clientes/usuarios que permite seleccionar platos, bebidas y calcular total
def menu_usuarios():
    """
    clientes que consulten el menú,
    seleccionar platillos y bebidas, y calcular el total a pagar.
    """
    total = 0
    while True:
        print("\n--- Menú para Usuarios ---")
        print("1. Consultar menú con precios y descuentos")
        print("2. Seleccionar platillo")
        print("3. Seleccionar bebida")
        print("4. Total del costo")
        print("5. Salir")

        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                consultar_platos()
            elif opcion == 2:
                platillo, precio, tiene_descuento = seleccionar_platillo()
                if platillo:
                    if tiene_descuento:
                        descuento = precio * 0.15
                        precio -= descuento
                        print(f"\nDescuento aplicado: -{int(descuento)} colones")
                    total += precio
            elif opcion == 3:
                bebida, precio_bebida = seleccionar_bebida()
                if bebida:
                    total += precio_bebida
            elif opcion == 4:
                print(f"\nTotal a pagar: {int(total)} colones")
                print("\nOpciones de pago:")
                print("1. Pagar con tarjeta")
                print("2. Pagar en efectivo")
                input("Seleccione una opción para continuar...")
            elif opcion == 5:
                break
            else:
                print("\nOpción inválida. Intente de nuevo.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

# Menú principal del sistema MarMariscos
def menu():
    """
    Punto de entrada principal Permite al usuario elegir entre
    menú de empleados, menú de usuarios o salir.
    """
    insumos = {}
    while True:
        print("\n--- MarMariscos Sistema ---")
        print("1. Menú de empleados")
        print("2. Menú de usuarios")
        print("3. Salir")
        try:
            seleccion = int(input("\nSeleccione una opción: "))
            if seleccion == 1:
                menu_empleados(insumos)
            elif seleccion == 2:
                menu_usuarios()
            elif seleccion == 3:
                print("\n¡Gracias por usar MarMariscos!")
                break
            else:
                print("\nOpción inválida.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

# Ejecución principal del programa
if __name__ == "__main__":
    menu()

















