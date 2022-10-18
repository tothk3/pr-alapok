import random


"""szam = int(input("Kerek egy szamot "))
szam1 = int(input("Kerek egy szamot "))
if szam > szam1:
    print(f"{szam} nagyobb mint {szam1}")
if szam1 > szam:
    print(f"{szam1} nagyobb mint {szam}")
if szam1 == szam:
    print(f"{szam} meg egyezik {szam1}")
"""

"""szam = int(input("Kerek egy szamot "))
szam1 = int(input("Kerek egy szamot "))
if szam > szam1:
    print(f"{szam} nagyobb mint {szam1}")
elif szam1 > szam:
    print(f"{szam1} nagyobb mint {szam}")
elif szam1 == szam:
    print(f"{szam} meg egyezik {szam1}")"""


"""szam = int(input("Kerek egy szamot "))
szam1 = int(input("Kerek egy szamot "))
if szam > szam1:
    print(f"{szam} nagyobb mint {szam1}")
elif szam1 > szam:
    print(f"{szam1} nagyobb mint {szam}")
else:
    print(f"{szam} meg egyezik {szam1}")"""

"""
x = None
print(x)
print(type(x))

if x :
    print("Do you think none is true")
elif x is False:
    print("Do you think none is False")
else:
    print("None is not True, or False, None is just None...")"""


"""jegy = int(input("Osztályzat: "))

if jegy == 1:
    print("elégteln")
elif jegy == 2:
    print("Elégséges")
elif jegy == 3:
    print("Közepes")
elif jegy == 4:
    print("Jó")
else jegy == 5:
    print("Kitünö")
else:
    print("Érvényltel osztályzat")
"""
"""
szam = int(input("szamot agya "))

if szam % 2 == 0:
    print("Páros")
else:
    print("Párátlan")

"""

"""a = random.randint(1, 6)
print('Sugó', a)


while tipp != a:

tipp = input(int("Gondtam egy szamra tippeld meg!: "))

   if tipp == a:
        print("Gart")
        break
    else:
        print("Probald ujra")
        continue"""

x = random.randint(1, 1000)

print(x)


if not(x % 2 == 0) and x <= 500:
    print("A szamod jó (paratlan)")
else:
    print("A szamod nem fele meg")
