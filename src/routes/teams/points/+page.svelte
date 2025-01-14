<script>
    import { tick } from 'svelte'; // To wait for DOM updates
    import { page } from '$app/stores'; // SvelteKit store for tracking route changes
    import punts_equips from '$lib/data/equips_punts';
    import DotPlotTeams from '$lib/components/DotPlotTeams.svelte';
    import { onMount } from 'svelte';
	import Titulo from '$lib/components/Titulo.svelte';
 
    /**
     * @type {string | null}
     */
     let currentPath;

    // Function to update the active link styling
    const updateActiveLink = async () => {
        await tick(); // Ensure DOM is updated
        const menuLinks = document.querySelectorAll('.menu-link');
        menuLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('text-slate-700', 'border-slate-700', 'font-bold');
                link.classList.remove( 'border-white','text-slate-300');
            } else {
                
                link.classList.add('border-white', 'text-slate-300');
                link.classList.remove('text-slate-700', 'border-slate-700', 'font-bold');
            }
        });
    };
    onMount(() => {
        updateActiveLink();
    });

    // Reactive block to update the active link when the route changes
    $: currentPath = $page.url.pathname;

</script>

<header class="container mx-auto top-0 h-10 flex mb-4 w-full">
<nav class="bg-white w-full flex flex-col">
    <div class="container mx-auto px-6 flex items-center justify-between">
        <div class="flex mx-auto items-center space-x-8">
            <div class="flex space-x-6">
                <a href="/teams" class="menu-link tracking-widest  text-center p-4 w-36 text-slate-700">WINS/LOSSES</a>
                <a href="/teams/points" class="menu-link tracking-widest text-center p-4 w-36 text-slate-700">POINTS</a>
            </div>
            <div class="flex space-x-6">
                <a href="/about" class="menu-link tracking-widest  text-center p-4 w-36 text-slate-700">ABOUT</a>
                <a href="/contact" class="menu-link tracking-widest  text-center p-4 w-36 text-slate-700">CONTACT</a>
            </div>
        </div>
    </div>
    <div class="bg-turquoise h-px"></div>
    <div class="bg-turquoise h-px"></div>
</nav>
</header>


<div class="flex flex-col  items-ceter justify-center">
    <div class="flex mx-auto flex-col items-ceter justify-center">
        <Titulo titulo="Good offenses win basketball matches, good defenses win championchips." subtitulo="Vertical axis represents points made by the team and horizontal one the points received by each team. " />
        <div class="flex items-center justify-center">
            {#if punts_equips}
            <DotPlotTeams series={punts_equips} />
            {:else}
            <div class="text-center">Loading data...</div>
            {/if}

        </div>
    </div>


</div>
