from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from repository.database import database
from model.database_models import *
from resources.person_resource import *
from resources.project_resource import *
from resources.todo_resource import *
from resources.project_preson_resource import *
from resources.report_resource import *
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@34.65.213.59/flask_api"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
CORS(app)

api = Api(app)


SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint)

database.init_app(app)
with app.app_context():
    database.create_all()

# Adding routes
api.add_resource(PersonList, "/person/<int:page_size>/<int:page_number>")
api.add_resource(PersonAdd, "/person/")
api.add_resource(PersonGet, "/person/<int:id>")
api.add_resource(PersonRemove, "/person/<int:id>")
api.add_resource(PersonUpdate, "/person/<int:id>")
api.add_resource(PersonFilter, "/person/filter/<int:age>")

api.add_resource(ProjectList, "/project/<int:page_size>/<int:page_number>")
api.add_resource(ProjectGet, "/project/<int:id>")
api.add_resource(ProjectAdd, "/project/")
api.add_resource(ProjectRemove, "/project/<int:id>")
api.add_resource(ProjectUpdate, "/project/<int:id>")
api.add_resource(ProjectTodoBulk, "/project/<int:id>/todo")

api.add_resource(ProjectPersonList, "/project-person/<int:page_size>/<int:page_number>")
api.add_resource(ProjectPersonGet, "/project-person/<int:id>")
api.add_resource(ProjectPersonAdd, "/project-person/")
api.add_resource(ProjectPersonRemove, "/project-person/<int:id>")
api.add_resource(ProjectPersonUpdate, "/project-person/<int:id>")

api.add_resource(TodoList, "/todo/<int:page_size>/<int:page_number>")
api.add_resource(TodoAdd, "/todo/")
api.add_resource(TodoGet, "/todo/<int:id>")
api.add_resource(TodoRemove, "/todo/<int:id>")
api.add_resource(TodoUpdate, "/todo/<int:id>")

api.add_resource(TodoPriorityReport,
                 "/report/projects-by-done-todos")
api.add_resource(TodoEndDateReport,
                 "/report/todo-by-end-date/<string:end_date>")

if __name__ == "__main__":
    app.run(debug=True)
