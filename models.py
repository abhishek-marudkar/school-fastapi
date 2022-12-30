from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import Base


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer(), autoincrement=True, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    description = Column(String(255))


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer(), autoincrement=True, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    age = Column(Integer())
    class_id = Column(ForeignKey('classes.id'))
