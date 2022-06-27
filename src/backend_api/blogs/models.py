from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from config.db_settings import DatabaseConnection


Base = DatabaseConnection.base_instance()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20),nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)

