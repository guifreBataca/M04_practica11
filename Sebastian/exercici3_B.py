def ejer3():
    a = input("Ponga edad: ")
    b = input("Ponga el salario: ")
    a = int(a)
    b = int(b)
    # Si la persona tiene 18 o mas años y cobra mas de 1200 tendrá que hacer una declaración de hacienda
    if(a >= 18 and b > 1200):
        print("És necessari que facis la declaració d’hisenda, porque tiene {a}, y cobra {b}".format(a=a,b=b))
    else:
        print("Encara no pots fer la declaració, porque tiene {a}, y cobra {b} ".format(a=a,b=b))
ejer3()