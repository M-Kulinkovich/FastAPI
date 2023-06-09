from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, Column, JSON, Table, Boolean
from sqlalchemy.orm import DeclarativeBase

from database import metadata

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON),
)


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registered_time', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, nullable=False)
    registered_time = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
