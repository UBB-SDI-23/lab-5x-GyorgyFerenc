from model.database_models import *
from flask_restful import Resource, reqparse
import model.status_codes as StatusCode
from controller.controller import controller


class TodoList(Resource):
    """
        Returns a list of todos

        {"todos" : [todo...]}
    """

    def get(self,page_size,page_number):
        list = controller.get_all_todos(page_size,page_number)
        list_json = TodoSchema(many=True).dump(list)
        return {"todos": list_json}, StatusCode.OK


class TodoGet(Resource):
    """
        Returns a todo with the id
        {
            "todo": todo
        }
    """

    def get(self, id):
        todo = controller.get_todo(id)
        json = TodoSchema().dump(todo)
        return {"todo": json}, StatusCode.OK


todo_parser = reqparse.RequestParser()
todo_parser.add_argument("name", type=str)
todo_parser.add_argument("description", type=str)
todo_parser.add_argument("deadline", type=str)
todo_parser.add_argument("done", type=bool)
todo_parser.add_argument("project_id", type=int)


class TodoAdd(Resource):
    """
        Adds the todo

        Returns the id
        {
            "id": int
        }     
    """

    def put(self):
        todo = todo_parser.parse_args()
        id = controller.add_todo(todo)
        return {"id": id}, StatusCode.OK


class TodoRemove(Resource):
    """
        Removes the todo with the given id
    """

    def delete(self, id):
        controller.remove_todo(id)
        return {}, StatusCode.OK


class TodoUpdate(Resource):
    """
        Updated the todo with the given id
    """

    def patch(self, id):
        person = todo_parser.parse_args()
        controller.update_todo(id, person)
        return {}, StatusCode.OK

