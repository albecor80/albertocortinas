<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';
    import { ages } from '$lib/data/data';
    import { selectedCountry } from './store';

    let svg;
    let legendSvg;
    let tooltip;
    let width, height;
    let selected;

    selectedCountry.subscribe(country => {
        selected = country;
        if (svg) drawMap(); // Redraw the map when a country is selected
    });

    // Dynamically calculate dimensions based on the window size
    function updateDimensions() {
        width = Math.min(window.innerWidth * 0.9, 800); // Set a maximum width
        height = width * 0.95; // Adjust height based on width, keeping a consistent aspect ratio
    }

    // Load GeoJSON file and draw the map
    onMount(async () => {
        try {
            updateDimensions(); // Initial dimensions

            // Fetch the GeoJSON data
            const response = await fetch('/src/lib/data/europe.geojson');
            const geojson = await response.json();

            console.log('Fetched GeoJSON:', geojson); // Log GeoJSON structure for inspection

            // Projection to transform geo-coordinates into 2D plane
            const projection = d3.geoMercator()
                .scale(width / 1.3) // Adjust scale based on dynamic width
                .translate([width / 2.8, height * 1.5]);

            // Path generator
            const path = d3.geoPath().projection(projection);

            /** @type {{ [key: string]: number }} */
            const ageMap = {};
            ages.forEach(d => {
                ageMap[d.country] = d.age;
            });

            const colorScale = d3.scaleSequential(d3.interpolateBlues)
                .domain([d3.min(ages, d => d.age), d3.max(ages, d => d.age)]);

            // Append the SVG element
            const svgElement = d3.select(svg)
                .attr('viewBox', `0 0 ${width} ${height}`) // Set viewBox for responsiveness
                .attr('preserveAspectRatio', 'xMinYMin meet'); // Ensure it resizes properly

            // Add tooltip to DOM
            tooltip = d3.select("#tooltip");
            
            // Bind data and create paths for each feature
            svgElement.selectAll('path')
                .data(geojson.features)
                .enter()
                .append('path')
                .attr('d', path)
                .attr('fill', d => {
                    const countryName = d.properties.NAME;
                    const age = ageMap[countryName];
                    return age ? colorScale(age) : '#ccc'
                })
                .attr('stroke', '#fff')    // Country border color
                .on('mouseover', function (event, d) {
                    const countryName = d.properties.NAME;
                    const age = ageMap[countryName];
                    tooltip
                        .style("left", (event.pageX + 5) + "px")
                        .style("top", (event.pageY - 5) + "px")
                        .style("font-size", "12px")
                        .style("opacity", 1)
                        .html(`${countryName}<br/>Age: ${age ? age + " years" : "No data"}`);  // Display country name and age
                })
                .on('mousemove', function (event) {
                    tooltip.style("left", (event.pageX + 5) + "px").style("top", (event.pageY - 5) + "px");
                })
                .on('mouseout', function () {
                    tooltip.style("opacity", 0);  // Hide tooltip when not hovering
                });

            // Append the legend SVG
            const legendWidth = Math.min(window.innerWidth * 0.5, 500); // Make legend responsive
            const legendHeight = 28;

            const legendSvgElement = d3.select(legendSvg)
                .attr('viewBox', `0 0 ${legendWidth} ${legendHeight}`) // Responsive legend
                .attr('preserveAspectRatio', 'xMinYMin meet'); // Maintain aspect ratio

            // Create a linear gradient for the legend
            const defs = legendSvgElement.append('defs');
            const linearGradient = defs.append('linearGradient')
                .attr('id', 'linear-gradient');

            linearGradient.selectAll('stop')
                .data(colorScale.ticks(10).map((t, i, n) => ({
                    offset: `${100 * i / n.length}%`,
                    color: colorScale(t)
                })))
                .enter()
                .append('stop')
                .attr('offset', d => d.offset)
                .attr('stop-color', d => d.color);

            // Draw the gradient rectangle
            legendSvgElement.append('rect')
                .attr('width', legendWidth)
                .attr('height', legendHeight - 20)
                .style('fill', 'url(#linear-gradient)');

            // Add a scale for the legend
            const xScale = d3.scaleLinear()
                .domain([d3.min(ages, d => d.age), d3.max(ages, d => d.age)])
                .range([0, legendWidth]);

            const xAxis = d3.axisBottom(xScale)
                .ticks(6)
                .tickFormat(d => `${d} yrs`);

            // Append the axis to the legend
            legendSvgElement.append('g')
                .attr('transform', `translate(0,${legendHeight - 20})`)
                .call(xAxis)
                .call(g => g.select(".domain").remove())  // Remove axis line
                .call(g => g.selectAll(".tick line").remove())
                .call(g => g.selectAll(".tick text")
                    .style("fill", "rgb(98, 168, 210)"));
        } catch (error) {
            console.error("Error loading or processing GeoJSON", error);
        }

        // Resize handler for responsiveness
        window.addEventListener('resize', () => {
            updateDimensions(); // Recalculate dimensions on resize
            drawMap(); // Redraw map based on updated dimensions
        });
    });
</script>

<div class="flex flex-col">
    <svg class="mx-auto" bind:this={svg}></svg>
    <svg class="mx-auto" bind:this={legendSvg}></svg>
</div>


<div id="tooltip" class="absolute bg-white text-gray-800 p-1 rounded"></div>
