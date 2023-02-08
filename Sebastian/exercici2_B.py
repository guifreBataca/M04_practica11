def ejer2():
    #Ver si a es par o impar
    a = input("Digite un número: ")
    a = int(a)
    if(a % 2 == 0):
        print("{a} es par".format(a=a))
    else:
        print("{a} es impar".format(a=a))

