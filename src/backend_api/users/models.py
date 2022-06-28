from datetime import datetime
from email.policy import default
from inspect import classify_class_attrs
from xmlrpc.client import Boolean
from sqlalchemy import BOOLEAN, Column, Integer, String, DateTime, true
from config.db_settings import DatabaseConnection


Base = DatabaseConnection.base_instance()


class AuthGroup(Base):
    """权限组分类"""
    __tablename__ = "auth_group"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"authGroup(id={self.id}, name={self.name})"


class AuthGroupPermissions(Base):
    """权限组权限"""
    __tablename__ = "auth_group_permissions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=True)

    def __repr__(self):
        return f"authGroupPermissions(id={self.id}, \
            group_id={self.group_id}, permission_id={self.permission_id})"


class AuthUserGroups(Base):
    """用户权限组"""
    __tablename__ = "auth_user_groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"authGroupPermissions(id={self.id}, \
            group_id={self.group_id}, permission_id={self.user_id})"


class AUthPermission(Base):
    __tablename__ = "auth_permission"

    def __repr__(self):
        return f"authGroup(id={self.id}, name={self.name})"


class AUthUser(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    is_superuser = Column(Boolean, default=True)
    last_login = Column(DateTime, default=now())
    is_staff = Column(Boolean, default=1)
    is_active = Column()

    def __repr__(self):
        return f"authGroup(id={self.id}, name={self.user_name})"















class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20),nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)