from flask_restful import Resource, reqparse
from controller.controller import controller
import model.status_codes as StatusCode
from model.database_models import *


class TodoPriorityReport(Resource):
    def get(self):
        list = controller.report_projects_by_number_of_done_todos()
        return list, StatusCode.OK

class TodoEndDateReport(Resource):
    def get(self, end_date):
        list = controller.report_todos_by_project_end_date(end_date)
        list_json = TodoSchema(many=True).dump(list)
        return list_json, StatusCode.OK
