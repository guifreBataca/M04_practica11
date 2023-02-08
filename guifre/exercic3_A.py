import random
#Aquesta funcio et fa adivinar un numero
def numeroSort():
    aleatori = random.randrange(1, 101)
    print("Escriu un numero del 1 al 100:\n")

    trobat = False
    superior = 100
    inferior = 0
    while not trobat:
        numero = int(input())


        if numero == aleatori:
            trobat = True
        if numero < aleatori:
            inferior = numero
            print("El numero que busques està entre {inferior} i {superior}\n".format(inferior=inferior, superior=superior))
        if numero > aleatori:
            superior = numero

            print("El numero que busques està entre {inferior} i {superior}\n".format(inferior=inferior, superior=superior))


