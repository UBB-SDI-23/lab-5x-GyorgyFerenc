import { getPersons } from "./backend.js";

export const ssr = false;

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    let data = {
        persons: getPersons(),
    };

    return data;
}

