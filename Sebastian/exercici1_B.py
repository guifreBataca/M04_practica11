def ejer1():
    a = input("Digite el primer número: ")
    b = input("Digite el segundo número: ")
    #Ver a es mayor, menor o igual
    if(a > b):
        print("{a} es mayor".format(a=a))
    elif(a < b):
        print("{b} es mayor".format(b=b))
    else:
        print("{a} y {b} son iguales".format(a=a,b=b))
