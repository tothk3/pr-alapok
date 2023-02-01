
napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

osszesen = 0
for ertekesites in napi_ertekesitesek:
      osszesen = osszesen + ertekesites

print("A héten ennyi értékesítés történt: ", osszesen)

# --------------------------------------------------------------------------

print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
      darab = darab + 1
      osszeg = osszeg + erdemjegy
      erdemjegy = int(input('Add meg az következő érdemjegyet: '))

if darab != 0:
      print('A jegyeid átlaga: ', osszeg / darab)
else:
      print('Nem adtál meg egy jegyet sem!')


'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]
for szam in lista:
      if szam < min:
            min = szam
      if szam > max:
            max = szam

print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)  

# -----------------------------------------------------------------------------------

'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]
for szam in lista:
	if szam < min:
		min = szam
	if szam > max:
		max = szam

print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)



'''
lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')


"""
A listát bejárhattuk volna egy for ciklus segítségével is természetesen, de felesleges végighaladnunk az összes elemen. A fenti program amint megtatálja az első olyan elemet, amely megfelel a feltételeknek, befejezi a lista átvizsgálását. Hiszen ha már találtunk egy ilyen elemet, megvan a válasz.
"""


'''
lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
      if lista[index] == 'piros':
            talalat = True
      index = index + 1

if talalat:
      print('Van a listában piros szín, az indexe: ', index-1)
else:
      print('Nincs a listában piros szín.')