import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self):
        self._host = os.getenv("DB_HOST")
        self._port = int(os.getenv("DB_PORT"))
        self._user = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._database = os.getenv("DB_NAME")

    def conectar(self):
        try:
            return mysql.connector.connect(
                host=self._host,
                port=self._port,
                user=self._user,
                password=self._password,
                database=self._database,
            )
        except mysql.connector.Error as erro:
            print(f"Erro ao conectar ao banco: {erro}")
            return None