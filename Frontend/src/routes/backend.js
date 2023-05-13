/**
 * @typedef Person
 * @type {object}
 * @property {number} id
 * @property {string} first_name
 * @property {string} last_name
 * @property {string} cnp
 * @property {string} gender
 * @property {number} age
 */

/**
 * @typedef Project
 * @type {object}
 * @property {number} id
 * @property {string} name
 * @property {string} description
 * @property {string} start_date
 * @property {string} end_date
 * @property {number} priority_level
 */

/**
 * @typedef Todo
 * @type {object}
 * @property {number} id
 * @property {string} name
 * @property {string} description
 * @property {string} deadline
 * @property {boolean} done
 * @property {number} project_id
 */

/**
 * @typedef ProjectPerson
 * @type {object}
 * @property {number} id
 * @property {number} project_id
 * @property {number} person_id
 * @property {string} role
 * @property {string} date
 */

//const link = "https://flask-api-381710.lm.r.appspot.com"
const link = "http://127.0.0.1:5000"

/**
    * @param {number} page_size,
    * @param {number} page_number,
 * @returns {Promise<Person[]>}
 */
export async function getPersons(page_size, page_number) {
    let p = await fetch(`${link}/person/${page_size}/${page_number}`);

    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["persons"];
}


/**
 * @param {number} id
 * @return {Promise<Person>}
*/
export async function getPerson(id) {
    let p = await fetch(
        `${link}/person/${id}`
    );

    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["person"];
}

/**
 * @param {number} age
 * @return {Promise<Person[]>}
*/
export async function filterPerson(age) {
    let p = await fetch(
        `${link}/person/filter/${age}`
    );

    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["persons"];
}

/**
 * @param {Person} person
*/
export async function updatePerson(person) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(person);

    var requestOptions = {
        method: 'PATCH',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/person/${person.id}`, requestOptions)
        .catch(error => console.log('error', error));
}


/**
 * @param {Person} person
*/
export async function removePerson(person) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(person);

    var requestOptions = {
        method: 'DELETE',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/person/${person.id}`, requestOptions)
        .catch(error => console.log('error', error));
}


/**
 * @param {Person} person
 * @returns {Promise<number>}
*/
export async function addPerson(person) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(person);

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
    };

    let p = await fetch(`${link}/person/`, requestOptions)
    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["id"];
}


/**
    * @param {number} page_size
    * @param {number} page_number
 * @returns {Promise<Project[]>}
 */
export async function getProjects(page_size, page_number) {
    let p = await fetch(
        `${link}/project/${page_size}/${page_number}`
    );

    let text = await p.text();
    let ob = JSON.parse(text);
    return ob;
}


/**
 * @param {Project} project
 * @returns {Promise<number>}
*/
export async function addProject(project) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(project);

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
    };

    let p = await fetch(`${link}/project/`, requestOptions)
    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["id"];

}

/**
 * @param {Project} project
*/
export async function removeProject(project) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(project);

    var requestOptions = {
        method: 'DELETE',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/project/${project.id}`, requestOptions)
        .catch(error => console.log('error', error));
}

/**
 * @param {Project} project
*/
export async function updateProject(project) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(project);

    var requestOptions = {
        method: 'PATCH',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/project/${project.id}`, requestOptions)
        .catch(error => console.log('error', error));
}

/**
    * @param {number} page_size
    * @param {number} page_number
 * @returns {Promise<Todo[]>}
 */
export async function getTodos(page_size, page_number) {
    let p = await fetch(
        `${link}/todo/${page_size}/${page_number}`
    );

    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["todos"];
}

/**
 * @param {Todo} todo
 * @returns {Promise<number>}
*/
export async function addTodo(todo) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(todo);
    console.log(raw);

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
    };

    let p = await fetch(`${link}/todo/`, requestOptions)
    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["id"];
}

/**
 * @param {Todo} todo
*/
export async function removeTodo(todo) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(todo);
    console.log(raw);

    var requestOptions = {
        method: 'DELETE',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/todo/${todo.id}`, requestOptions)
        .catch(error => console.log('error', error));
}

/**
 * @param {Todo} todo
*/
export async function updateTodo(todo) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(todo);
    console.log(raw);

    var requestOptions = {
        method: 'PATCH',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/todo/${todo.id}`, requestOptions)
        .catch(error => console.log('error', error));
}

/**
 * @param {ProjectPerson} project_person
 * @returns {Promise<number>}
*/
export async function addProjectPerson(project_person) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(project_person);
    console.log(raw);

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
    };

    let p = await fetch(`${link}/project-person/`, requestOptions)
    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["id"];
}

/**
    * @param {number} page_size
    * @param {number} page_number
 * @returns {Promise<ProjectPerson[]>}
 */
export async function getProjectPersons(page_size, page_number) {
    let p = await fetch(
        `${link}/project-person/${page_size}/${page_number}`
    );

    let text = await p.text();
    let ob = JSON.parse(text);

    // console.log(ob);

    return ob;
}

/**
 * @param {ProjectPerson} project_person
*/
export async function removeProjectPerson(project_person) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(project_person);
    console.log(raw);

    var requestOptions = {
        method: 'DELETE',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/project-person/${project_person.id}`, requestOptions)
        .catch(error => console.log('error', error));
}

/**
 * @param {ProjectPerson} project_person
*/
export async function updateProjectPerson(project_person) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(project_person);
    console.log(raw);

    var requestOptions = {
        method: 'PATCH',
        headers: myHeaders,
        body: raw,
    };

    return fetch(`${link}/project-person/${project_person.id}`, requestOptions)
        .catch(error => console.log('error', error));
}
