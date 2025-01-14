<script>

	import Titulo from "$lib/components/Titulo.svelte";
    import Equip from "$lib/components/Equip.svelte";
    import equips_ordenats from "$lib/data/equips.js";
    let visibleCount = 6; // Initial number of items to show
    let rowsToShow = 1; // Tracks the number of rows being displayed

    function showMore() {
        rowsToShow += 1;
        visibleCount = rowsToShow * 6; // Update visible count based on rows
    }

</script>

<div class="flex h-screen max-w-full ml-16 p-4 mr-16">
    <!-- First Section -->
    <div class="flex flex-col flex-1 max-w-full gap-4">
        <a href="/league">
            <div class="flex  flex-col p-4 rounded-md bg-gray-100">
                <h1 class="font-bebas tracking-widest text-4xl text-gray-800">
                    THE LEAGUE
                </h1>
                <h2 class="font-baskerville font-xl">
                    From the first match to the seasons' final buzzer, dive into the triumphs, surprises, and defining stats that shaped a year full of the game we love.
                </h2>
            </div>
    
        </a>
        <div class="flex  flex-col p-4 rounded-md bg-gray-100">
            <h1 class="font-bebas tracking-widest text-4xl text-gray-800">
                THE TEAMS
            </h1>
            <h2 class="font-baskerville font-xl">
                Every team has a story. Explore the journey of each team through the season.
            </h2>
            <div class="grid grid-cols-9 ">
                {#each equips_ordenats.slice(0, 18) as equip}
                <a href="teams/{equip.id}">
                    <div class="w-48">
                        <Equip nom={equip.nom} imatge={equip.img} width="w-24" height="h-24"/>
                    </div>
                </a>

                {/each}
            </div>
            
        </div>
        <div class="flex  flex-col p-4 rounded-md bg-gray-100">
            <h1 class="font-bebas tracking-widest text-4xl text-gray-800">
                THE PLAYERS
            </h1>
            <h2 class="font-baskerville font-xl">
                Basketball is a team game but, sometimes, a single player can make the difference. Discover the most valuable players of the season.
            </h2>
        </div>
    </div>  
</div>