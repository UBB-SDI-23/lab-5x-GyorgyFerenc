from app import app
from random import randint
from controller.controller import controller


def filter_test():
    def filter_aux(age):
        persons = controller.filter_person_by_age(age)
        for person in persons:
            if person.age <= age:
                assert False

    filter_aux(1)
    filter_aux(20)
    filter_aux(10)
    filter_aux(5)
    filter_aux(6)

    for _ in range(10):
        age = randint(1, 100)
        filter_aux(age)


def report_test():
    projects = controller.report_projects_by_number_of_done_todos()
    before_nr = 0
    for project in projects:
        number = project['number_of_done_todos']
        if before_nr > number:
            assert False, "Number should be increasing"

        before_nr = number


def run_test():
    filter_test()
    report_test()


if __name__ == "__main__":
    with app.app_context():
        run_test()
