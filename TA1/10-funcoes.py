# Convenção ser em minusculo e seprardo por _
def imprimir_mensagem(disciplina, curso):
  print(f"Minha primeira funcao em python desenvolvido na disciplina {disciplina} no curso {curso}")

imprimir_mensagem("Python", "ADS")


# Parametros obrigatórios
def somar(a, b):
  return a+b

r = somar(2, 3)

print(r)

# Parametros nao obrigatórios
def calcular_desconto(valor, desconto=0):
  # O parametro desconto possui o 0 como valor default
  valor_com_desconto = valor - (valor * desconto)
  return valor_com_desconto

valor1 = calcular_desconto(100) # Nao aplicado desconto
valor2 = calcular_desconto(100, 0.25) # Aplicado desconto

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

# Parametros nominais
def converter_maiuscula(texto, flag_maiuscula):
  if flag_maiuscula:
    return texto.upper()
  else:
    return texto.lower()

# Passagem nominal de parametros, nao importa a ordem
texto = converter_maiuscula(flag_maiuscula=True, texto="Gabriel")
print(texto)


# Parametro posicional e nao obrigatórios
# parametro vira um array de parametros
def imprimir_parametros(*args):
  qtde_parametros = len(args)
  print(f"Quantidade de parametros = {qtde_parametros}")

def mostrar_parametros(*args):
  for i, valor in enumerate(args):
    print(f"Posição = {i}, valor = {valor}")
  

  print(args[0])


imprimir_parametros("Sao paulo", 10, 23, "Joao")
mostrar_parametros("Sao paulo", 10, 23, "Joao")

# Parametro nominal e nao obrigatório
def imprimir_param(**kwargs):
  print(f"Tipo de objeto recebido = {type(kwargs)}\n")
  qtde_parametros = len(kwargs)
  print(f"quantidade de parametros = {qtde_parametros}")

  for chave, valor in kwargs.items():
    print(f"variavel = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_param(cidade="Sao paulo", idade=33, nome="Gab")
print("\nChamada 2")
imprimir_param(desconto=10, valor=100)

# Funcoes anonimas

soma = lambda x, y: x + y
print(soma(x=5, y=3))

subtrai = lambda x,y: x - y
print(subtrai(x=10, y=4))