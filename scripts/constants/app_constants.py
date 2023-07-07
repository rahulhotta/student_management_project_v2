from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    branch: str


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str


average_age_aggregation = [
    {
        '$group': {
            '_id': None,
            'avgAge': {
                '$avg': '$age'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
]
