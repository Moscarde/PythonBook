# Verifica se um numero é menor do que o a lista e ordena, reduz a lista e repete o processo a partir dele

def executar_selection_sort(lista):
    n = len(lista) #5
    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
            lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista


lista = [10, 9, 5, 8, 11, 3]

print(executar_selection_sort(lista))