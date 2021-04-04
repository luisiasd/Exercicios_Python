import pyodbc
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
    except OSError as e:
        print("Erro na Conexão: {}".format(e))
BDHelpDesk = conexao_sql()

vsql = """INSERT INTO [dbo].[Registro_Usuarios](nome,sobrenome,email,cpf,teamview) 
                VALUES ('"+nome+"','"+sobrenome+"','"+email+"','"+cpf+"','"+teamview+"')"""
def InserindoDados(conexao,sql):
    try:
        BDHelpDeskIsert = conexao.cursor()
        BDHelpDeskIsert.execute(sql)
        conexao.commit()
        print("Registro Inseridos")
    except OSError as ex:
        Print("Erro na Inserção de Dados: {}".format(ex)) 

nome        = input("Nome: ")
sobrenome   = input("Sobrenome: ")
email       = input("Email: ")
cpf         = input("CPF: ")
teamview    = input("TeamView: ")




InserindoDados(BDHelpDesk,vsql)
