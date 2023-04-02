<script>
    import { onMount } from "svelte";

    let alma = "alma";

    async function getPersons() {
        let p = await fetch(
            "https://flask-api-381710.lm.r.appspot.com/person/"
        );

        return p.json();
    }

    let persons = "";

    onMount(async () => {
        let j = await getPersons();
        persons = j.toString();
        console.log(persons);
    });
</script>

<section>
    asd {persons}
</section>
