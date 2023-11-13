from principal import *
from configuracion import *
import random
import math
from extras import *

# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    archivo_lectura = open("productos.txt", "r")  # Abrimos el archivo en modo lectura
    lista_productos = []  # Inicializamos una lista para almacenar los productos

    # Iteramos sobre cada línea en el archivo
    for linea in archivo_lectura:
        producto_cadena = linea.strip().split(',')  # Eliminamos espacios en blanco y dividimos la línea en partes usando ',' como delimitador
        producto_final = [producto_cadena[0], int(producto_cadena[1]), int(producto_cadena[2])]  # Creamos una lista con el nombre del producto y sus dos valores numéricos
        lista_productos.append(producto_final)  # Agregamos la lista del producto a la lista principal

    archivo_lectura.close()  # Cerramos el archivo después de leer todas las líneas
    return lista_productos  # Retornamos la lista de productos obtenida desde el archivo



#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
    indice_aleatorio = random.randint(0, len(lista_productos) - 1)# Generamos un índice aleatorio para seleccionar un producto de la lista
    producto_original = lista_productos[indice_aleatorio]# Seleccionamos el producto aleatorio de la lista
    nuevo_producto = []# Inicializamos una nueva lista para almacenar el producto modificado

    # Iteramos sobre cada índice en el rango de la longitud del producto original
    for indice in range(len(producto_original)):
        if indice == 1:# Si estamos en el segundo elemento (posición 1), añadimos una etiqueta aleatoria
            etiqueta = random.choice(["(premium)", "(economico)"])
            nuevo_producto.append(etiqueta)
        else: # Si no estamos en el segundo elemento, simplemente copiamos el elemento original
            nuevo_producto.append(producto_original[indice])

    return nuevo_producto  # Retornamos el producto modificado
    # producto = ["Silla de oficina", "(premium)", 4391]

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    while True:
        producto = buscar_producto(lista_productos)  # Utilizamos la función buscar_producto para obtener un producto aleatorio
        # Buscamos productos con valor similar, deben ser al menos 2 adicionales
        if esUnPrecioValido(producto[2], lista_productos, margen):
            return producto


#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    count = 0  # Inicializamos el contador a cero

    for producto in lista_productos:
        # Controlamos que el precio del producto esté dentro del rango especificado por el margen
        if abs(producto[2] - precio) <= margen:  # Comparamos la diferencia absoluta entre los precios
            count = count + 1  # Incrementamos el contador si el precio está dentro del margen
        if count >= 3:
            return True  # Si encontramos al menos tres precios dentro del margen, retornamos True

    return False  # Si no encontramos tres precios dentro del margen, retornamos False

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):
    if(abs(producto_principal[2] - producto_candidato[2]) <= margen):
        return 1
    else:
        return 0

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = [producto]# Inicializamos la lista con el producto principal
    dos_garantizado = 0 # Contador para garantizar al menos 2 productos con el mismo precio
    
    while len(productos_seleccionados) < 6: # Mientras no hayamos alcanzado la cantidad deseada de productos
        producto_random = buscar_producto(lista_productos)# Obtener un nuevo producto aleatorio

        # Verificar si el nuevo producto tiene un precio similar y aún no garantizamos 2 productos
        if abs(producto[2] - producto_random[2]) <= margen and dos_garantizado <= 2:
            dos_garantizado = dos_garantizado + 1  # Incrementamos el contador
            productos_seleccionados.append(producto_random)
        elif dos_garantizado > 2: # Si ya garantizamos 2 productos, simplemente agregamos el nuevo producto
            productos_seleccionados.append(producto_random)

    return productos_seleccionados
    #productos_seleccionados =   [["Monitor de computadora", "(premium)", 2870],
    #        ["Silla de oficina", "(economico)", 3174],
    #        ["Lavadora", "(premium)", 4197],
    #        ["Refrigerador", "(premium)", 4533],
    #        ["Laptop", "(economico)", 4650],
    #        ["Cafetera", "(economico)", 2358]]