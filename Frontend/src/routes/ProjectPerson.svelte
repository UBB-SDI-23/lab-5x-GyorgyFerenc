<script>
    import {
        addProjectPerson,
        getProjectPersons,
        removeProjectPerson,
        updateProjectPerson,
    } from "./backend.js";

    export let data;

    /**
     * @type {import('./backend').ProjectPerson[]}
     */
    let person_projects = data.project_persons;

    let choosen = person_projects[0];

    if (person_projects.length == 0) {
        choosen = {
            id: -1,
            project_id: -1,
            person_id: -1,
            role: "",
            date: "",
        };
    }

    /**
     * @param {import('./backend').ProjectPerson} project_person
     */
    function projectClicked(project_person) {
        choosen = project_person;
    }
    async function update() {
        await updateProjectPerson(choosen);
        person_projects = await getProjectPersons();
    }
    async function add() {
        choosen.id = await addProjectPerson(choosen);
        person_projects = await getProjectPersons();
    }
    async function remove() {
        await removeProjectPerson(choosen);
        person_projects = await getProjectPersons();
    }
</script>

<section>
    <div class="project_person-inspector">
        <input bind:value={choosen.project_id} />
        <input bind:value={choosen.person_id} />
        <input bind:value={choosen.role} />
        <input bind:value={choosen.date} />

        <button class="btn btn-light" on:click={add}> add </button>
        <button class="btn btn-light" on:click={update}> update </button>
        <button class="btn btn-light" on:click={remove}> remove </button>
        <button
            class="btn btn-light"
            on:click={async () => {
                person_projects = await getProjectPersons();
            }}
        >
            refresh
        </button>
    </div>
    <table>
        <tr class="Description">
            <th> Project ID </th>
            <th> Person ID </th>
            <th> Role </th>
            <th> Date </th>
        </tr>
        {#each person_projects as project_person}
            <tr on:click={() => projectClicked(project_person)}>
                <th>{project_person.project_id}</th>
                <th>{project_person.person_id} </th>
                <th>{project_person.role}</th>
                <th>{project_person.date}</th>
            </tr>
        {/each}
    </table>
</section>

<style>
    section {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    table {
        border-collapse: collapse;
        border: 1px solid;
    }
    tr:hover:not(.Description) {
        background-color: lightblue;
    }
    th {
        padding-right: 10px;
    }
    .Description {
        border-bottom: 1px solid black;
    }
    .project_person-inspector {
        width: fit-content;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
