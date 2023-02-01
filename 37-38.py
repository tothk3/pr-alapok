#széső érték meghat

listaaa = [1,2,3,4,5,6,7,8,9]


def szelsoertek_10c(munka_lsita):

    min = munka_lsita[0]
    max = munka_lsita[0]

    for szam in munka_lsita:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f"Legnagyobb szam:{max}")
    print(f"Legkissebbbbbb szam:{min}")

szelsoertek_10c(listaaa)