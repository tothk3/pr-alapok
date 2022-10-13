import math

szam = input("irja be egy szamot  ")
szam1 = input("na meg egyet ")
szam = int(szam)
szam1 = int(szam1)
a = szam - szam1
b = abs(a)

if szam == szam1:
    print(f"Az első szam {szam} egyenlő a masodikal {szam1}")
    

elif szam < szam1: 
    print("2 szam nem egyezik")
    print("A külömbség", b , "a", szam, "kisseb mint ",szam1)
  
else:
    print("2 szam nem egyezik")
    print("A külömbség", b , "a", szam1, "kisseb mint ",szam)
    
quit()