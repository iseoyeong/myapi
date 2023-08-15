# coding: utf-8
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

from database import Base
from database import ENGINE

class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=True)
    password = Column(String(30), nullable=True)


class User(BaseModel):
    id : int
    name : str
    password : int

if __name__ == "__main__":
    # 테이블 생성
    Base.metadata.create_all(bind=ENGINE)