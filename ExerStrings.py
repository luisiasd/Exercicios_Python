#Parte 1: Ler uma string e trocar sobrenome Silva por Ferreira.
#Parte 2: Ler uma string e trocar todos os carateres “a” por “@”.
def testando_Replace():
    nome = input("Nome: ")
    nome = nome.replace("Silva", "Ferreira")
    nome = nome.replace("a", "@")
    print(nome)
    separador()

#Parte 1: Ler uma string e quebrá-la por “espaços”.
#Parte 2: Ler uma string e quebrá-la em “,”.
def testando_Split():
    nome = input("Nome: ")
    dados = nome.split()
    print(dados)

    registro = "José da Silva, 27, Gerente Financeiro, 3.456"
    dados = registro.split(",")

    print(dados)

    separador()

#Usar os comandos lstrip, rstrip e strip para 
# retirar caracteres “.”  e espaço de uma string.
def testando_Sprit():
    endereco = "....Endereço: Rua.... Chinesa..."
    print(endereco.lstrip('.'))
    print(endereco.rstrip('.'))
    print(endereco.strip('.'))

    endereco = "     Endereço: Rua.... Chinesa   "
    print(endereco.lstrip())
    print(endereco.rstrip())
    print(endereco.strip())

    separador()

#Montar uma string distinta a partir de cada uma das listas abaixo. 
# A primeira usando o separados “/” e a segunda o espaço:
#lista = ["22","4","1500"]
#palavras = ['Ahhh,', 'eu', 'amei', 'te', 'ver!’] 
def testando_Join():
    lista = ["22","4","1500"]
    palavras = ['Ahhh,', 'eu', 'amei', 'te', 'ver!'] 

    data = "/".join(lista)
    print(data)
    separador()

    delimitador = " "
    musica = delimitador.join(palavras)
    print(musica)
    separador()

#Criar uma string e contar quantas letras “a” existem nela.
def testando_Count():
    mensagem = "É para ficar em casa!!!!"
    resposta = mensagem.count("a")
    print("A quantidade de a é", resposta)
    separador()

def separador():
    print()
    print("="*40 + "\n")

def main():
    #testando_Replace()
    #testando_Split()
    #testando_Sprit()
    #testando_Join()
    testando_Count()

main()
