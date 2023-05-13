<script>
    import Person from "./Person.svelte";
    import Project from "./Project.svelte";
    import ProjectPerson from "./ProjectPerson.svelte";
    import Todo from "./Todo.svelte";

    export let data;

    const Page = {
        Person: 1,
        Project: 2,
        Todo: 3,
        ProjectPerson: 4,
    };

    let page = Page.Person;
</script>

<section>
    <div class="menu">
        <button class="btn btn-light" on:click={() => (page = Page.Person)}>
            Person
        </button>
        <button class="btn btn-light" on:click={() => (page = Page.Project)}>
            Project
        </button>
        <button class="btn btn-light" on:click={() => (page = Page.Todo)}>
            Todo
        </button>
        <button
            class="btn btn-light"
            on:click={() => (page = Page.ProjectPerson)}
        >
            Project Person
        </button>
    </div>

    {#if page == Page.Person}
        <Person {data} />
    {:else if page == Page.Project}
        <Project {data} />
    {:else if page == Page.Todo}
        <Todo {data} />
    {:else if page == Page.ProjectPerson}
        <ProjectPerson {data} />
    {/if}
</section>

<style>
    .menu {
        display: flex;
        justify-content: center;
        /* flex-direction: column; */
        align-items: center;
        margin-bottom: 10px;
    }
    button {
        width: 100px;
    }
</style>
