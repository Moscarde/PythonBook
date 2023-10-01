# Verifica elemento a elemento se o valor é igual ao de busca
def executar_busca_linear(lista, valor):
    for item in lista:
        if item == valor:
            return lista.index(item)
    return False
        

lista_alunos = "Gabriel Laura Nicolas Marcio Silvana Luiz Marta Marcos Lilian Louise Camile Loyola Marcia Maria".split(" ")

print(executar_busca_linear(lista_alunos, "Marcio"))