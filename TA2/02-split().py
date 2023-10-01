texto = "Aprendendo Python na disciplina de linguagem de programação"

print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()
palavras = texto.split(",")
palavras = texto.split("de")

print(f"Palavras = {palavras}")
print(f"Quantidade de palavras =  {len(palavras)}")