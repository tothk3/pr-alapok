napi_max = [14,17,21,15,16,13,8,11,12,14,16,16,14,15,13,14,16,16,14,12,12,10,11,13,15,17,19,17,19,20]
napi_min = [8,8,9,6,7,1,0,2,3,5,4,4,3,5,4,6,8,6,4,2,1,-1,-1,1,3,5,7,5,7,9]



def napimindb (napi_min_fv):
    darab = 0
    for szam in napi_min_fv:
        darab = darab + 1
    return darab



print(napimindb(napi_min))

def napimaxdb (napi_max_fv):
    darab = 0
    for szam in (napi_max_fv):
        darab = darab + 1
    return darab



print(napimaxdb(napi_max))




def napmaxat (napi_max_fv):
    lista = 0
    for szam in napi_max_fv:
        lista = lista + szam
    lista = lista / len(napi_max_fv)
    return lista
    
    
print(napmaxat(napi_max))

def napmint (napi_min_fv):
    lista = 0
    for szam in napi_min_fv:
        lista = lista + szam
    lista = lista / len(napi_min_fv)
    return lista
    
    
print(napmint(napi_min))



print(f"tejes össz átlag {(napmaxat(napi_max) + napmint(napi_min)) / 2 }")


