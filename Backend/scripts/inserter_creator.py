import sys
import logging
from faker import Faker
from faker.providers import BaseProvider
from random import choice, randrange
from data import greeknames, jobs, verbs, nouns


class CNPProvider(BaseProvider):
    def cnp(self) -> str:
        s = choice(['5', '6'])
        aa = f"{randrange(0, 99):02d}"
        ll = f"{randrange(0, 12):02d}"
        zz = f"{randrange(0, 28):02d}"
        jj = f"{randrange(0, 48):02d}"
        nnn = f"{randrange(0, 999):03d}"
        c = f"{randrange(0, 9)}"

        return s + aa + ll + zz + jj + nnn + c


class ProjectNameProvider(BaseProvider):
    def project_name(self) -> str:
        return "Project " + choice(greeknames)


class RoleProvider(BaseProvider):
    def role(self) -> str:
        return choice(jobs)


class TodoProvider(BaseProvider):
    def todo(self) -> str:
        return choice(verbs) + " the " + choice(nouns)


fake = Faker()
fake.add_provider(CNPProvider)
fake.add_provider(ProjectNameProvider)
fake.add_provider(RoleProvider)
fake.add_provider(TodoProvider)


def sourind_with_qoutes(a):
    return f"\"{a}\""


person_id = 1


def person_insert():
    global person_id
    id = person_id
    person_id += 1
    first_name = fake.first_name()
    first_name = sourind_with_qoutes(first_name)

    last_name = fake.last_name()
    last_name = sourind_with_qoutes(last_name)

    cnp = fake.cnp()
    cnp = sourind_with_qoutes(cnp)

    gender = choice(['male', 'female'])
    gender = sourind_with_qoutes(gender)

    age = randrange(1, 100)

    return f"({id},{first_name},{last_name},{cnp},{gender},{age})"


project_id = 1


def project_insert():
    global project_id
    id = project_id
    project_id += 1

    name = fake.project_name()
    name = sourind_with_qoutes(name)

    description = fake.text(max_nb_chars=50)
    description = sourind_with_qoutes(description)

    date1 = fake.date_time()
    date2 = fake.date_time()
    if date1 > date2:
        temp = date1
        date1 = date2
        date2 = temp

    start_date = date1.strftime("%Y-%m-%d")
    end_date = date2.strftime("%Y-%m-%d")

    start_date = sourind_with_qoutes(start_date)
    end_date = sourind_with_qoutes(end_date)

    priority_level = randrange(1, 10)

    return f"({id},{name},{description},{start_date},{end_date},{priority_level})"


project_person_id = 1

used_person_id = 1
used_project_id = 1


def project_person_insert():
    global project_person_id
    id = project_person_id
    project_person_id += 1

    global used_person_id
    global person_id
    global used_project_id

    _person_id = used_person_id
    _project_id = used_project_id

    used_person_id += 1
    if used_person_id >= person_id:
        used_person_id = 1
        used_project_id += 1

    role = fake.role()
    role = sourind_with_qoutes(role)

    date = fake.date()
    date = sourind_with_qoutes(date)

    return f"({id},{_project_id},{_person_id},{role},{date})"


todo_id = 1

todo_used_project_id = 1


def todo_insert():
    global todo_id
    id = todo_id
    todo_id += 1

    global todo_used_project_id
    global project_id

    _project_id = todo_used_project_id

    todo_used_project_id += choice([0, 0, 0, 0, 1])
    if todo_used_project_id >= project_id:
        todo_used_project_id = 1

    name = fake.todo()
    description = name + " duh"
    name = sourind_with_qoutes(name)
    description = sourind_with_qoutes(description)

    deadline = fake.date()
    deadline = sourind_with_qoutes(deadline)

    done = choice(['true', 'false'])

    return f"({id},{name},{description},{deadline},{done},{_project_id})"


NR_INSERT = 1_000_000
NR_INSERT_MANY = 10_000_000
BATCH_SIZE = 1000

to_be_executed = "use flask_api;\n"

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


for i in range(int(NR_INSERT/BATCH_SIZE)):
    insert = "insert into person values"
    for j in range(BATCH_SIZE-1):
        insert += person_insert() + ","
    insert += person_insert() + ";"
    to_be_executed += insert + "\n"

logging.debug('generation is done for person')


for i in range(int(NR_INSERT/BATCH_SIZE)):
    insert = "insert into project values"
    for j in range(BATCH_SIZE-1):
        insert += project_insert() + ","
    insert += project_insert() + ";"
    to_be_executed += insert + "\n"

logging.debug('generation is done for project')


for i in range(int(NR_INSERT_MANY/BATCH_SIZE)):
    insert = "insert into project_person values"
    for j in range(BATCH_SIZE-1):
        insert += project_person_insert() + ","
    insert += project_person_insert() + ";"
    to_be_executed += insert + "\n"

logging.debug('generation is done for project_person')


for i in range(int(NR_INSERT/BATCH_SIZE)):
    insert = "insert into todo values"
    for j in range(BATCH_SIZE-1):
        insert += todo_insert() + ","
    insert += todo_insert() + ";"
    to_be_executed += insert + "\n"

logging.debug('generation is done for todo')
logging.debug('started writing')

with open("insert_million.sql", "w") as f:
    f.write(to_be_executed)

logging.debug('end of  writing')
