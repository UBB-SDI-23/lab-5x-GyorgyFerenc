from flask_restful import Resource, reqparse
from controller.controller import controller
import model.status_codes as StatusCode
from model.database_models import *


class ProjectPersonList(Resource):
    """
        Returns a list of persons

        {"project_persons" : [project_person...]}
    """

    def get(self,page_size,page_number):
        list = controller.get_all_project_persons(page_size,page_number)
        list_json = ProjectPersonSchema(many=True).dump(list)
        return list_json, StatusCode.OK


class ProjectPersonGet(Resource):
    """
        Returns a person with the id
        {
            "project_person": person
        }
    """

    def get(self, id):
        project_person = controller.get_project_person(id)
        project_person_json = ProjectPersonSchema().dump(project_person)
        return project_person_json, StatusCode.OK


project_person_parser = reqparse.RequestParser()
project_person_parser.add_argument("project_id", type=int)
project_person_parser.add_argument("person_id", type=int)
project_person_parser.add_argument("role", type=str)
project_person_parser.add_argument("date", type=str)


class ProjectPersonAdd(Resource):
    """
        Adds the person to the project

        Returns the id
        {
            "id": int
        }
    """

    def put(self):
        person = project_person_parser.parse_args()
        id = controller.add_project_person(person)
        return {"id": id}, StatusCode.OK


class ProjectPersonRemove(Resource):
    """
        Removes the project_person with the given id
    """

    def delete(self, id):
        controller.remove_project_person(id)
        return {}, StatusCode.OK


class ProjectPersonUpdate(Resource):
    """
        Updated the project_person with the given id
    """

    def patch(self, id):
        person = project_person_parser.parse_args()
        controller.update_project_person(id, person)
        return {}, StatusCode.OK
