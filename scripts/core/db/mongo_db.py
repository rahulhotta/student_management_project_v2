from pymongo import MongoClient
from scripts.utility.mongo_utility import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME
from scripts.constants.app_constants import average_age_aggregation
from scripts.logging.log_config import getLogger
logger = getLogger()


class Mongo_database:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_URI)
            logger.info("URI connected")
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
        try:
            self.db = self.client[MONGO_DB_NAME]
            logger.info("Connected to DB")
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
        try:
            self.collection = self.db[MONGO_COLLECTION_NAME]
            logger.info("Connected to the collection")
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})

    def view_all_data(self):
        try:
            collection_data = list(self.collection.find({}, {'_id': False}))
            logger.info({"status": "Success", "Message": "Fetched all data"})
            return collection_data
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def find_by_id(self, id):
        try:
            found_data = list(self.collection.find(id,{"_id":False}))
            logger.info({"status": "Success", "Message": "Fetched data by id"})
            return found_data
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def add_data_to_db(self, data):
        try:
            self.collection.insert_one(data.dict())
            logger.info({"status": "Success", "Message": "Added data to db"})
            return {"status": "success", "Message": "Data added successfully!"}
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def update_data_in_db(self, obj_id: int, data):
        try:
            self.collection.update_one(
                {"id": obj_id}, {"$set": data.dict()})
            logger.info({"status": "Success", "Message": "Updated data in db"})
            return {"status": "success", "Message": "Data updated successfully!"}
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def delete_data_from_db(self, obj_id: int):
        try:
            self.collection.delete_one({"id": obj_id})
            logger.info({"status": "Success", "Message": "Deleted data from db"})
            return {"status": "success", "Message": "Deleted successfully!"}
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}
    def mongo_aggregation(self):
        try:
            return self.collection.aggregate(average_age_aggregation)
        except Exception as e:
            logger.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

student_database_object = Mongo_database()
