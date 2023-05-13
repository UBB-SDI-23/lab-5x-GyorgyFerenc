import { getPersons, getProjectPersons, getProjects, getTodos } from "./backend.js";

export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    let data = {
        persons: getPersons(10, 0),
        projects: getProjects(10, 0),
        todos: getTodos(10, 0),
        project_persons: getProjectPersons(10, 0),
    };

    return data;
}

