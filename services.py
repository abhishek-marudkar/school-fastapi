from fastapi import status
from sqlalchemy.orm import Session
import schemas
import models


def create_class(request, response, db: Session):
    data_exist = db.query(models.Class).filter(
        models.Class.name == request.name).first()
    if data_exist:
        response.status_code = status.HTTP_409_CONFLICT
        res = schemas.ResponseCommonMessage(
            message="Class with this name already exist!")
        return res
    new_class = models.Class(
        name=request.name, description=request.description)
    db.add(new_class)
    db.flush()
    db.commit()
    response.status_code = status.HTTP_201_CREATED
    res = schemas.ResponseCreateClass(
        id=new_class.id, name=new_class.name, description=new_class.description)
    return res


def create_student(request, response, db: Session):
    class_exist = db.query(models.Class).filter(
        models.Class.id == request.class_id).first()
    if not class_exist:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        res = schemas.ResponseCommonMessage(
            message="Invalid Class Id!")
        return res
    data_exist = db.query(models.Students).filter(
        models.Students.name == request.name and models.Students.age == request.age and models.Students.class_id == request.class_id).first()
    if data_exist:
        response.status_code = status.HTTP_409_CONFLICT
        res = schemas.ResponseCommonMessage(
            message="student with this name already exist!")
        return res
    new_student = models.Students(
        name=request.name, age=request.age, class_id=request.class_id)
    db.add(new_student)
    db.flush()
    db.commit()
    response.status_code = status.HTTP_201_CREATED
    res = schemas.ResponseCreateStudent(
        id=new_student.id, name=new_student.name, age=new_student.age, class_id=new_student.class_id)
    return res


def class_students(class_id, response, db: Session):
    students = db.query(models.Students).filter(
        models.Students.class_id == class_id)
    if students.count() == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        res = schemas.ResponseCommonMessage(
            message="Students not found!")
        return res
    students_list = []
    for student in students:
        students_list.append(schemas.ResponseClassStudent(
            id=student.id, name=student.name, age=student.age))
    response.status_code = status.HTTP_200_OK
    res = schemas.ResponseClassId(students=students_list)
    return res


def update_students(request, student_id, response, db: Session):
    student = db.query(models.Students).filter(
        models.Students.id == student_id).first()
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
        res = schemas.ResponseCommonMessage(
            message="Student not found!")
        return res
    student.name = request.name
    student.age = request.age
    db.merge(student)
    db.commit()
    res = schemas.ResponseClassStudent(
        id=student.id, name=student.name, age=student.age)
    response.status_code = status.HTTP_200_OK
    return res


def delete_students(student_id, response, db: Session):
    student = db.query(models.Students).filter(
        models.Students.id == student_id).first()
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
        res = schemas.ResponseCommonMessage(
            message="Student not found!")
        return res
    db.delete(student)
    db.commit()
    response.status_code = status.HTTP_202_ACCEPTED
    res = schemas.ResponseCommonMessage(
        message=f"Successfully deleted student with ID {student_id}")
    return res


def get_student(student_id, response, db: Session):
    student = db.query(models.Students).filter(
        models.Students.id == student_id).first()
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
        res = schemas.ResponseCommonMessage(
            message="Student not found!")
        return res
    response.status_code = status.HTTP_200_OK
    res = schemas.ResponseClassStudent(
        id=student.id, name=student.name, age=student.age)
    return res
