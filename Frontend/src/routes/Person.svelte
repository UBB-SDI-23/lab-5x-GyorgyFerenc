<script>
    import {
        addPerson,
        addProject,
        addProjectPerson,
        filterPerson,
        getPersons,
        removePerson,
        updatePerson,
    } from "./backend.js";

    export let data;

    const page_size = 10;
    let page_number = 0;

    /**
     * @type {import('./backend').Person[]}
     */
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
            id: -1,
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
        if (!validate_person(choosen)) return;
        await updatePerson(choosen);
        persons = await getPersons(page_size, page_number);
    }
    async function add() {
        if (!validate_person(choosen)) return;
        choosen.id = await addPerson(choosen);
        persons = await getPersons(page_size, page_number);

        for (let wrapper of wrappers) {
            wrapper.project.id = await addProject(wrapper.project);
            wrapper.project_person.project_id = wrapper.project.id;
            wrapper.project_person.person_id = choosen.id;
            addProjectPerson(wrapper.project_person);
        }
    }
    async function remove() {
        await removePerson(choosen);
        persons = await getPersons(page_size, page_number);
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

    /**
     * @typedef Wrapper
     * @type {object}
     * @property {import('./backend').Project} project
     * @property {import('./backend').ProjectPerson} project_person
     */

    /**
     * @type {Wrapper[]}
     */
    let wrappers = [];
</script>

<section>
    <div class="person-inspector">
        <div class="item">
            First Name <input bind:value={choosen.first_name} />
        </div>
        <div class="item">
            Last Name <input bind:value={choosen.last_name} />
        </div>
        <div class="item">CNP <input bind:value={choosen.cnp} /></div>
        <div class="item">Gender <input bind:value={choosen.gender} /></div>
        <div class="item">Age <input bind:value={choosen.age} /></div>

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
        <button
            class="btn btn-light"
            on:click={async () => {
                persons = await getPersons(page_size, page_number);
            }}
        >
            refresh
        </button>
        <button
            class="btn btn-light"
            on:click={() => {
                wrappers.push({
                    project: {
                        id: -1,
                        name: "",
                        description: "",
                        start_date: "",
                        end_date: "",
                        priority_level: 1,
                    },
                    project_person: {
                        id: -1,
                        person_id: -1,
                        project_id: -1,
                        role: "",
                        date: "",
                    },
                });
                wrappers = wrappers;
            }}
        >
            add project
        </button>
    </div>

    {#each wrappers as wrapper}
        Project <br />
        <div class="item">Name<input bind:value={wrapper.project.name} /></div>
        <div class="item">
            Description<input bind:value={wrapper.project.description} />
        </div>
        <div class="item">
            Start Date<input bind:value={wrapper.project.start_date} />
        </div>
        <div class="item">
            End Date<input bind:value={wrapper.project.end_date} />
        </div>
        <div class="item">
            Priority Level<input bind:value={wrapper.project.priority_level} />
        </div>
        <div class="item">
            Role <input bind:value={wrapper.project_person.role} />
        </div>
        <div class="item">
            Date <input bind:value={wrapper.project_person.date} />
        </div>
    {/each}

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
    .item {
        display: flex;
        justify-content: space-between;
        width: 300px;
    }
</style>
