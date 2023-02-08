
#Aquesta funció et diu quin dels dos nombres que entres és més gran i quin més petit, per si tenies dubtes.
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


