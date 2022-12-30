import imp
from fastapi import FastAPI, Response
from schemas import *
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
import databases
import sqlalchemy
from databases import engine
import models
import services
metadata = sqlalchemy.MetaData()
models.Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/class")
def create_class(request: CreateClass, response: Response, db: Session = Depends(databases.get_db)):
    return services.create_class(request, response, db)


@app.post("/student")
def create_student(request: CreateStudent, response: Response, db: Session = Depends(databases.get_db)):
    return services.create_student(request, response, db)


@app.get("/students")
def class_students(class_id: int, response: Response, db: Session = Depends(databases.get_db)):
    return services.class_students(class_id, response, db)


@app.put("/students/{student_id}")
def update_students(request: UpdateStudent, student_id: int, response: Response, db: Session = Depends(databases.get_db)):
    return services.update_students(request, student_id, response, db)


@app.delete("/students/{student_id}")
def delete_students(student_id: int, response: Response, db: Session = Depends(databases.get_db)):
    return services.delete_students(student_id, response, db)


@app.get("/students/{student_id}")
def get_student(student_id: int, response: Response, db: Session = Depends(databases.get_db)):
    return services.get_student(student_id, response, db)
