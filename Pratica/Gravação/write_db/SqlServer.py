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
    except Error as er_SQL:
        print("Error na Conexão ao Banco de dados")
BDHelpDesk = conexao_sql()


BDHelpDesk.execute("SELECT * FROM Registro_Usuarios")
row = BDHelpDesk.fetchone() 
while row: 
    print(row)
    row = BDHelpDesk.fetchone()


