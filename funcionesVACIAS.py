from principal import *
from configuracion import *
import random
import math
from extras import *

# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    file = open("productos.txt", "r")
    list = []
    for element in file:
        line = element.strip().split(',')
        producto = [line[0], int(line[1]), int(line[2])]
        list.append(producto)
    file.close
    return list


#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
    numeroAleatorio = random.randint(0, len(lista_productos) - 1)
    producto = lista_productos[numeroAleatorio]
    newProduct = []
    for element in range(len(producto)):
        if(element == 1):
            numeroAleatorio = random.randint(0, 1)
            if(numeroAleatorio == 1):
                newProduct.append("(premium)")
            else:
                newProduct.append( "(economico)")
        else:
            newProduct.append(producto[element])
    # producto = ["Silla de oficina", "(premium)", 4391]
    return newProduct

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    while(True):
        producto = buscar_producto(lista_productos)
        ##buscar productos con valor similar debe tener por lo menos 2
        if (esUnPrecioValido(producto[2],lista_productos,margen)):
            return producto


#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    count = 0
    for producto in lista_productos:
        #controlar que elemento[2] este dentro del rango del precio
        if (abs(producto[2] - precio) <= margen):
            count = count +1
        if(count >=3 ):
            return True
    else:
        return False

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
    productos_seleccionados = []
    productos_seleccionados.append(producto)
    #se agrega el producto que ya viene o no? por que se ve que lo maneja por el fondo
    #hacer un random para que no se siempre la misma lista
    #falta controlar que minimo 2 esten garantizado
    for i in range(5):
        productos_seleccionados.append(dameProducto(lista_productos, margen))
        
    #productos_seleccionados =   [["Monitor de computadora", "(premium)", 2870],
    #        ["Silla de oficina", "(economico)", 3174],
    #        ["Lavadora", "(premium)", 4197],
    #        ["Refrigerador", "(premium)", 4533],
    #        ["Laptop", "(economico)", 4650],
    #        ["Cafetera", "(economico)", 2358]]
    return productos_seleccionados


