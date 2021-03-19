def cadastrar():
    num_emps = int(input('Quantos registros de empregados quer criar? '))
    arquivo = open('empregados.txt', 'w')

    for n in range(1, num_emps + 1):
        print('Entre com os dados do empregado #', n)
        nome    = input('Nome: ')
        id_emp  = input('ID: ')
        dept    = input('Departamento: ')
        salario = input("Salário: ")
        idade   = input("Idade: ")

        #Constante é interessante colocar tudo em maiusculo
        #Poderia ser colocado o separador como limitadro - VIRGULA
        arquivo.write(nome    + ",")
        arquivo.write(id_emp  + ",")
        arquivo.write(dept    + ",")
        arquivo.write(salario + "\n")
        print()
  
    arquivo.close()
    print("Empregados cadastrados com sucesso!!")

def cabecalho():
    print("*"*52)
    companhia = "Nova Floresta, LTDA."
    endereco  = "Rua das Águas, 456"
    cidade    = "Goiânia, Goiás"

    print(f"\t\t{companhia}")
    print(f"\t\t{endereco}")
    print(f"\t\t{cidade}")
    print("="*52)

def rodape():
    print("Faça uma coisa boa por alguém hoje!".center(52))
    print("*"*52)

def consultar():
    arquivo = open('empregados.txt', 'r')

    nome = arquivo.readline()
    while nome != '':
        id_emp = arquivo.readline()
        dept = arquivo.readline()

        nome = nome.rstrip('\n')
        id_emp = id_emp.rstrip('\n')
        dept = dept.rstrip('\n')

        print("Nome: ", nome)
        print("ID: ", id_emp)
        print("Dept: ", dept)
        print()

        nome = arquivo.readline()

    arquivo.close()

def main():
#    cadastrar()
#   consultar()
    cabecalho()
    rodape()

main()