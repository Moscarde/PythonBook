linguagens = "Python Java Javascript C C#".split()

def to_lower(linguagem):
  return linguagem.lower()

linguagens_lower = map(to_lower, linguagens)

print(linguagens_lower)
print(list(linguagens_lower))


# Definindo a função de multiplicação
def multiplicar_por_dois(numero):
    return numero * 2

# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Usando a função map para aplicar a função a cada elemento da lista
resultado = map(multiplicar_por_dois, numeros)

# Convertendo o iterador em uma lista para visualizar os resultados
resultado_lista = list(resultado)

print(resultado_lista)