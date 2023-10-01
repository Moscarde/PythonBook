alunos = {"João", "Maria", "Pedro", "Ana", "Joaquim"}

novo_aluno = input("Digite o nome do novo aluno: ")

print(novo_aluno in alunos)

if novo_aluno not in alunos:
	# alunos.append(novo_aluno)
	alunos.add(novo_aluno)
	print("Novo aluno cadastrado com sucesso!")

print(alunos)
