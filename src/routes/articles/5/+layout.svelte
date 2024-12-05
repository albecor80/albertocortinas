<script lang="ts">
    import type { pageData } from "$lib/types"; // Importing the type

    let title = "When the guest doubts"
    let date = "2024-11-20"
    let author = "Alberto Cortinas"
    let summary = "Exploring the reasons for hotel reservation cancellations."
    import Navigator from "$lib/navigate/Navigator.svelte";
    import PageTransition from "$lib/navigate/Transition.svelte";
    export let data: pageData
</script>

<Navigator />

<PageTransition key={data.url} duration={600}>
    <slot />
</PageTransition>