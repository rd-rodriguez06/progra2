def Calcular_valor ():
    # Solocitar dos numeros enteros al usuario 
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("ingrese el suegundo nuemero entero: "))
    
    # Comprueba si ambos numeros on pares.
    if num1 % 2 == 0 and num2 % 2 == 0:
        # multiplicar ambos numeros 
        resultadofinal = num1 * num2 
    else: 
        # Suma de los numeros y multiplicacion por 10.
        resultadofinal =  (num2 + num2) * 10 
    
    return resultadofinal
resultadofinal = Calcular_valor()
print(f"El valor final es: {resultadofinal}")