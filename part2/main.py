from math import sqrt

"""
Sujet:
- Ecrire une fonction qui retourne l'ecart type et la moyenne d'une suite de valeur
"""

def avgAndEcart(arr):
    cumsum = 0
    cumEcart = 0
    ecart = 0
    for e in arr:
        cumsum += e
    l = len(arr)
    avg = float(cumsum / l)
    for e in arr:
        cumEcart += (e - avg)**2
    ecart = sqrt(cumEcart / l)
    return avg, ecart

myArr = [5,10,5,10]
myAvg, myEcart = avgAndEcart(myArr)

print("Average: ",myAvg,"Ecart",myEcart)