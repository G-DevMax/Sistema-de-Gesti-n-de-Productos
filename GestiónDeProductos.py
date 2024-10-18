productos = []

def añadir_producto():
    # Lógica para añadir un producto

    while True:
        try:
            print("Ingrese el nombre del producto")
            nombreProducto = str(input())
            break
        except ValueError:
            print("Error: El nombre del producto debe ser una cadena de texto")

    while True:
        try:
            print("Ingresar el precio del producto")
            precioProducto = float(input())
            break
        except ValueError:
            print("Error: El precio del producto debe ser un número")
        
    while True:
        try:
            print("Ingrese la cantidad del producto")
            cantidadProducto = int(input())
            break
        except ValueError:
            print("Error: La cantidad del producto debe ser un número entero")

    productos.append({"nombre_Producto" : nombreProducto, "precio" : precioProducto, "cantidad" : cantidadProducto})

    print("Producto Agregado")
    pass

def ver_productos():
    # Lógica para ver todos los productos
    print("Lista de Productos")
    productos_file = open("productos.txt", "r")
    print(productos_file.read())
    productos_file.close()
    pass

def actualizar_producto():
    # Lógica para actualizar un producto
    print("Ingrese el nombre del producto a actualizar")
    productoUpdate = str(input())
    for producto in productos:
        if producto["nombre_Producto"] == productoUpdate:
            print("Ingrese el nuevo precio del producto")
            producto["precio"] = float(input())
            print("Ingrese la nueva cantidad disponible del producto")
            producto["cantidad"] = int(input())
            print("Producto Actualizado")
        else:
            print("Producto no encontrado")
    pass

def eliminar_producto():
    # Lógica para eliminar un producto
    print("Ingrese el nombre del producto a eliminar")
    nombreProductoE = input()
    encontrado = False  # variable para confirmar si se encontro el producto

    for producto in productos[:]:  # con[:] se itera sobre una copia
        if producto["nombre_Producto"] == nombreProductoE:
            productos.remove(producto) 
            print(f"Producto Eliminado: {producto}")  # Mostrar información del producto eliminado, para confirmar si se elimino todos los datos
            encontrado = True # la variable pasa a true para que el "if not" no muestre el mensaje 
            break 

    if not encontrado: # si no se encuentra el producto, se imprime el mensaje
        print("Producto no encontrado")


def guardar_datos():
    # Lógica para guardar los datos en un archivo
    try:
        with open("productos.txt", 'w') as file:
            for producto in productos:
                file.write(f"Nombre: {producto['nombre_Producto']}\n")
                file.write(f"Precio: {producto['precio']}\n")
                file.write(f"Cantidad disponible: {producto['cantidad']}\n\n")
        print(f"Productos guardados correctamente en productos.txt")
    except Exception as e:
        print(f"Error al guardar productos: {e}")
    
    pass

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open("productos.txt", 'r') as f:
            contenido = f.read().strip().split('\n\n')  # Leer el contenido y separar por productos
            for producto_str in contenido:
                lineas = producto_str.strip().split('\n')
                if len(lineas) >= 3:  # Asegurarse de que hay suficientes líneas
                    nombre = lineas[0].split(': ')[1]
                    precio = float(lineas[1].split(': ')[1])
                    cantidad = int(lineas[2].split(': ')[1])
                    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print(f"Productos cargados correctamente desde productos.txt")
    except Exception as e:
        print(f"Error al cargar productos: {e}")
    pass

def menu():
    while True:
        cargar_datos()
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()