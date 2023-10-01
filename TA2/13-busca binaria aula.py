def executar_buscar_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        print(f'Valor minimo = {minimo}, Valor maximo = {maximo}')
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2

        # Verifica se o valor procurado está a esquerda
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return f"Valor encontrado no index {meio}" # Se o valor for encontrado
        
    
    return False # Se o valor nao for encontrado

lista_numeros:list = [1, 2, 3, 4, 5, 6, 7, 11, 12, 15, 23, 25, 35, 36, 37, 41, 42, 44, 46, 47, 51, 52, 53, 55]


print(executar_buscar_binaria(lista_numeros, 11))