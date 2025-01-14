<script>

	import Titulo from "$lib/components/Titulo.svelte";
    import Equip from "$lib/components/Equip.svelte";
    import equips_ordenats from "../lib/data/equips.js";

</script>

<div class="flex h-screen max-w-full p-4">
    <!-- First Section -->
    <div class="flex  flex-1 max-w-full gap-4">
        <div class="flex flex-1 flex-col p-4 rounded-md bg-gray-100">
            <Titulo titulo="THE LEAGUE" subtitulo="Subtítulo" />
            <div class="flex flex-col">
                {#each equips_ordenats as equip}
                    <div class="flex w-48">
                        <Equip nom={equip.nom} imatge={equip.img} />
                        <div class="flex ml-4 my-auto gap-1">
                            {#each equip.matches as match}
                                <div
                                    class="w-2 h-2 md:w-3 md:h-3"
                                    class:bg-green-500={match === 1}
                                    class:bg-gray-300={match === 0}
                                ></div>
                            {/each}
                        </div>
                    </div>
                {/each}
            </div>
        </div>
        <div class="flex flex-1 max-w-full gap-4">
            <div class="flex flex-col flex-1 p-4 rounded-md bg-gray-100">
                <Titulo titulo="EQUIPOS" subtitulo="Subtítulo" />
                <div class="flex flex-col">
                    {#each equips_ordenats as equip}
                        <div class="flex w-48">
                            <Equip nom={equip.nom} imatge={equip.img} />
                            <div class="flex ml-4 my-auto gap-1">
                                {#each equip.matches as match}
                                    <div
                                        class="w-2 h-2 md:w-3 md:h-3"
                                        class:bg-green-500={match === 1}
                                        class:bg-gray-300={match === 0}
                                    ></div>
                                {/each}
                            </div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    
        <div class="flex flex-1 p-4 rounded-md bg-gray-100">
            <Titulo titulo="5 jugadors més valuosos" subtitulo="Subtítulo" />
        </div>
    </div>
</div>