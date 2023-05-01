import { getPersons, getProjectPersons, getProjects, getTodos } from "./backend.js";

export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    let data = {
        persons: getPersons(),
        projects: getProjects(),
        todos: getTodos(),
        project_persons: getProjectPersons(),
    };

    return data;
}

