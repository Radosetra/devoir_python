print("Resolution equation second degree : ax^2 + bx + c")
a = input("Entre une valieur numerique de a")
b = input("Entre une valieur numerique de b")
c = input("Entre une valieur numerique de c")


# cas 1: a = 0
    # b != 0 && c != 0
if a == 0:
    if (b != 0 and c != 0):
        print("Solution :", -b//c)
    elif (b==0 and c != 0):
        print("Pas de solution dans R")
    elif c == 0 and b != 0:
        print("Solution : 0")
    else:
        print("Solution : R")
elif b == 0:
    if c != 0:
        if (c < 0 and a > 0) or (c > 0 and a < 0):
            s = sqrt(c/a)
            print("Solution:", s)
        else:
            print("Pas de solution dans R")
    elif c == 0:
        print("Solution : 0")
elif a!=0 and b!=0:
    delta = b**2 - 4*a*c
    if delta>0:
        print("Admet deux solution unique\nx1=",(-b -sqrt(delta))/2*a,"x2=",(-b +sqrt(delta))/2*a)
    elif delta == 0:
        print("Admet une solution double x1=x2=",(-b/2*a))
    else:
        print("Pas de solution dans R")





