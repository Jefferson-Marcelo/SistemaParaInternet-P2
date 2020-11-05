lista = [1,2,3,4,5]


def busca(li,dado):
    for i in range(len(li)):
        if li[i] == dado:
            return 'encontrado'
    return None
        

print(busca(lista,5))
