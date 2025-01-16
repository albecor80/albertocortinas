<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';

    import equips_ordenats from '$lib/data/equips';
    // Declare the prop with the exact name
    export let series = [];
  
    let svg;
    const width = 800;
    const height = 600;
    const margin = { top: 40, right: 40, bottom: 50, left: 70 };
  
    onMount(() => {
      if (!series || series.length === 0) {
        console.error('series data is empty or undefined.');
        return;
      }
      series = series.map(team => {
        const equip = equips_ordenats.find(e => e.id === team.value);

        return {
            ...team,
            nom: equip ? equip.nom : 'Unknown Team',
            img: equip ? equip.img : 'img/equips/placeholder.png', // Fallback image
            position: equip ? equip.position : 'N/A'
        };
    });

      // Set up SVG
      const svgElement = d3.select(svg)
        .attr('width', width)
        .attr('height', height);
  
      // Clear any existing content
      svgElement.selectAll('*').remove();
  
      // Define the chart area
      const chartWidth = width - margin.left - margin.right;
      const chartHeight = height - margin.top - margin.bottom;
  
      // Create a group element for margins
      const chart = svgElement.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
  
      // Define scales
      const xScale = d3.scaleLinear()
        .domain(d3.extent(series, d => d.x)).nice()
        .range([0, chartWidth]);
  
      const yScale = d3.scaleLinear()
        .domain(d3.extent(series, d => d.y)).nice()
        .range([chartHeight, 0]);
  
      // Define axes
      const xAxis = d3.axisBottom(xScale).ticks(5);
      const yAxis = d3.axisLeft(yScale).ticks(5);
  
      // Append X axis
      chart.append('g')
        .attr('transform', `translate(0, ${chartHeight})`)
        .call(xAxis)
        .append('text')
        .attr('x', chartWidth / 2)
        .attr('y', 40)
        .attr('fill', 'black')
        .attr('text-anchor', 'middle')
        .attr('font-size', '2em')
        .attr('class', 'font-baskerville italic') // Tailwind classes
        .text('points received');
        chart.selectAll('.domain').remove();
        chart.selectAll('.x-axis .tick line')
            .attr('stroke', '#808080');

      // Append Y axis
      chart.append('g')
        .call(yAxis)
        .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', -chartHeight / 2)
        .attr('y', -50)
        .attr('fill', 'black')
        .attr('text-anchor', 'middle')
        .attr('font-size', '2em')
        .attr('class', 'font-baskerville italic') // Tailwind classes

        .text('points made');
        chart.selectAll('.domain').remove();


    
      // Append dots
      chart.selectAll('.dot')
        .data(series)
        .enter().append('image')
        .attr('class', 'dot')
        .attr('href', d => d.img) // Image path from data
        .attr('x', d => xScale(d.x))
        .attr('y', d => yScale(d.y))
        .attr('width', 50)
        .attr('height', 50)
        .on('mouseover', function(event, d) {
          const tooltip = d3.select('body').append('div')
          .attr('class', 'tooltip')
          .style('position', 'absolute')
          .style('background-color', 'white')
          .style('border', '1px solid #808080')
          .style('border-radius', '5px')
          .style('padding', '10px')
          .style('opacity', 0);

        tooltip.transition()
          .duration(200)
          .style('opacity', 0.9);
        tooltip.html(`
          <strong>${d.nom}</strong><br/>
          Position: ${d.position}<br/>
          Points Against: ${d.x}<br/>
          Points: ${d.y}
        `)
          .style('left', `${event.pageX + 5}px`)
          .style('top', `${event.pageY - 28}px`);
      })
      .on('mouseout', function () {
        // Remove the tooltip on mouse out
        d3.selectAll('.tooltip').remove();
      });
    });
  </script>

  
  <svg bind:this={svg}></svg>
  

  <style>
    .tick line {
        stroke: #808080 !important;
    }

    .tick text {
        fill: #808080 !important;
    }

    .tooltip {
    pointer-events: none; /* Avoid interfering with mouse events */
    font-family: Arial, sans-serif;
    font-size: 14px;
    color: #333;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

</style>
