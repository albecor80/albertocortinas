<script>
    import { tick } from 'svelte'; // To wait for DOM updates
    import { page } from '$app/stores'; // SvelteKit store for tracking route changes
    import punts_equips from '$lib/data/equips_punts';
    import DotPlotTeams from '$lib/components/DotPlotTeams.svelte';
    import { onMount } from 'svelte';
 
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



<div class="relative h-screen">
    
    <div class="flex flex-col items-center text-center justify-center py-8 px-4">
      <h1 class="text-8xl text-gray-800 font-bebas">Points made vs Points received</h1>
      <h2 class="text-2xl text-gray-400 italic font-baskerville">Good offenses win basketball matches, good defenses win championchips.</h2>
      <div class="flex mt-4 pt-1 pl-1 flex-col h-full">
        <div class="flex items-center justify-center">
            {#if punts_equips}
            <DotPlotTeams series={punts_equips} />
            {:else}
            <div class="text-center">Loading data...</div>
            {/if}

        </div>
    </div>

    
    </div>
 
    <!-- Navigation Buttons -->
    <a
        href="/season"
        class="absolute top-1/2 left-4 transform -translate-y-1/2 h-12 w-12 bg-gray-200 hover:bg-gray-300 flex items-center justify-center rounded-full shadow-md"
        aria-label="Previous Page"
    >
        <span class="text-black font-bold text-lg">❮</span>
    </a>

    <a
        href="/teams"
        class="absolute top-1/2 right-4 transform -translate-y-1/2 h-12 w-12 bg-gray-200 hover:bg-gray-300 flex items-center justify-center rounded-full shadow-md"
        aria-label="Next Page"
    >
        <span class="text-black font-bold text-lg">❯</span>
    </a>
</div>
