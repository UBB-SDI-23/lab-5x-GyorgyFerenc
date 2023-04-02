<script>
    import {
        filterPerson,
        getPerson,
        getPersons,
        updatePerson,
    } from "./backend.js";
    import { onMount } from "svelte";

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

    function update() {
        updatePerson(choosen);
        getPersons().then((per) => {
            persons = per;
        });
    }
</script>

<section>
    <div class="person-inspector">
        <input bind:value={choosen.first_name} />
        <input bind:value={choosen.last_name} />
        <input bind:value={choosen.cnp} />
        <input bind:value={choosen.gender} />
        <input bind:value={choosen.age} />
        <button on:click={update}> update </button>
    </div>
    <input bind:value={age} />
    <table>
        <tr class="Description">
            <th> First Name </th>
            <th> Last Name </th>
            <th> CNP </th>
            <th> Gender </th>
            <th> Age </th>
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
    table {
        border-collapse: collapse;
        border: 1px solid;
    }
    tr:hover {
        background-color: blue;
    }
    th {
        padding-right: 10px;
    }
    .Description {
        border-bottom: 1px solid black;
    }
</style>
