<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3';

  export let series = [];

  let timelineRef;
  let svgWidth; // Ancho dinámico
  let svgHeight = 400; // Altura fija por ahora
  let containerWidth;

  const margin = { top: 20, right: 30, bottom: 50, left: 50 };

  const redraw = () => {
      if (!series || series.length === 0 || !containerWidth) return;

      svgWidth = containerWidth - margin.left - margin.right;
      const svg = d3.select(timelineRef);
      svg.selectAll('*').remove(); // Limpiar el SVG antes de redibujar

      const allDates = series.flatMap(s => s.values.map(v => new Date(v.date)));
      const allValues = series.flatMap(s => s.values.map(v => v.value));

      const xScale = d3.scaleTime()
          .domain(d3.extent(allDates))
          .range([margin.left, svgWidth - margin.right]);

      const yScale = d3.scaleLinear()
          .domain([0, d3.max(allValues)])
          .nice()
          .range([svgHeight - margin.bottom, margin.top]);

      // Ejes
      const xAxis = d3.axisBottom(xScale).ticks(13);
      const yAxis = d3.axisLeft(yScale).ticks(5);

      svg.append('g')
          .attr('transform', `translate(0, ${svgHeight - margin.bottom})`)
          .call(xAxis)
          .attr('font-size', '0.7rem')
          .attr('color', '#999')
          .call(g => g.selectAll('.tick line').remove()); // Eliminar las líneas de los ticks


      // Dibujar las series
      series.forEach(serie => {
          const line = d3.line()
              .x(d => xScale(new Date(d.date)))
              .y(d => yScale(d.value))
              .curve(d3.curveMonotoneX);

          svg.append('path')
              .datum(serie.values)
              .attr('fill', 'none')
              .attr('stroke', serie.color)
              .attr('stroke-width', 2)
              .attr('d', line);

          // Puntos
          svg.selectAll(`.point-${serie.name}`)
              .data(serie.values)
              .enter()
              .append('circle')
              .attr('cx', d => xScale(new Date(d.date)))
              .attr('cy', d => yScale(d.value))
              .attr('r', 3)
              .attr('fill', serie.color);
        svg.selectAll(`.label-${serie.name}`)
            .data(serie.values)
            .enter()
            .append('text')
            .attr('x', d => xScale(new Date(d.date)))
            .attr('y', d => yScale(d.value) - 10) // Position slightly above the point
            .attr('text-anchor', 'middle')
            .attr('font-size', '10px')
            .attr('fill', serie.color)
            .text(d => d.value.toFixed(0)); // Display the value

      });
      const legend = svg.append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);

series.forEach((serie, index) => {
    const legendItem = legend.append('g')
        .attr('transform', `translate(${svgWidth*.4 + index* 50}, ${svgHeight+15 - margin.bottom})`);

    // Rectángulo de color
    legendItem.append('rect')
        .attr('x', 0)
        .attr('y', 0)
        .attr('width', 12)
        .attr('height', 12)
        .attr('fill', serie.color);

    // Texto de la leyenda
    legendItem.append('text')
        .attr('x', 20)
        .attr('y', 10)
        .text(serie.name)
      
        .attr('font-size', '12px')
        .attr('fill', '#999');
});

  };

  $: redraw(); // Redibujar cuando cambie el ancho del contenedor o las series

  onMount(() => {
      const resizeObserver = new ResizeObserver(() => redraw());
      resizeObserver.observe(timelineRef.parentNode);
      return () => resizeObserver.disconnect();
  });
</script>

<div class="flex justify-center items-center">
  <!-- Contenedor que adapta el ancho automáticamente -->
  <div class="w-full" bind:clientWidth={containerWidth}>
      <svg bind:this={timelineRef} width="100%" height={svgHeight}></svg>
  </div>
</div>

<style>
  svg {
      display: block;
  }
</style>
