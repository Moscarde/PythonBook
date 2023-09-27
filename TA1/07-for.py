nome = "Guido"

for c in nome:
	print(c)

notasBimestre:list = [4, 5, 8, 10]

mediaFinal:float = 0

	# counter, posIten
for bimestre, nota in enumerate(notasBimestre):
	bimestre+=1

	if nota < 6:
		print(f"{bimestre}º bimestre - Abaixo da média")
	else:
		print(f"{bimestre}º bimestre - Acima da média")

	mediaFinal+= nota

mediaFinal = mediaFinal/4

if mediaFinal>=6:
	print(f"{mediaFinal}pts - Aluno aprovado")
else:
	print(f"{mediaFinal}pts - Aluno em recuperação")


# Aumenta o counter
for i in range(10):
	print(i)
