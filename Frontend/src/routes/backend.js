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

// const link = "https://flask-api-381710.lm.r.appspot.com"
const link = "http://127.0.0.1:5000"

/**
 * @returns {Promise<Person[]>}
 */
export async function getPersons() {
    let p = await fetch(
        `${link}/person/`
    );

    let text = await p.text();
    let ob = JSON.parse(text);
    console.log(ob);

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
    console.log(raw);

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
    console.log(raw);

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
    console.log(raw);

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

