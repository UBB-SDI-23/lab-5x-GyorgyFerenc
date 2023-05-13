from flask_restful import Resource, reqparse, request
from controller.controller import controller
import model.status_codes as StatusCode
from model.database_models import *
from .todo_resource import todo_parser


class ProjectList(Resource):
    """
        Returns a list of persons

        {"projects" : [project...]}
    """

    def get(self,page_size,page_number):
        list = controller.get_all_projects(page_size,page_number)
        list_json = ProjectSchema(many=True).dump(list)
        return list_json, StatusCode.OK


class ProjectGet(Resource):
    """
        Returns a person with the id
        {
            "project": person
        }
    """

    def get(self, id):
        project = controller.get_project(id)
        project_json = ProjectWithRelationsSchema().dump(project)
        return project_json, StatusCode.OK


project_parser = reqparse.RequestParser()
project_parser.add_argument("name", type=str)
project_parser.add_argument("description", type=str)
project_parser.add_argument("start_date", type=str)
project_parser.add_argument("end_date", type=str)
project_parser.add_argument("priority_level", type=int)


class ProjectAdd(Resource):
    """
        Adds the person

        Returns the id
        {
            "id": int
        }
    """

    def put(self):
        person = project_parser.parse_args()
        id = controller.add_project(person)
        return {"id": id}, StatusCode.OK


class ProjectRemove(Resource):
    """
        Removes the project with the given id
    """

    def delete(self, id):
        controller.remove_project(id)
        return {}, StatusCode.OK


class ProjectUpdate(Resource):
    """
        Updated the project with the given id
    """

    def patch(self, id):
        person = project_parser.parse_args()
        controller.update_project(id, person)
        return {}, StatusCode.OK


class ProjectTodoBulk(Resource):

    def put(self, id):
        for todo in request.json:
            todo['project_id'] = id
            controller.add_todo(todo)
        return {}, StatusCode.OK
