from sqlalchemy.orm import Session
from scripts.constants.sql_models import Student
from scripts.logging.log_config import getLogger
import traceback
logger = getLogger()


class Sql_db:
    def find_by_id(self, id: int, db: Session):
        try:
            data_by_id = db.query(Student).filter(Student.id == id).first()
            if data_by_id:
                return [data_by_id]
            else:
                return []
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def view_all_data(self, db: Session):
        try:
            return list(db.query(Student).offset(0).limit(100).all())
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def add_data_to_db(self, data, db: Session):
        try:
            db_data = Student(id=data.id, name=data.name,
                              age=data.age, branch=data.branch)
            db.add(db_data)
            db.commit()
            db.refresh(db_data)
            return {"status": "success", "Message": "Data added successfully!"}

        except Exception as e:
            traceback.print_exc()
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def update_data_in_db(self, id, data, db: Session):
        try:
            db_data = db.query(Student).get(id)
            if db_data:
                db_data.id = data.id
                db_data.name = data.name
                db_data.age = data.age
                db_data.branch = data.branch
                db.commit()
                db.refresh(db_data)
                return {"status": "success", "Message": "Data updated successfully!"}
            return {"message": "data not found"}
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def delete_data_from_db(self, data_id: int, db: Session):
        try:
            db_data = db.query(Student).get(data_id)
            if db_data:
                db.delete(db_data)
                db.commit()
                return {"message": "Deleted Successfully"}
            return {"Error": "Student not found"}
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}


sql_db_obj = Sql_db()
