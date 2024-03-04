from test1 import MyException
def factoriel(a):
    if a < 0:
        raise ArithmeticError("mon message d'error")
    if a == 0:
        return 1
    return a * factoriel(a - 1)


if __name__ == '__main__':

    """
    birthyear = input("Annees de naissances")
    try:
        print("tu as", 2024 - int(birthyear), "ans")
    except:
        print("Errreur , veuillez entrer un nombre valide")
    print("Fin du programme")
    """
    """
    try:
        a = int(input("Donner un nombre 1 :"))
        b = int(input("Donner un nombre 2 :"))
        print("le resultat est ", a/b)
    except Exception as d:
        print(type(d))
        print(d)
    print("Fin du programme")
    """
    try:
        a = int(input("Entrez un nombre :" ))
        print(factoriel(a))
    except MyException as e:
        print(type(e)) 
    print("la suite ici")
