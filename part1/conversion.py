chiffreToLetter = ['zero','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix']

val = 1
while val in range(0,11):
    val = int(input("Entrez un chiffre(0-10)\nEntre -1 pour quitter"))
    if val not in range(0,11):
        print("Impossible a convertir")
        break
    else:
        print("Conversion de",val," to",chiffreToLetter[val])

