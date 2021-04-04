from empregados import Empregado

def Cadastrar():
    obj = Empregado()
    num_emps = int(input("Quantos Registros deseja cadastrar:"))
    
    for n in range(1, num_emps + 1):
        print("Entre com os dados do empregado # ", n)
        nome = input("Nome: ")
        id_emp = input("ID: ")
        dept = input("Departamento: ")
        salario = input("Salário: ")
        idade = input("Idade: ")
    print("Empregados cadastrados com sucesso!!")

def main():
    Cadastrar()
main()