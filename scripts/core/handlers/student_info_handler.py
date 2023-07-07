from scripts.core.db.mongo_db import student_database_object
from scripts.core.db.sql_db import sql_db_obj
from scripts.constants.app_constants import Student
from scripts.logging.log_config import getLogger
from sqlalchemy.orm import Session


logger = getLogger()
class Student_handler:
    def view_all_student(self,db: Session):
        try :
            all_students = sql_db_obj.view_all_data(db)
            if all_students == []:
                return {"status": "Success","Message":"No students found"}
            return all_students 
        except Exception as e:
            logger.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
    def add_new_student(self, student_id:int, student: Student,db: Session):
        try:
            if sql_db_obj.find_by_id(student_id,db) != []:
                return {"status": "failed","error":"Student already exist"}
                # return sql_db_obj.find_by_id(student_id,db)
            # db_data = Student(id=student.id, name=student.name,
            #                   age=student.age, branch=student.branch)
            return sql_db_obj.add_data_to_db(student,db)
        except Exception as e:
            logger.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
        
    def update_student(self,student_id:int, student: Student,db: Session):
        try:
            if sql_db_obj.find_by_id(student_id,db) == []:
                return {"status": "failed","error":"Student does not exist"}
            return sql_db_obj.update_data_in_db(student_id, student,db)
        except Exception as e:
            logger.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
    def delete_student(self,student_id:int,db: Session):
        try:
            if sql_db_obj.find_by_id(student_id,db) == []:
                return {"status": "failed","error":"Student does not exist"}
            return sql_db_obj.delete_data_from_db(student_id,db)
        except Exception as e:
            logger.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
    # def calculate_avg_age(self):
    #     try:
    #         avg_age = student_database_object.mongo_aggregation()
    #         avgList = list(avg_age)
    #         return avgList[0]["avgAge"]
    #     except Exception as e:
    #         logger.error({"status": "failed","error":str(e.args)})
    #         return {"status": "failed","error":str(e.args)}
    

        


