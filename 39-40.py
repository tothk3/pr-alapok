szamok_lista = [3,21,7,63,9,27]



def min_max(munka_lsita):

    min = munka_lsita[0]
    max = munka_lsita[0]

    for szam in munka_lsita:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f"Legnagyobb szam:{max}")
    print(f"Legkissebbbbbb szam:{min}")



print(min(szamok_lista))
print(max(szamok_lista))


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#öszegzés tétele

öszeg = 0

"""for reszösszeg in szamok_lista:
    öszeg = öszeg + reszösszeg
print(öszeg)
"""
#a lista elemeinek átlag számmitás



def átlagszámitas():
    átlag = None
    öszeg = 0
    for reszösszeg in szamok_lista:
        öszeg = öszeg + reszösszeg

    átlag =  öszeg // len(szamok_lista)

    print(átlag)

átlagszámitas()



