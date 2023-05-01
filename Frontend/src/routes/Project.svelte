<script>
    import {
        addPerson,
        addProject,
        addProjectPerson,
        getProjects,
        removeProject,
        updateProject,
    } from "./backend.js";

    export let data;

    /**
     * @type {import('./backend').Project[]}
     */
    let projects = data.projects;

    let choosen = projects[0];

    if (projects.length == 0) {
        choosen = {
            id: -1,
            name: "",
            description: "",
            start_date: "",
            end_date: "",
            priority_level: 1,
        };
    }

    /**
     * @param {import('./backend').Project} project
     */
    function projectClicked(project) {
        choosen = project;
    }

    async function update() {
        await updateProject(choosen);
        projects = await getProjects();
    }
    async function add() {
        choosen.id = await addProject(choosen);
        projects = await getProjects();

        for (let wrapper of wrappers) {
            wrapper.person.id = await addPerson(wrapper.person);
            wrapper.project_person.person_id = wrapper.person.id;
            wrapper.project_person.project_id = choosen.id;
            addProjectPerson(wrapper.project_person);
        }
    }
    async function remove() {
        await removeProject(choosen);
        projects = await getProjects();
    }

    /**
     * @typedef Wrapper
     * @type {object}
     * @property {import('./backend').Person} person
     * @property {import('./backend').ProjectPerson} project_person
     */

    /**
     * @type {Wrapper[]}
     */
    let wrappers = [];
</script>

<section>
    <div class="project-inspector">
        <div class="item">Name <input bind:value={choosen.name} /></div>
        <div class="item">
            Description <input bind:value={choosen.description} />
        </div>
        <div class="item">
            Start Date<input bind:value={choosen.start_date} />
        </div>
        <div class="item">End Date<input bind:value={choosen.end_date} /></div>
        <div class="item">
            Priority Level<input bind:value={choosen.priority_level} />
        </div>

        <button class="btn btn-light" on:click={add}> add </button>
        <button class="btn btn-light" on:click={update}> update </button>
        <button class="btn btn-light" on:click={remove}> remove </button>
        <button
            class="btn btn-light"
            on:click={async () => {
                projects = await getProjects();
            }}
        >
            refresh
        </button>
        <button
            class="btn btn-light"
            on:click={() => {
                wrappers.push({
                    person: {
                        id: -1,
                        first_name: "",
                        last_name: "",
                        age: 0,
                        cnp: "",
                        gender: "male",
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
            add person
        </button>
    </div>
    {#each wrappers as wrapper}
        Project <br />
        <div class="item">
            First Name<input bind:value={wrapper.person.first_name} />
        </div>
        <div class="item">
            Last Name<input bind:value={wrapper.person.last_name} />
        </div>
        <div class="item">
            Age<input bind:value={wrapper.person.age} />
        </div>
        <div class="item">
            CNP<input bind:value={wrapper.person.cnp} />
        </div>
        <div class="item">
            Gender<input bind:value={wrapper.person.gender} />
        </div>
        <div class="item">
            Role <input bind:value={wrapper.project_person.role} />
        </div>
        <div class="item">
            Date <input bind:value={wrapper.project_person.date} />
        </div>
    {/each}

    <table>
        <tr class="Description">
            <th> Name </th>
            <th> Description </th>
            <th> Start Date </th>
            <th> End Date </th>
            <th> Priority Level</th>
        </tr>
        {#each projects as project}
            <tr on:click={() => projectClicked(project)}>
                <th>{project.name}</th>
                <th>{project.description} </th>
                <th>{project.start_date}</th>
                <th>{project.end_date}</th>
                <th>{project.priority_level}</th>
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
    .project-inspector {
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
