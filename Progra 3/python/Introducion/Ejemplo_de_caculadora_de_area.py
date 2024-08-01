def Área_del_triángulo ():
    b = float(input("Ingrese la lomgitud de la base: "))
    h = float(input("Ingrese la longitud de la altura: "))
    área_triángulo = (b * h)/2
    print("El área del triángulo es: ", área_triángulo)
    
def Área_del_cuadrado ():
    b = float(input("Ingrese la longitud de uno de los lados: "))
    área_cuadrado = 1 ** 2
    print("El área del cuadrado es " , área_cuadrado)
    
    
    op = 1
    
    while op != 3: #Se ejecuta mientras op sea diferente de 3
        print("1.Área del triángulo\n2.Área del cuadrado\n3.Salir")
        op = int(input("Ingresa ima opción "))
        
        if op == 1:
            Área_del_triángulo()
        elif op == 2:
            Área_del_cuadrado
        elif op == 3:
            print("Salio...")
        else:
            print("Ingrese una opción valida")
            
def Área_del_rectángulo ():
    b = float(input("Ingrese la lomgitud de la base: "))
    h = float(input("Ingrese la longitud de la altura: "))
    área_rectángulo = (b * h)/2
    print("El área del triángulo es: ", área_rectángulo)
    
    
def Área_del_rombo ():
    d1 = float(input("Ingrese la longitud de la diagonal mayor: "))
    d2 = float(input("Ingrese la longitud de la diagonal menor: "))
    área_rombo = d1 * d2
    print("El área del cuadrado es " , área_rombo)
    
def Área_del_círculo():
    r = float(input("Ingrese la longitud del radio del círculo: "))
    área_círculo = r * 3.1416
    print("El área del círculo es: ", área_círculo)
    
def Área_del_pentágono():
    l = float(input("Ingrese la longitud del lado: "))
    a = float(input("Ingresa la longitud del apotema: "))
    p = 5 * l
    área_pentagono = (a * p) / 2
    print("El área del pentagono es: ", área_pentagono)
        
    
    op = 1
    
    while op != 5: #Se ejecuta mientras op sea diferente de 3
        print("1.Área del triángulo\n2.Área del cuadrado\n7.Salir")
        op = int(input("Ingresa ima opción "))
        
        if op == 1:
            Área_del_rectángulo()
        elif op == 2:
            Área_del_rombo()
        elif op == 3:
            Área_del_círculo()
        elif op == 4:
            Área_del_pentágono()
        elif op == 5:
            print("Salio...")
        else:
            print("Ingrese una opción valida")