from fastapi import APIRouter
from scripts.core.handlers.student_info_handler import Student_handler
from scripts.constants.app_constants import Student
from scripts.core.handlers.email_handler import email_object, Email
from scripts.logging.log_config import getLogger
from json2html import *
from fastapi import Depends
from scripts.utility.sql_utility import SessionLocal, engine
from scripts.utility.sql_utility import Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


logger = getLogger()
student_router = APIRouter()


# @student_router.get("/send_email")
# def send_an_email(email: Email):
#     try:
#         student_object = Student_handler()
#         all_students_list_json = student_object.view_all_student()

#         table = json2html.convert(json = all_students_list_json)
#         styles = {
#         "th": 'color: white; background-color: #333; padding:1rem;',
#         "td": 'text-align: center; padding:1rem;'
#             }
#         for tag, style in styles.items():
#             table = table.replace("<{}>".format(tag), '<{} style="{}">'.format(tag, style))
#         email_object.send_email(table, email)
#         return {"Message": "email sent!!"}
#     except Exception as e:
#         logger.error({"status": "failed", "error": str(e.args)})
#         return {"status": "failed", "error": str(e.args)}


@student_router.get("/view-all-students")
def view_students(db: Session = Depends(get_db)):
    try:
        student_object = Student_handler()
        all_students = student_object.view_all_student(db)
        return all_students
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    try:
        student_object = Student_handler()
        response = student_object.add_new_student(student_id, student, db)
        return response
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.put("/update-student/{student_id}")
def update_a_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    try:
        student_object = Student_handler()
        response = student_object.update_student(student_id, student, db)
        return response
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.delete("/delete-student/{student_id}")
def delete_a_student(student_id: int, db: Session = Depends(get_db)):
    try:
        student_object = Student_handler()
        response = student_object.delete_student(student_id, db)
        return response
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}
