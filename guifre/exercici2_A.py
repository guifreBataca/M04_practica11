
def salutacions():
    noms = ["Mar", "Mariona", "Marcel", "Marti", "Guifre"]
    print(noms)
    nom = input("Escriu un d'aquests noms\n")
    salutacio = "Bon dia {nom}, sóc una inteligencia artificial, en què puc servir-te?"
    if(noms.count(nom) == 0):
        print("No ha introduit un nom valid.")
    else:
        print(salutacio.format(nom=nom))
