import pyodbc

class DataBase:
    def __init__(self):
        self.server = 'tcc-db-srv.database.windows.net:1433'
        self.database = 'tcc-bd'
        self.username = 'adm'
        self.password = 'Abc789@#dsfdsf'
        self.driver ='{SQL Server}'
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pyodbc.connect('DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def insert_game_smell(self, id, tipo, quant):
        self.cursor.execute("INSERT INTO game_smells (id, tipo, quant) VALUES (?, ?, ?)", (id, tipo, quant))
        self.conn.commit()
        print("Dados inseridos na tabela game_smells com sucesso.")

    def insert_metricas_qualidade(self, id, complexidade_ciclomatica, perc_linhas_duplicadas, indice_divida_tecnica, bugs):
        self.cursor.execute("INSERT INTO metricas_qualidade (id, complexidade_ciclomatica, perc_linhas_duplicadas, indice_divida_tecnica, bugs) VALUES (?, ?, ?, ?, ?)",
                            (id, complexidade_ciclomatica, perc_linhas_duplicadas, indice_divida_tecnica, bugs))
        self.conn.commit()
        print("Dados inseridos na tabela metricas_qualidade com sucesso.")

# Exemplo de uso da classe
connector = SQLServerConnector(server='seu_servidor', database='seu_banco_de_dados', username='seu_usuario', password='sua_senha')

connector.connect()

connector.insert_game_smell("001", "Controle de Versão", 5)
connector.insert_metricas_qualidade("001", 10, 20, 30, 5)

connector.disconnect()
