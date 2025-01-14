<script>
    export let title;
    export let subtitle;
    export let value;
    export let series;

    // Parse the series to extract the data for the line chart
    let lineChartData = series.map((d, i) => ({ x: i, y: d }));

    const chartWidth = 150; // Width of the SVG
    const chartHeight = 60; // Height of the SVG
    const maxY = Math.max(...series); // Maximum value in the series
    const minY = Math.min(...series); // Minimum value in the series
    const xScale = chartWidth / (lineChartData.length - 1); // Scale for x-axis
    const yScale = chartHeight / (maxY - minY); // Scale for y-axis

</script>

<div class="flex flex-col m-2 bg-gray-100 shadow-md w-44 rounded-lg ">
    <!-- Titles Section -->
    <div class="mb-2 mx-auto">
        <h2 class="text-lg  font-bold">{title}</h2>
        <p class="text-xs italic text-gray-500">{subtitle}</p>
    </div>

    <!-- Value Section -->
    <div class="mb-4">
        <h3 class="text-4xl text-center font-semibold">{value}</h3>
    </div>
    <!-- Line Chart Section -->
    <div class="h-16 mx-auto">
        <svg width={chartWidth} height={chartHeight}>
            <g>
                {#each lineChartData as { x, y }, index}
                    {#if index > 0}
                        <line
                            x1={(lineChartData[index - 1].x) * xScale}
                            y1={chartHeight - (lineChartData[index - 1].y - minY) * yScale}
                            x2={(x) * xScale}
                            y2={chartHeight - (y - minY) * yScale}
                            stroke="blue"
                            stroke-width="2"
                        />
                    {/if}
                {/each}
            </g>
        </svg>
    </div></div>

<style>
    line {
        transition: stroke 0.3s ease;
    }
    line:hover {
        stroke: #4F46E5; /* Example hover color */
    }
</style>