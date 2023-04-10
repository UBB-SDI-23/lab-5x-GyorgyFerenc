import { getPersons, getPerson } from "./backend.js";

export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    let data = {
        persons: [getPerson(2)],
    };

    return data;
}

