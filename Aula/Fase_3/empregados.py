class Empregado:
    #Método para gravar um registro de empregado no arquivo texto
    def cadastrar(self,nome,id_emp,dept,salario,idade):
        try:
            arquivo = open("empregados.txt", "a")
            arquivo.write(nome    + ",")
            arquivo.write(id_emp  + ",")
            arquivo.write(dept    + ",")
            arquivo.write(salario + "\n")
            arquivo.write(idade + "\n")
            arquivo.close()
        except OSError as e:
            print("Erro no cadastro de empregados: {}".format(e))
