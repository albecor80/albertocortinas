<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { ageDifferences, europeanAverage } from '$lib/data/data';
    import { selectedCountry } from './store';

    let svg;
    const width = 300;
    const height = ageDifferences.length * 20; // Dynamically set height based on the number of bars

    // Set up scales for x and y axes
    const maxDifference = d3.max(ageDifferences, d => Math.abs(d.difference));
    const xScale = d3.scaleLinear()
        .domain([-maxDifference, maxDifference]) // Center around zero
        .range([0, width - 120]); // Account for padding and label space

    const yScale = d3.scaleBand()
        .domain(ageDifferences.map(d => d.country))
        .range([0, height - 40])
        .padding(0.1);

    // Draw the bar chart
    function drawChart() {
        const svgElement = d3.select(svg)
            .attr('width', width)
            .attr('height', height);

        // Add bars
        svgElement.selectAll('.bar')
            .data(ageDifferences)
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr('x', d => 80 + (d.difference < 0 ? xScale(d.difference) : xScale(0))) // Position negative bars to the left
            .attr('y', d => yScale(d.country) + 2.5)
            .attr('width', d => Math.abs(xScale(d.difference) - xScale(0))) // Bar width
            .attr('height', yScale.bandwidth() - 5)
            .attr('fill', '#8EC1DE')
            .on('click', (event, d) => {
                selectedCountry.set(d.country);}); // Update selected country on click
        
        // Add country labels (left or right of the bar)
        svgElement.selectAll('.country_label')
            .data(ageDifferences)
            .enter()
            .append('text')
            .attr('class', 'country_label')
            .attr('x', d => d.difference >= 0 
                ? 80 + xScale(0) - 5 
                : 80 + xScale(d.difference) + Math.abs(xScale(d.difference) - xScale(0)) + 5)
            .attr('y', d => yScale(d.country) + yScale.bandwidth() / 2)
            .attr('dy', '0.35em')
            .attr('text-anchor', d => d.difference >= 0 ? 'end' : 'start') // Align text based on direction
            .attr('fill', '#62A8D2')
            .style('font-size', '12px')
            .text(d => d.country);

        // Add difference labels to bars
        svgElement.selectAll('.label')
            .data(ageDifferences)
            .enter()
            .append('text')
            .attr('class', 'label')
            .attr('x', d => 80 + (d.difference >= 0 
                ? xScale(d.difference) + 5 
                : xScale(d.difference) - 25))
            .attr('y', d => yScale(d.country) + yScale.bandwidth() / 2)
            .attr('dy', '0.35em')
            .attr('fill', '#111')
            .style('font-size', '12px')
            .text(d => d.difference >= 0 
                ? `+${d.difference.toFixed(1)}` 
                : `${d.difference.toFixed(1)}`);
    }

    onMount(() => {
        drawChart(); // Initialize chart on component mount
    });
</script>

<svg bind:this={svg}></svg>
