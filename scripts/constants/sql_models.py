from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from scripts.utility.sql_utility import Base


class Student(Base):
    __tablename__ = "rahul_new_student3"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    branch = Column(String)