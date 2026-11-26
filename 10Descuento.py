va = float(input("Ingrese el valor del articulo: "))

if va > 150000:
    vd = va * 0.05
    cf = va - vd
    print("El valor de descuento es: ", vd)
    print("El articulo costaria: ", cf)
else:
    print("No tienes ningun descuento")

