elso_szam = int(input("Kérek egy számot 1-100ig:"))
masodik_szam = int(input("Kérek egy másik számot 1-100ig:"))

if elso_szam or masodik_szam > 100:
    print("asas")
else:
    print(elso_szam + masodik_szam)
    print(elso_szam * masodik_szam)
