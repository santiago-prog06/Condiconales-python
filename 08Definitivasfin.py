nt = float(input("Ingrese su nota definitva"))

if nt < 3.0:
    print("Insuficiente")
else:
    if nt <= 3.5:
        print("Aceptable")
    else:
        if nt <= 4.0:
            print("Sobresaliente")
        else:
            if nt <= 5.0:
                print("Excelente")
            else:
                print("Nota Invalida")