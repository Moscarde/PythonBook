texto = "Aprendendo Python na disciplina de linguagem de programação"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")

vogais:list = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
  print(f"Posição = {vogais.index(vogal)}, valor = {vogal}")