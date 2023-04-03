from repository.database import database
from sqlalchemy import ForeignKey
from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()


class Person(database.Model):
    """
        Person = {
            "id": int
            "first_name": str
            "last_name" : str
            "cnp" : str
            "gender": str
            "age": int
        }
    """
    id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(100))
    last_name = database.Column(database.String(100))
    cnp = database.Column(database.String(100))
    gender = database.Column(database.String(100))
    age = database.Column(database.Integer)


class PersonSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Person


class Project(database.Model):
    """
        Project = {
            "id" : int
            "name": str
            "description" : str
            "start_date" : str
            "end_date" : str
            "priority_level": int
    }
    """
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    description = database.Column(database.String(100))
    start_date = database.Column(database.String(100))
    end_date = database.Column(database.String(100))
    priority_level = database.Column(database.Integer)


class ProjectSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Project


class ProjectPerson(database.Model):
    """
        ProjectPerson = {
            "id" : int
            "project_id": int
            "person_id" : int
            "role": str
            "date" : str
        }
    """
    id = database.Column(database.Integer, primary_key=True)
    project_id = database.Column(database.Integer, ForeignKey(Project.id))
    person_id = database.Column(database.Integer, ForeignKey(Person.id))
    role = database.Column(database.String(100))
    date = database.Column(database.String(100))


class ProjectPersonSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = ProjectPerson


class Todo(database.Model):
    """
        Todo = {
            "id" : int
            "name" : str
            "description" : str
            "deadline" : str
            "done" : boolean
            "project_id" : int
        }
    """
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    description = database.Column(database.String(100))
    deadline = database.Column(database.String(100))
    done = database.Column(database.Boolean)
    project_id = database.Column(database.Integer, ForeignKey(Project.id))


class TodoSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = Todo


Project.todos = database.relationship(Todo)

Project.persons = database.relationship(
    Person, secondary='project_person', backref='projects')


class ProjectWithRelationsSchema(marshmallow.SQLAlchemyAutoSchema):
    todos = marshmallow.Nested(TodoSchema, many=True)
    persons = marshmallow.Nested(PersonSchema, many=True)

    class Meta:
        model = Project


class PersonWithRelationsSchema(marshmallow.SQLAlchemyAutoSchema):
    projects = marshmallow.Nested(ProjectSchema, many=True)

    class Meta:
        model = Person
