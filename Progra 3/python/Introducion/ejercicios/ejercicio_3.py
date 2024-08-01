def pertenece_al_intervalo(numero):
    if -3 <= numero <= 27:
        return True
    else:
        return False

# Número a verificar
numero = 10

if pertenece_al_intervalo(numero):
    print(f"El número {numero} pertenece al intervalo de -3 a 27.")
else:
    print(f"El número {numero} no pertenece al intervalo de -3 a 27.")