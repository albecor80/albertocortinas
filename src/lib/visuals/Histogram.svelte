<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    let data = [];
    let svgWidth = 550;
    let svgHeight = 450;
    let margin = { top: 20, right: 30, bottom: 50, left: 20 };
    let chartWidth = svgWidth - margin.left - margin.right;
    let chartHeight = svgHeight - margin.top - margin.bottom;
  
    let xScale, yScale;
  
    onMount(async () => {
      // Load data from the JSON file
      const response = await fetch('/data/hotel_cost.json'); // Update path
      const rawData = await response.json();
  
      // Transform the data
      data = rawData.map((item) => {
        const [label, value] = Object.entries(item)[0];
        return { label, value: +value };
      });
  
      // Create scales
      xScale = d3
        .scaleBand()
        .domain(data.map((d) => d.label))
        .range([0, chartWidth])
        .padding(0.2);
  
      yScale = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.value)])
        .nice()
        .range([chartHeight, 0]);
    });
  </script>
  
  <svg width={svgWidth} height={svgHeight}>
    {#if xScale && yScale && data.length > 0}
      <!-- Chart group -->
      <g transform={`translate(${margin.left}, ${margin.top})`}>
        <!-- Bars -->
        {#each data as { label, value }}
          <g>
            <!-- Bar -->
            <rect
              x={xScale(label)}
              y={yScale(value)}
              width={xScale.bandwidth()}
              height={chartHeight - yScale(value)}
              fill="#96DBC9"
            />
            <!-- Value label above the bar -->
            <text
              x={xScale(label) + xScale.bandwidth() / 2}
              y={yScale(value) - 5}
              text-anchor="middle"
              font-size="12"
              fill="#16795f"
            >
              {value.toFixed(1)}
            </text>
          </g>
        {/each}
  
        <!-- X-Axis -->
        <g transform={`translate(0, ${chartHeight})`}>
          {#each data as { label }}
            <text
              x={xScale(label) + xScale.bandwidth() / 2}
              y={20}
              text-anchor="middle"
              font-size="12"
              fill="#16795f"
            >
              {label}
            </text>
          {/each}
        </g>
      </g>
    {/if}
  </svg>
  