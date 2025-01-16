<!-- src/routes/Teams.svelte -->

<script>
    import { tick } from 'svelte';
    import { page } from '$app/stores';
    import { onMount, onDestroy } from 'svelte';
    import Equip from '$lib/components/Equip.svelte';
    import equips_ordenats from '$lib/data/equips.js';
    import { estat_equips_tirs } from '$lib/data/estat_equips_tirs.js';
    import CircleGrid from '$lib/components/CircleGrid.svelte';
    // -----------------------------
    // Function Definitions
    // -----------------------------

    /**
     * Handles the selection of a team.
     * @param {Object} equip - The selected team object.
     */
    const selectEquip = (equip) => {
        console.log(`selectEquip called. Selecting team: ${equip.nom} (ID: ${equip.id})`);
        selectedEquip = equip;
    };

    /**
     * Retrieves the statistics for the currently selected team.
     * @returns {Object|null} - The statistics object or null if not found.
     */
    const getSelectedEquipStats = () => {
        console.log(`getSelectedEquipStats called. Selected Equip ID: ${selectedEquip.id}`);
        if (selectedEquip.id === null || selectedEquip.id === undefined) {
            console.log('Selected Equip has no ID.');
            return null;
        }
        // Find the stats where id matches selectedEquip.id
        const stats = estat_equips_tirs.find(stat => String(stat.id) === String(selectedEquip.id)) || null;
        console.log(`Found stats:`, stats);
        return stats;
    };
    // -----------------------------
    // State Variables
    // -----------------------------
    let currentPath;
    let selectedEquip = equips_ordenats[0]; // Initialize with the first Equip
    let selectedEquipStats = null; // Holds the statistics for the selected team


    // -----------------------------
    // Reactive Statements
    // -----------------------------

    /**
     * Reactive statement to update selectedEquipStats whenever selectedEquip changes.
     */
    $: selectedEquipStats = getSelectedEquipStats();

    /**
     * Reactive statement to log changes to selectedEquip.
     */
    $: console.log(`Selected Equip updated to: ${selectedEquip.nom} (ID: ${selectedEquip.id})`);

    /**
     * Reactive statement to update currentPath when the route changes.
     */
    $: currentPath = $page.url.pathname;

    // -----------------------------
    // Lifecycle Hooks
    // -----------------------------

    onMount(() => {
        console.log('Component mounted.');
        console.log('Equipos:', equips_ordenats);
        console.log('Estadísticas:', estat_equips_tirs);
    });

    /**
     * Updates active link styling based on the current path.
     */
    const updateActiveLink = async () => {
        await tick(); // Ensure DOM is updated
        const menuLinks = document.querySelectorAll('.menu-link');
        menuLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('text-slate-700', 'border-slate-700', 'font-bold');
                link.classList.remove('border-white', 'text-slate-300');
            } else {
                link.classList.add('border-white', 'text-slate-300');
                link.classList.remove('text-slate-700', 'border-slate-700', 'font-bold');
            }
        });
    };
</script>

<style>
    /* Optional: Add any component-specific styles here */
    .selected-equip {
        transition: all 0.3s ease-in-out;
    }

    /* Optional: Adjust button styles on hover and disabled state */
    button:hover:not(:disabled) {
        background-color: #3b82f6; /* Tailwind's blue-500 */
    }

    button:disabled {
        cursor: not-allowed;
        opacity: 0.6;
    }
</style>

<div class="relative min-h-screen bg-gray-50">
    <!-- Main Content Container -->
    <div class="flex flex-col items-center text-center justify-center py-8 px-4">
        <!-- Header Section -->
        <h1 class="text-5xl md:text-8xl text-gray-800 font-bebas ">EXPLORE THE TEAMS</h1>
        <h2 class="text-xl md:text-2xl text-gray-400 italic font-baskerville ">
            Every team has a story. Explore the journey of each team through the season.
        </h2>

        <!-- Equip Cards Section -->
        <div class="flex flex-wrap justify-center gap-4 mb-8">
            {#each equips_ordenats as equip (equip.id)}
                <Equip
                    equip={equip}
                    isSelected={selectedEquip.id === equip.id}
                    on:select={event => {
                        console.log(`Received select event for: ${event.detail.nom} (ID: ${event.detail.id})`);
                        selectEquip(event.detail);
                    }}
                />
            {/each}
        </div>

        <!-- Selected Equip Display Section -->
        <div class="flex ml-48 h-full w-full items-center">
            <div class="flex-none w-[300px] h-auto border-4 border-slate-700 rounded-lg flex flex-col items-center justify-start p-4 bg-white">
                <h1 class="text-3xl md:text-4xl text-slate-700 tracking-wider font-bebas mt-2">
                    {selectedEquip.nom.toUpperCase()}
                </h1>
                <div class="w-[90%] h-[2px] bg-slate-700 my-2"></div>
                <p class=" md:text-base text-slate-700 text-center italic font-baskerville">
                    Baloncesto Málaga SAD
                </p>
                <p class=" text-xs  text-slate-700 text-center italic font-baskerville">
                    Palacio de Deportes José María Martín Carpena
                </p>
                <a
                    href="http://www.unicajabaloncesto.com"
                    class="mt-2 text-xs  text-slate-700 text-center italic font-baskerville"
                >
                http://www.unicajabaloncesto.com
                </a>
                <img src={selectedEquip.img} alt={selectedEquip.nom} class="w-24 md:w-32 h-auto mt-4">
            </div>
            <div class="flex ">
                <!-- Statistics Section -->
                {#if selectedEquipStats}
                    <div class="flex m-4">
                        <div class="flex flex-col">
                            <h2 class="font-bebas tracking-wider text-2xl ">FREE THROWS</h2>
                            <CircleGrid filledCircles={selectedEquipStats.perc_TL} highlightedCircle=75 />

                        </div>
                        <div class="flex flex-col">
                            <h2 class="font-bebas tracking-wider text-2xl ">2 - POINT</h2>
                            <CircleGrid filledCircles={selectedEquipStats.perc_T2} highlightedCircle=54 />

                        </div>

                        <div class="flex flex-col">
                            <h2 class="font-bebas tracking-wider text-2xl ">3 - POINT</h2>
                            <CircleGrid filledCircles={selectedEquipStats.perc_T3} highlightedCircle=35 />

                        </div>

                        
                    </div>

                {:else}
                    <div class="w-full max-w-md mt-4 p-4 bg-white rounded-lg shadow-md">
                        <h2 class="text-xl font-semibold text-gray-700 mb-4">Shooting Statistics</h2>
                        <p class="text-gray-500">No statistics available for this team.</p>
                    </div>
                {/if}

            </div>
        </div>
    </div>

    <!-- Navigation Buttons -->
    <a
        href="/points"
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
