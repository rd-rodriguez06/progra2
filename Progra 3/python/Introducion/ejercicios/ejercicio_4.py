# Solicitar 3 numeros enteros
num1 = float(input("Introduzca el primer numero: "))
num2 = float(input("Introduzca el segundo numero: "))
num3 = float(input("introduzca el tercer numero: "))

# Determina cual es el mayor; el menor, y el intermedio
if (num1 >= num2) and (num1 >= num3):
    mayor = num1
    if num2 >= num3 :
        intermedio = num2
        menor = 3
    else: 
        intermedio = num3
        menor = num2
elif (num2 >= num1) and (num2 >= num3):
    mayor = num2
    if num1 >= num3:
        intermedio = num1
        menor = num3 
    else:
         intermedio = num3
         menor = num1
else:
    mayor = num3
    if num1 >= num2:
        intermedio = num1
        menor = num2
    else:
        intermedio = num2
        menor = num1

# Resulatados 
print("El numero mayor es:", mayor)
print("El numero intermedio es:", intermedio)
print("El numero menor", menor)
