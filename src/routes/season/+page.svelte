<script>
    import Equip from "$lib/components/Equip.svelte";
    import equips_ordenats from "$lib/data/equips.js";
    let hoveredEquipId = null; // Tracks the ID of the hovered Equip
    let selectedEquip = equips_ordenats[0]; // Initialize with the first Equip

    let pages = [
      { title: "THE SEASON" },
      { title: "Page 2" },
      { title: "Page 3" },
      { title: "Page 4" }
    ];
    let currentPageIndex = 0;
  
    function nextPage() {
      if (currentPageIndex < pages.length - 1) {
        currentPageIndex++;
      }
    }
  
    function previousPage() {
      if (currentPageIndex > 0) {
        currentPageIndex--;
      }
    }
  </script>
  
<div class="relative h-screen">
    
    <div class="flex flex-col items-center text-center justify-center py-8 px-4">
      <h1 class="text-8xl text-gray-800 font-bebas">Wins and losses through the season</h1>
      <h2 class="text-2xl text-gray-400 italic font-baskerville">Each team did his own journey through the season, with some good moments and also bad ones</h2>
      <div class="flex mt-4 pt-1 pl-1 flex-col h-full">
        {#each equips_ordenats as equip}
            <div class="flex">
              <div class="font-baskerville italic text-gray-500 mr-2 text-right w-64">
                {equip.nom}
              </div>
              <Equip
                width="w-6"
                equip={equip}
                isHovered={hoveredEquipId === equip.id}
                isSelected={selectedEquip.id === equip.id}
                on:select={event => selectEquip(event.detail)}
                on:mouseover={() => hoveredEquipId = equip.id}
                on:mouseleave={() => hoveredEquipId = null}
                on:focus={() => hoveredEquipId = equip.id}
                on:blur={() => hoveredEquipId = null}
            />
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

    <!-- Navigation Buttons -->

    <a
        href="/teams"
        class="absolute top-1/2 right-4 transform -translate-y-1/2 h-12 w-12 bg-gray-200 hover:bg-gray-300 flex items-center justify-center rounded-full shadow-md"
        aria-label="Next Page"
    >
        <span class="text-black font-bold text-lg">❯</span>
    </a>
</div>
