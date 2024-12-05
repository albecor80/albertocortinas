<script>
	import Icon from "./Icon.svelte";

    export let data = {};
    export let color = '#000';

    const keys = Object.keys(data);

</script>

<div class="grid grid-cols-12 gap-4">
    {#each keys as key}

        <div class="flex flex-col">
            <p class="text-[{color}]">{key}</p>
            <Icon color={color} percentage={data[key]} />
        </div>
            
    {/each}
</div>