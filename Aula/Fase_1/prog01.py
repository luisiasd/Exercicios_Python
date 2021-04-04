file = open("teste.txt", "w")
file.write("Joelma Ferreira\n")
file.close()

file = open("teste.txt", "r")
dados = file.read()
file.close()

for x in file:
    print(dados)
