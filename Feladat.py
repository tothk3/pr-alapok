"""a = input("Szó")

print(a.upper())"""

"""lista_szov1 = ["fa","alma","szo3"]
lista_szov2 = []

for szo in lista_szov1:
    szo = lista_szov2.append(szo.upper())

print(lista_szov1,lista_szov2)"""


"""lista = ['felhő', 'levél', 'fa']

mas_lista = [szo.upper() for szo in lista if len(szo) > 3]

print(lista)
print(mas_lista)"""


"""lista = ['felhő', 'levél', 'fa']

mas_lista = [szo.swapcase() for szo in lista]

print( lista)
print( mas_lista)
"""

"""tartomany = list(range(-3, 5))

keszlet = [2 * x - 3 for x in tartomany]

print(tartomany)
print(keszlet)
"""
'''
tartomany = list(range(-3, 5))

keszlet = [2 * x - 3 for x in tartomany if x >= 0]

print(tartomany)
print(keszlet)'''

"""szinek = ['fehér', 'fekete', 'barna', 'zöld',
          'kék', 'piros', 'citromsárga', 'narancssárga']

szin = input("Adj meg egy színt!")

i = 0
for index in range(len(szinek)):
    if (szin == szinek[index]):
        print("A(z)", szinek[index],
            "szín megtalálható a listában! A listában szereplő színek:", szinek)
    else:
        i = i + 1

if (i == len(szinek)):
    print("A(z)", szin, "nincs a listában! A listában szereplő színek:", szinek)
"""

"""import random


paletta = ['piros', 'fehér', 'lila']

szin = input('Szín: ')

print('A', szin, 'már' if szin in paletta else 'még nem',
      'szerepel a listában:', ', '.join(paletta))"""


"""paletta = ['piros', 'fehér', 'piros', 'piros', 'lila', 'fehér']

szin = input('Szín: ')

if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat ==
          szin]), '-szor szerepel a listában:', ', '.join(paletta))
else:
    print('A megadott szín nem szerepel a listában')"""


"""paletta = ['piros', 'fehér', 'piros', 'piros', 'lila', 'fehér']

szin = input('Szín: ')

if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat ==
          szin]), '-szor szerepel a listában:', end=' ')
else:
    print('A megadott szín nem szerepel a listában:', end=' ')

paletta.append(szin)

print(', '.join(paletta))
"""
2.


"""lista = [random.randint(1, 3) for _ in range(10)]

print('A lista:', lista)

torlendo = int(input('Törlendő: '))

lista = [szam for szam in lista if szam != torlendo]

print('A lista', torlendo, '-es nélkül:', lista)"""


"""betu_leves = []

while True:
    betu = input('Betű: ')
    if not betu:
        break

    if betu.lower() in betu_leves or betu.upper() in betu_leves:
        print('Ezt a betűt már rögzítettem')
    else:
        betu_leves.append(betu)
        betu_leves.sort()

    print('Rögzített betűk:', betu_leves)
"""
