
def mesGran():
    num1 = int(input("Escriu un nombre\n"))
    num2 = int(input("Escriu un altre nombre\n"))
    if num1 < num2:
        print("El nombre més gran és {nombre}".format(nombre=num2))
        print("El nombre més petit és {nombre}".format(nombre=num1))
    elif num1 > num2:
        print("El nombre més gran és {nombre}".format(nombre=num1))
        print("El nombre més petit és {nombre}".format(nombre=num2))
    else:
        print("Els dos numeros són iguals")


