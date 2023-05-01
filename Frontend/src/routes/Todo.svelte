<script>
    import { addTodo, getTodos, removeTodo, updateTodo } from "./backend.js";

    export let data;

    /**
     * @type {import('./backend').Todo[]}
     */
    let todos = data.todos;

    let choosen = todos[0];

    if (todos.length == 0) {
        choosen = {
            id: -1,
            name: "",
            description: "",
            deadline: "",
            done: false,
            project_id: -1,
        };
    }

    /**
     * @param {import('./backend').Todo} project
     */
    function projectClicked(project) {
        choosen = project;
    }
    async function update() {
        await updateTodo(choosen);
        todos = await getTodos();
    }
    async function add() {
        choosen.id = await addTodo(choosen);
        console.log(choosen);
        todos = await getTodos();
    }
    async function remove() {
        await removeTodo(choosen);
        todos = await getTodos();
    }
</script>

<section>
    <div class="project-inspector">
        <input bind:value={choosen.name} />
        <input bind:value={choosen.description} />
        <input bind:value={choosen.deadline} />
        <input bind:value={choosen.done} />
        <input bind:value={choosen.project_id} />

        <button class="btn btn-light" on:click={add}> add </button>
        <button class="btn btn-light" on:click={update}> update </button>
        <button class="btn btn-light" on:click={remove}> remove </button>
        <button
            class="btn btn-light"
            on:click={async () => {
                todos = await getTodos();
            }}
        >
            refresh
        </button>
    </div>
    <table>
        <tr class="Description">
            <th> Name </th>
            <th> Description </th>
            <th> Start Date </th>
            <th> End Date </th>
            <th> Priority Level</th>
        </tr>
        {#each todos as project}
            <tr on:click={() => projectClicked(project)}>
                <th>{project.name}</th>
                <th>{project.description} </th>
                <th>{project.deadline}</th>
                <th>{project.done}</th>
                <th>{project.project_id}</th>
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
</style>
