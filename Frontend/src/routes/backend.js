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
 * @returns {Promise<Person[]>}
 */
export async function getPersons() {
    let p = await fetch(
        "https://flask-api-381710.lm.r.appspot.com/person/"
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
        `https://flask-api-381710.lm.r.appspot.com/person/${id}`
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
        `https://flask-api-381710.lm.r.appspot.com/person/filter/${age}`
    );

    let text = await p.text();
    let ob = JSON.parse(text);

    return ob["persons"];
}

/**
 * @param {Person} person
*/
export async function updatePerson(person) {
    // let p = await fetch(
    //     `https://flask-api-381710.lm.r.appspot.com/person/${person.id}`, {
    //     method: 'PATCH',
    //     body: JSON.stringify(person),
    //     headers: {
    //         'Content-type': 'application/json',
    //     },
    // }
    // );
    // console.log(p);

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(person);

    var requestOptions = {
        method: 'PATCH',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(`https://flask-api-381710.lm.r.appspot.com/person/${person.id}`, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}

