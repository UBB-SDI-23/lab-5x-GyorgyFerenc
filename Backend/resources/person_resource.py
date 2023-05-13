from model.database_models import *
from flask_restful import Resource, reqparse
import model.status_codes as StatusCode
from controller.controller import controller

class PersonList(Resource):
    """
        Returns a list of persons

        {"persons" : [person...]}
    """

    def get(self,page_size,page_number):
        list = controller.get_all_persons(page_size,page_number)
        list_json = PersonSchema(many=True).dump(list)
        return {"persons": list_json}, StatusCode.OK


class PersonGet(Resource):
    """
        Returns a person with the id
        {
            "person": person
        }
    """

    def get(self, id):
        person = controller.get_person(id)
        person_json = PersonWithRelationsSchema().dump(person)
        return {"person": person_json}, StatusCode.OK


person_parser = reqparse.RequestParser()
person_parser.add_argument("first_name", type=str)
person_parser.add_argument("last_name", type=str)
person_parser.add_argument("cnp", type=str)
person_parser.add_argument("gender", type=str)
person_parser.add_argument("age", type=int)


def validate_person(person: dict) -> bool:
    cnp = person['cnp']
    gender = person['gender']
    age = person['age']

    if len(cnp) != 13:
        return False

    if gender not in ['male', 'female']:
        return False

    if age not in range(1, 120):
        return False

    return True


class PersonAdd(Resource):
    """
        Adds the person

        Returns the id
        {
            "id": int
        }     
    """

    def put(self):
        person = person_parser.parse_args()

        if not validate_person(person):
            return {"message": "Person is not valid"}, StatusCode.BAD_REQUEST

        id = controller.add_person(person)
        return {"id": id}, StatusCode.OK


class PersonRemove(Resource):
    """
        Removes the person with the given id
    """

    def delete(self, id):
        controller.remove_person(id)
        return {}, StatusCode.OK


class PersonUpdate(Resource):
    """
        Updated the person with the given id
    """

    def patch(self, id):
        person = person_parser.parse_args()
        controller.update_person(id, person)
        return {}, StatusCode.OK


class PersonFilter(Resource):

    """
        Filters by age < person.age
        {"persons" : [person...]}
    """

    def get(self, age):
        list = controller.filter_person_by_age(age)
        list_json = PersonSchema(many=True).dump(list)
        return {"persons": list_json}, StatusCode.OK
