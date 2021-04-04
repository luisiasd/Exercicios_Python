import locale

def cadastrar():
    num_emps = int(input("Quantos registros de empregados quer criar: "))
    arquivo = open("empregados.txt", "w")

    for n in range(1, num_emps + 1):
        print("Entre com os dados do empregado # ", n)
        nome = input("Nome: ")
        id_emp = input("ID: ")
        dept = input("Departamento: ")
        salario = input("Salário: ")
        idade = input("Idade: ")

        arquivo.write(nome + ",")
        arquivo.write(id_emp + ",")
        arquivo.write(dept + ",")
        arquivo.write(salario + ",")
        arquivo.write(idade + "\n")

        print()

    arquivo.close()
    print("Empregados cadastrados com sucesso!!!")


def cabecalho():
    print("*"*52)
    companhia = "Nova Floresta, LTDA."
    endereco = "Ruas das Águas, 456"
    cidade = "Goiânia - GO"

    print(f"\t\t{companhia}")
    print(f"\t\t{endereco}")
    print(f"\t\t{cidade}")
    print("="*52)

def rodape():
    print("Faça uma coisa boa por alguém hoje!".center(52))
    print("*"*52)

def consultar():
    locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')

    try:
        arquivo = open("empregados.txt", "r")
        cabecalho()

        for registro in arquivo.readlines():
            dados = registro.split(",")

            nome = dados[0].rstrip('\n')
            id_emp = dados[1].rstrip('\n')
            dept = dados[2].rstrip('\n')
            salario = float(dados[3].rstrip('\n'))
            idade = dados[4].rstrip('\n')

            print(nome, end="\t")
            print("|", id_emp, end="\t")
            print("|", dept, end="\t")
            print("| R$", 
                str(locale.currency(salario, grouping=True)).replace("R$",""), end="\t")
            print("|", idade, end="\n")
            print("-"*52)

        arquivo.close()
        rodape()

    except OSError as e:
        print("OS error: {}".format(e))

def main():
    #cadastrar()
    consultar()

main()

