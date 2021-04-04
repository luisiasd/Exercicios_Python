import pyodbc

class CadastroUsuarios:
    def __init__(self,nome, sobrenome, email, cpf, teamview):
        try:
           self.nome        = nome
           self.sobrenome   = sobrenome
           self.email       = email
           self.cpf         = cpf
           self.teamview    = teamview
        except OSError as e:
            print("Erro no cadastro de empregados: {}".format(e))

    def conexao_sql():
        try:
            server = "xyz"
            database = "xyz"
            username = "xyz"
            password = "xyz"
            #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
            string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
            conexao = pyodbc.connect(string_conexao)
            return conexao.cursor()
        except Error as er_SQL:
            print("Error na Conexão ao Banco de dados")
    BDHelpDesk = conexao_sql()



    vsql="""INSERT INTO [dbo].[Registro_Usuarios](nome,sobrenome,email,cpf,teamview) VALUES ('nome','sobrenome','email','cpf','teamview')"""
    def InserindoDados(conexao,sql):
        try:
            BDHelpDeskIsert = conexao.cursos()
            BDHelpDeskIsert.execute(sql)
            BDHelpDesk.commit()
        except Error as er:
            Print(er)
        print('Valores inseridos: ' + str(BDHelpDeskIsert))
InserindoDados(BDHelpDesk,vsql)
