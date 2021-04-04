dados = []
dados.append("Linha 2 \n")
dados.append("Linha 3 \n")
dados.append("Linha 4 \n")

file = open("teste.txt", "w")
file.writelines(dados)
file.close()
