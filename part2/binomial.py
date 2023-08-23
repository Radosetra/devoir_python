"""
Sujet: 
- fonction : LOI BINOMIALE
Fonction permettant de calculer le resultat d'une experience suivant la loi binomiale une
"""

def factoriel(n):
    return n * int(factoriel(n-1)) if n>1 else 1

def combinaison(n,p):
    return factoriel(n)/(factoriel(p) * factoriel(n-p))

def binomiale(n,nbrS,probS):
    if nbrS < 0 :
        return 0
    return combinaison(n,nbrS)*((probS)**nbrS)*((1-probS)**(n-nbrS)) + binomiale(n,nbrS-1,probS)


