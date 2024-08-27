from TestPythonProject_66_70_23_08.Zadanie_1.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from TestPythonProject_66_70_23_08.Zadanie_1.app.models import *

class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True, index=True )
    slug = Column(String, unique=True, index=True)
    user = relationship("user", back_populates="task")

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))