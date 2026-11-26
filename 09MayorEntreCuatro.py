n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))
n4 = float(input("Ingrese el cuarto numero: "))
if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            print("El numero mayor es: ", n1)
        else:
            print("El numero mayor es: ", n4)
    else:
        if n3 > n4:
            print("El numero mayor es: ", n3)
        else:
            print("El numero mayor es: ", n4)
else: 
    if n2 > n3:
        if n2 > n4:
            print("El numero mayor es: ", n2)
        else:
            print("El numero mayor es: ", n4)
    else:
        if n3 > n4:
            print("El numero mayor es: ", n3)
        else:
            print("El numero mayor es: ", n4)
