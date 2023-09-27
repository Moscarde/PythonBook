# Operadores Relacionais == === != > < >= <=
nome = 'Gabriel'
sobrenome = ''

lista:list = []

if nome:
	print('A variavel nome não é vazia')


# Estrutura composta

valor1 = 10
valor2 = 20

if valor1 > valor2:
	print('O valor1 é maior')
else:
	print('O valor1 é menor')

# Estrutura encadeada

cor = 'Alguma cor'

if cor == 'verde':
	print('acelerar')
elif cor == 'amarelo':
	print('atenção')
else:
	print('parar')


# Operadores Condicionais and or not

qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
	print("Aluno Aprovado!")
else:
	print("Aluno reprovado!")

