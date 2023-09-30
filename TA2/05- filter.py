linguagens = "Python Java Javascript C C#".split()

def starts_with_j(linguagem):
    return linguagem.startswith('J')

linguagens_com_j = filter(starts_with_j, linguagens)

print(list(linguagens_com_j))


# ================================================================
numeros = [2, 5, 9, 12, 19, 23, 40, 50, 60, 75, 206]

def divisiveis_por_3(numero):
  return (numero % 3) == 0

numeros_divisiveis_por_3 = filter(divisiveis_por_3, numeros)

print(list(numeros_divisiveis_por_3))

# ================================================================ 
numeros_sequenciais = list(range(0,21)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros_sequenciais))

print(numeros_pares)