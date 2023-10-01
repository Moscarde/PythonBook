# Necessita que a lista esteja ORDENADA
# Verifica se o elemento no meio da lista é igual a busca, caso seja, encerra a busca
# Caso seja menor ou maior, exclui a parte oposta da lista e verifica o proximo numero no meio do conjunto restante

lista_numeros:list = [1, 2, 3, 4, 5, 6, 7, 11, 12, 15, 23, 25, 35, 36, 36, 41, 42, 44, 46, 47, 51, 52, 53, 55]
# 35 i [12] meio


def executa_busca_binaria(lista:list, item):
  tamanho_da_lista = len(lista)
  meio_da_lista = int(len(lista)/2)
  print(f'comparando o meio {lista[meio_da_lista]} com {item}')
  
  if lista[meio_da_lista] == item:
    print(f"O item {item} foi encontrado no index {meio_da_lista}")
    return f"O item {item} foi encontrado no index {meio_da_lista}"
  
  elif lista[meio_da_lista] > item:
    print('menor que o meio')
    executa_busca_binaria(lista[0:meio_da_lista], item)
  
  else:
    print('maior que o meio')
    executa_busca_binaria(lista[meio_da_lista: tamanho_da_lista], item)
    
  
  

print(executa_busca_binaria(lista_numeros, 44))

print(lista_numeros[0:12])