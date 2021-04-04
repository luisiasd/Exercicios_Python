import pyodbc
class conexaoSQLSERVER:
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
            except OSError as er_SQL:
                print("Erro no cadastro de empregados: {}".format(er_SQL))
    BDHelpDesk = conexao_sql()
