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

    if (persons.length == 0) {
        choosen = {
            id: 1,
            first_name: "",
            last_name: "",
            age: 0,
            cnp: "",
            gender: "male",
        };
    }

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
        if (!validate_person(choosen)) return;
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

    const ErrorState = {
        none: 0,
        cnp: 1,
        gender: 2,
        age: 3,
    };

    let error_state = ErrorState.none;

    /**
     * @param {import('./backend').Person} person
     */
    function validate_person(person) {
        if (person.cnp.length != 13) {
            error_state = ErrorState.cnp;
            return false;
        }

        if (!["male", "female"].includes(person.gender)) {
            error_state = ErrorState.gender;
            return false;
        }

        if (person.age <= 0 || person.age > 120) {
            error_state = ErrorState.age;
            return false;
        }
        error_state = ErrorState.none;
        return true;
    }
</script>

<section>
    <div class="person-inspector">
        <input bind:value={choosen.first_name} />
        <input bind:value={choosen.last_name} />
        <input bind:value={choosen.cnp} />
        <input bind:value={choosen.gender} />
        <input bind:value={choosen.age} />
        {#if error_state == ErrorState.age}
            Error: age is not in range (0, 120]
        {:else if error_state == ErrorState.gender}
            Error: gender must be male or female
        {:else if error_state == ErrorState.cnp}
            Error: cnp must have a length of 13
        {/if}
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
    .hide {
        display: none;
    }
</style>
