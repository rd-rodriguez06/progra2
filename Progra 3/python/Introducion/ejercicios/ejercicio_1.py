def calcular_precio_final (num_productos):
#  Definir los precios y descuentos para cada producto.
 precios = {
    2: 0.90, # 10% descuento 
    3: 0.88, # 12% descuento 
    4: 0.85, # 15% descuento 
}

# Calcular el preciuo final en funcion del numero de productos.
if num_productos < 2:
    PrecioFianl = num_productos * 100
else:
    for thershold, descuento in precios.items ():
        if num_productos >= thershold:
           PrecioFianl = num_productos * 100 * descuento
        break
    
return PrecioFianl

# Ejemplo 
num_productos = int(input("ingrse la cantidad de productos comprados: "))
PrecioFianl = Calculaudar_precio_final(num_productos)
print(f"El valor final de la compra es: ${PrecioFianl:.2f}")
