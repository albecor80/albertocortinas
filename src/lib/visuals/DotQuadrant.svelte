<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';

    let data = [];

    onMount(async () => {
        const response = await fetch('/data/hipersegmentacion.json'); // Ruta al archivo JSON original
        data = await response.json();

        const minRadius = 15; // Radio mínimo
        const maxRadius = 30; // Radio máximo

        // Asignar radio aleatorio a cada burbuja
        data.forEach(d => {
            d.radius = Math.random() * (maxRadius - minRadius) + minRadius;
        });

        drawChart();
    });

    function drawChart() {
        const width = 1200;
        const height = 600;
        const margin = { top: 50, right: 50, bottom: 50, left: 50 };

        const xScale = d3.scaleLinear()
            .domain([0, 10]) // Ajustar según el rango de `value`
            .range([margin.left, width - margin.right]);

        const yScale = d3.scaleLinear()
            .domain([0, 10]) // Escala numérica de availability
            .range([height - margin.bottom, margin.top]);

        // Crear el SVG
        const svg = d3.select('#bubble-chart')
            .attr('width', width)
            .attr('height', height);

        // Crear simulación
        const simulation = d3.forceSimulation(data)
            .force('x', d3.forceX(d => xScale(d.value)).strength(1)) // Atraer hacia la posición en X
            .force('y', d3.forceY(d => yScale(d.availability)).strength(1)) // Atraer hacia la posición en Y
            .force('collide', d3.forceCollide(d => d.radius + 1.8)) // Usar el radio dinámico
            .stop(); // Detener para calcular las posiciones manualmente

        // Ejecutar simulación manualmente
        for (let i = 0; i < 300; i++) simulation.tick();

        // Dibujar burbujas
        const tooltip = d3.select('body')
            .append('div')
            .style('position', 'absolute')
            .style('background', 'white')
            .style('border', '1px solid #ccc')
            .style('padding', '5px')
            .style('border-radius', '5px')
            .style('pointer-events', 'none')
            .style('opacity', 0);

        svg.selectAll('circle')
            .data(data)
            .join('circle')
            .attr('cx', d => d.x) // Usar posición calculada por la simulación
            .attr('cy', d => d.y) // Usar posición calculada por la simulación
            .attr('r', d => d.radius) // Usar radio aleatorio
            .attr('fill', d => {
                // Colorear por tipo
                switch (d.type) {
                    case 'Consumidor': return 'rgba(70, 130, 180, 0.5)'; // Azul semitransparente
                    case 'Damm': return 'rgba(255, 165, 0, 0.5)'; // Naranja semitransparente
                    case 'Establecimiento': return 'rgba(0, 128, 0, 0.5)'; // Verde semitransparente
                    case 'Propietario': return 'rgba(128, 0, 128, 0.5)'; // Morado semitransparente
                    default: return 'rgba(128, 128, 128, 0.5)'; // Gris semitransparente
                }
            })
            .attr('stroke', d => {
                // Contorno opaco por tipo
                switch (d.type) {
                    case 'Consumidor': return 'steelblue';
                    case 'Damm': return 'orange';
                    case 'Establecimiento': return 'green';
                    case 'Propietario': return 'purple';
                    default: return 'gray';
                }
            })
            .attr('stroke-width', 2) // Grosor del contorno
            .on('mouseover', (event, d) => {
                tooltip.style('opacity', 1)
                    .html(`<strong>${d.name}</strong><br>Type: ${d.type}<br>Value: ${d.value}`)
                    .style('left', `${event.pageX + 10}px`)
                    .style('top', `${event.pageY - 10}px`);
            })
            .on('mousemove', (event) => {
                tooltip.style('left', `${event.pageX + 10}px`)
                    .style('top', `${event.pageY - 10}px`);
            })
            .on('mouseout', () => {
                tooltip.style('opacity', 0);
            });

        // Dibujar ejes
        const xAxis = d3.axisBottom(xScale)
            .ticks(2) // Mostrar solo extremos
            .tickFormat(d => {
                if (d === 0) return 'LOW VALUE';
                if (d === 10) return 'HIGH VALUE';
                return '';
            });

        const yAxis = d3.axisLeft(yScale)
            .ticks(2) // Mostrar solo extremos
            .tickFormat(d => {
                if (d === 0) return 'LOW AVAILABILITY';
                if (d === 10) return 'HIGH AVAILABILITY';
                return '';
            });

        svg.append('g')
            .attr('transform', `translate(0,${yScale(5)})`) // Eje X pasa por Y = 5
            .call(xAxis)
            .selectAll('text') // Seleccionar todos los elementos de texto;
            .attr('text-anchor', 'middle') // Desplazar el texto hacia abajo

        svg.append('g')
            .attr('transform', `translate(${xScale(5)},0)`) // Eje Y pasa por X = 5
            .call(yAxis);

        // Líneas centrales para los ejes
        svg.append('line')
            .attr('x1', margin.left)
            .attr('x2', width - margin.right)
            .attr('y1', yScale(5))
            .attr('y2', yScale(5))
            .attr('stroke', 'gray')
            .attr('stroke-width', 1);

        svg.append('line')
            .attr('x1', xScale(5))
            .attr('x2', xScale(5))
            .attr('y1', margin.top)
            .attr('y2', height - margin.bottom)
            .attr('stroke', 'gray')
            .attr('stroke-width', 1);

        const legendData = [
                { label: 'Consumidor', color: 'steelblue' },
                { label: 'Damm', color: 'orange' },
                { label: 'Establecimiento', color: 'green' },
                { label: 'Propietario', color: 'purple' }
            ];

        const legend = svg.append('g')
            .attr('transform', `translate(${width - 1100}, ${margin.top})`); // Posición de la leyenda

        legend.selectAll('rect')
            .data(legendData)
            .join('rect')
            .attr('x', 0)
            .attr('y', (d, i) => i * 25) // Espaciado entre elementos
            .attr('width', 20)
            .attr('height', 20)
            .attr('stroke', d => d.color)
            .attr('fill', d => d.color)
            .attr('opacity', 0.5)
            .style('cursor', 'pointer');

        legend.selectAll('text')
            .data(legendData)
            .join('text')
            .attr('x', 30)
            .attr('y', (d, i) => i * 25 + 15) // Alinear texto con los rectángulos
            .text(d => d.label)
            .attr('font-size', '14px')
            .attr('fill', d => d.color)

        }
</script>

<svg id="bubble-chart"></svg>
