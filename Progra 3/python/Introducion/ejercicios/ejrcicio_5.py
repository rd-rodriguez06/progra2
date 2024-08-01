# ingreso de los 3 numeros
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingrese el segundo numero:" ))
num3 = float (input("Ingrese el tercer numero: "))

# Comprueba si los nuemnros son iguales 
if num1 == num2 and num2 == num3: 
    print("Los tres nuemro son iguales: ")
    
# # Comprueba si los tres numeros non igualses 
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Hay dos numero iguales.")

# Si alguna de las condiciones anteriores es verdadera, entonces los numeros son diferentes.
else:
    print("Los tres numeros son diferentes.")
    