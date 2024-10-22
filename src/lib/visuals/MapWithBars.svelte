<script>
    import ColorpleteMap from './ColorpleteMap.svelte';
    import HorizontalBarChart from './HorizontalBarChart.svelte';
</script>

<div class="flex w-full h-full">
    <div class="flex flex-col  w-full h-full">
        <div>
            <h2 class="mb-0">When European fly nest?</h2>
            <p class="italic text-sm m-0">Average age at which young people leave the parental house, 2022</p>
            <p class="italic text-sm m-0">Difference with respect to the European average</p>
        </div>
        <div class="flex w-full">
            <div class="w-2/3 h-full">
                <ColorpleteMap />
            </div>
            <div class="w-1/3 my-auto h-full">
                <HorizontalBarChart />
            </div>
        </div>

    </div>

</div>
