from ctypes import Union
from multiprocessing import connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class DatabaseConnection(object):
    """初始化数据库连接.
    """
    def __init__(
        self,
        database: str,
        user: str,
        password: str,
        host: str = "127.0.0.1",
        port: int = 3306
    ) -> None:
        self.HOST = "35.193.161.48"
        self.DATABASE = "cools"
        self.USERNAME = "root"
        self.PASSWORD = "qw246850"
        self.PORT = port
        self.engine = self.generate_engine()

    def generate_engine(self):
        DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(
            self.USERNAME,
            self.PASSWORD,
            self.HOST,
            self.DATABASE,
            self.PORT
        )
        return create_engine(DB_URI)

    @staticmethod
    def base_instance(self):
        return declarative_base(self.engine)

    def get_connection(self):
        return self.engine.connect()

    def fetch_data(self):
        connection = self.get_connection()



if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    # Base = declarative_base(engine)
