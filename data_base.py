import os
from dotenv import load_dotenv
import pyodbc

class DataBase:
    def __init__(self):
        load_dotenv()
        self.server = os.getenv("DB_HOST")
        self.database = os.getenv("DB_DATA_BASE")
        self.username = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
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

