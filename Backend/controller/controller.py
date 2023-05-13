from model.database_models import *
from flask_sqlalchemy import SQLAlchemy
from repository.database import database


class Controller:

    def get_all_persons(self,page_size,page_number) -> list[Person]:
        return self.__get_all(Person,page_size,page_number)

    def get_all_projects(self,page_size,page_number) -> list[Project]:
        return self.__get_all(Project,page_size,page_number)

    def get_all_todos(self,page_size,page_number) -> list[Todo]:
        return self.__get_all(Todo,page_size,page_number)

    def get_all_project_persons(self,page_size,page_number) -> list[Todo]:
        return self.__get_all(ProjectPerson,page_size,page_number)

    def get_person(self, id: int) -> Person:
        return self.__get(Person, id)

    def get_project(self, id: int) -> Project:
        return self.__get(Project, id)

    def get_todo(self, id: int) -> Todo:
        return self.__get(Todo, id)

    def get_project_person(self, id: int) -> ProjectPerson:
        return self.__get(ProjectPerson, id)

    def add_person(self, person: dict) -> int:
        """
            Adds the person to the database and returns the id
        """
        person = self.__create_person_from_dictionary(person)
        return self.__add(person)

    def add_project(self, project: dict) -> int:
        project = Project(name=project["name"],
                          description=project["description"],
                          start_date=project["start_date"],
                          end_date=project["end_date"],
                          priority_level=project["priority_level"],)
        return self.__add(project)

    def add_todo(self, todo: dict) -> int:
        todo_entity = self.__create_todo_from_dictionary(todo)
        return self.__add(todo_entity)

    def add_project_person(self, project_person: dict) -> int:
        project_person = self.__create_project_person_from_dictionary(
            project_person)
        return self.__add(project_person)

    def remove_person(self, id: int):
        self.__remove(Person, id)

    def remove_todo(self, id: int):
        self.__remove(Todo, id)

    def remove_project(self, id: int):
        self.__remove(Project, id)
        
    def remove_project_person(self, id: int):
        self.__remove(ProjectPerson, id)

    def update_person(self, id, person: dict):
        self.__update(Person, id,  person)

    def update_todo(self, id, todo: dict):
        self.__update(Todo, id,  todo)

    def update_project(self, id, project: dict):
        self.__update(Project, id, project)

    def filter_person_by_age(self, age) -> list[Person]:
        select = database.select(Person).where(Person.age > age)
        result = database.session.execute(select).all()
        return self.__create_list_from_result(result)

    def report_projects_by_number_of_done_todos(self):
        count = database.func.count
        select = database.select(Project, count(Todo.id)).join(Todo).where(Todo.done) \
            .group_by(Project) \
            .order_by(count(Todo.id))
        result = database.session.execute(select).all()
        list = self.__create_list_from_result(result)
        list_json = TodoSchema(many=True).dump(list)

        for i in range(0, len(list)):
            list_json[i]['number_of_done_todos'] = result[i][1]

        return list_json

    def report_todos_by_project_end_date(self, end_date) -> list[Todo]:
        select = database.select(Todo) \
                         .join(Project) \
                         .where(end_date == Project.end_date)
        result = database.session.execute(select).all()
        return self.__create_list_from_result(result)

    def __get_all(self, type,page_size:int, page_number:int) -> list:
        offset = page_size * page_number
        select = database.select(type).offset(offset).limit(page_size)
        result = database.session.execute(select).all()
        items = self.__create_list_from_result(result)
        return items

    def __get(self, type, id: int):
        item = database.get_or_404(type, id)
        return item

    def __remove(self, type, id):
        delete = database.delete(type).where(type.id == id)
        database.session.execute(delete)
        database.session.commit()

    def __add(self, entity):
        database.session.add(entity)
        database.session.commit()
        return entity.id

    def __update(self, type, id,  entity):
        update = database.update(type).where(type.id == id).values(entity)
        database.session.execute(update)
        database.session.commit()

    def __create_list_from_result(self, person_result):
        persons = [r[0] for r in person_result]
        return persons

    def __create_person_from_dictionary(self, person) -> Person:
        first_name = person["first_name"]
        last_name = person["last_name"]
        cnp = person["cnp"]
        gender = person["gender"]
        age = person["age"]
        person = Person(first_name=first_name, last_name=last_name,
                        cnp=cnp, gender=gender, age=age)

        return person

    def __create_todo_from_dictionary(self, todo) -> Todo:
        name = todo["name"]
        description = todo["description"]
        deadline = todo["deadline"]
        done = todo["done"]
        project_id = todo["project_id"]
        todo = Todo(name=name, description=description,
                    deadline=deadline, done=done, project_id=project_id)
        return todo

    def __create_project_person_from_dictionary(self, project_person) -> Todo:
        person_id = project_person["person_id"]
        role = project_person["role"]
        date = project_person["date"]
        project_id = project_person["project_id"]
        project_person = ProjectPerson(person_id=person_id, role=role,
                                       date=date, project_id=project_id)
        return project_person


controller = Controller()
