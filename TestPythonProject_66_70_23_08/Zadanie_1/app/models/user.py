from TestPythonProject_66_70_23_08.Zadanie_1.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from TestPythonProject_66_70_23_08.Zadanie_1.app.models import *


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    task = relationship('Category', back_populates='task')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))