<script>
    import { onMount } from "svelte";

    export let serie1 = [];
    export let serie2 = [];

    let size = 300;
    let center = size / 2;
    let radius = size * 0.45;

    const updateDimensions = () => {
        size = Math.min(window.innerWidth, window.innerHeight) * 0.4;
        center = size / 2;
        radius = size * 0.45;
    };

    const getCoordinates = (value, month) => {
        const angle = (30 * month - 90) * (Math.PI / 180); // Offset -90 for 12 o'clock
        const scaledRadius = value * (radius / 50); // Scale factor proportional to the data
        const x = center + scaledRadius * Math.cos(angle);
        const y = center + scaledRadius * Math.sin(angle);
        return { x, y };
    };
    let points1 = [];
    let points2 = [];
    let polyline1 = "";
    let polyline2 = "";

    onMount(() => {
        updateDimensions();
        points1 = serie1.map((value, i) => getCoordinates(value, i));
        points2 = serie2.map((value, i) => getCoordinates(value, i));      
        
        polyline1 = `M ${points1.map(({ x, y }) => `${x},${y}`).join(" ")} Z`;
        polyline2 = `M ${points2.map(({ x, y }) => `${x},${y}`).join(" ")} Z`;

        console.log(points1, points2);
        window.addEventListener("resize", updateDimensions);
        return () => window.removeEventListener("resize", updateDimensions);
    });

</script>
<svg
class="w-full h-full"
viewBox={`-20 -20 ${40+size} ${40+size}`}
xmlns="http://www.w3.org/2000/svg"
>
<!-- Circle for context -->
{#each Array(12) as _, i}
<line
    x1={center}
    y1={center}
    x2={center + radius * Math.cos((30 * i - 90) * (Math.PI / 180))}
    y2={center + radius * Math.sin((30 * i - 90) * (Math.PI / 180))}
    class="stroke-gray-100"
    stroke-width="1"
/>
{/each}
<!-- Lines connecting points for dataset 1 -->
<path d={polyline1} class="fill-none stroke-[#96DBC9] stroke-1" />

<!-- Lines connecting points for dataset 2 -->
<path d={polyline2} class="fill-none stroke-[#dd6fb2] stroke-1" />

<!-- Dots for dataset 1 -->
{#each points1 as { x, y }, i}
    <circle cx={x} cy={y} r={size * 0.0065} class="fill-[#96DBC9]" />
    <text
        x={x}
        y={y - size * 0.03}
        text-anchor="middle"
        alignment-baseline="middle"
        class="text-[0.5rem] fill-[#96DBC9]"
    >
    {serie1[i]}%
</text>
    {/each}
<!-- Dots for dataset 2 -->
{#each points2 as { x, y }, i}
    <circle cx={x} cy={y} r={size * 0.0065} class="fill-[#dd6fb2]" />
    <text
        x={x}
        y={y - size * 0.03}
        text-anchor="middle"
        alignment-baseline="middle"
        class="text-[0.5rem] fill-[#dd6fb2]"
    >
        {serie2[i]}%
    </text>
{/each}
<!-- Month labels -->
{#each Array(12) as _, i}
    <text
        x={center + radius * 1.1 * Math.cos((30 * i - 90) * (Math.PI / 180))}
        y={center + radius * 1.1 * Math.sin((30 * i - 90) * (Math.PI / 180))}
        text-anchor="middle"
        alignment-baseline="middle"
        class="text-xs md:text-sm fill-gray-400"
        style="font-size: {size * 0.03}px;"
    >
        {["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][i]}
    </text>
{/each}

</svg>
