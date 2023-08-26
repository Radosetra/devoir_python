from binomial import *

# Test loi binomiale
try:
    nbrTirage = int(input("Nombre de tirage:"))
    nbrSucces = int(input("Nombre de succes:"))
    probaSucces = float(input("Probabilite d'un succes:"))
    print("Resultat : ", binomiale(nbrTirage, nbrSucces, probaSucces))
except e:
    print("Donnee entree incorrecte :" + e)

print("Fin du programme.")