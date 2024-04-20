import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

class SQLServerConnector:
    def __init__(self):
        load_dotenv()
        self.server = os.getenv("DB_HOST")
        self.database = os.getenv("DB_DATA_BASE")
        self.username = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.engine = None

    def __connect(self):
        try:
            conn_str = f"mssql+pymssql://{self.username}:{self.password}@{self.server}/{self.database}?charset=utf8"
            self.engine = create_engine(conn_str)
            print("Conexão bem sucedida!")
        except Exception as e:
            print("Erro ao conectar ao banco de dados:", e)

    def insert_data_from_dataframe(self, dataframe, table_name):
        try:
            self.__connect()
            dataframe.to_sql(name=table_name, con=self.engine, if_exists='append', index=False)
            print("Dados inseridos com sucesso.")
        except Exception as e:
            print("Erro ao inserir dados:", e)
