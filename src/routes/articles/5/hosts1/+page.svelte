<script>
	import BarMap from "$lib/visuals/BarMap.svelte";
    import ColorpleteMapHotels from "$lib/visuals/ColorpleteMapHotels.svelte";
	import Histogram from "$lib/visuals/Histogram.svelte";



</script>


<div class="flex flex-col w-full min-h-screen">
    <div class="flex flex-col p-4 w-full bg-[#96DBC9]">
        <h1 class="pt-8 text-center">The guest matters</h1>
        <p class="flex mx-auto text-lg text-gray-600">Which cancellation ratio do we have depending on the guests and... </p>
    </div>
    <div class="flex flex-col w-full p-4">
        <p class=" font-semibold text-xl mt-0 mx-auto  text-gray-500">...wether they come for work or vacation?</p>

        <BarMap />

    </div>

</div>




