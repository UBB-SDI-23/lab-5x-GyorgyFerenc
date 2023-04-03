<script>
    import {
        addPerson,
        filterPerson,
        getPerson,
        getPersons,
        removePerson,
        updatePerson,
    } from "./backend.js";

    export let data;
    let persons = data.persons;
    let age = 0;
    $: {
        if (age > 0) {
            filterPerson(age).then((per) => {
                persons = per;
            });
        }
    }

    let choosen = persons[0];

    /**
     * @param {import('./backend').Person} person
     */
    function personClicked(person) {
        choosen = person;
    }

    async function update() {
        await updatePerson(choosen);
        persons = await getPersons();
    }
    async function add() {
        choosen.id = await addPerson(choosen);
        console.log(choosen);
        persons = await getPersons();
    }
    async function remove() {
        await removePerson(choosen);
        persons = await getPersons();
    }

    let sort_icon = "v";

    function sortAge() {
        if (sort_icon == "v") {
            sortByAgeAscending();
            sort_icon = "^";
        } else if (sort_icon == "^") {
            sortByAgeDescending();
            sort_icon = "v";
        }
    }

    function sortByAgeAscending() {
        persons.sort((a, b) => a.age - b.age);
        persons = persons;
    }
    function sortByAgeDescending() {
        persons.sort((a, b) => b.age - a.age);
        persons = persons;
    }
</script>

<section>
    <div class="person-inspector">
        <input bind:value={choosen.first_name} />
        <input bind:value={choosen.last_name} />
        <input bind:value={choosen.cnp} />
        <input bind:value={choosen.gender} />
        <input bind:value={choosen.age} />
        <button class="btn btn-light" on:click={add}> add </button>
        <button class="btn btn-light" on:click={update}> update </button>
        <button class="btn btn-light" on:click={remove}> remove </button>
    </div>
    <div>
        age:
        <input bind:value={age} />
    </div>
    <table>
        <tr class="Description">
            <th> First Name </th>
            <th> Last Name </th>
            <th> CNP </th>
            <th> Gender </th>
            <th>
                Age <button on:click={sortAge} class="sort btn btn-light"
                    >{sort_icon}</button
                ></th
            >
        </tr>
        {#each persons as person}
            <tr on:click={() => personClicked(person)}>
                <th>{person.first_name}</th>
                <th>{person.last_name} </th>
                <th>{person.cnp}</th>
                <th>{person.gender}</th>
                <th>{person.age}</th>
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
    .person-inspector {
        width: fit-content;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
