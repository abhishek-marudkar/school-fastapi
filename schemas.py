from pydantic import BaseModel
from typing import Union, List


class CreateClass(BaseModel):
    name: str
    description: str


class CreateStudent(BaseModel):
    name: str
    age: int
    class_id: int


class UpdateStudent(BaseModel):
    name: str
    age: int


#! Response Schemas


class ResponseCreateClass(BaseModel):
    id: int
    name: str
    description: str


class ResponseCommonMessage(BaseModel):
    message: str


class ResponseClassStudent(BaseModel):
    id: int
    name: str
    age: int


class ResponseCreateStudent(BaseModel):
    id: int
    name: str
    age: int
    class_id: int


class ResponseClassId(BaseModel):
    students: List[ResponseClassStudent]
