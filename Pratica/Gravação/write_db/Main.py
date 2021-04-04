from Cadastro_Usuario import Usuario

def Cadastrar():
    obj = Usuario()
    num_usuario = 0
    for n in range(1, num_usuario + 1):
        nome        = input("Nome: ")
        sobrenome   = input("Sobrenome: ")
        email       = input("Email: ")
        cpf         = input("CPF: ")
        teamview    = input("TeamView: ")
    print("Cadastrados Realizado com sucesso!!")

def main():
    InserindoDados()
main()
