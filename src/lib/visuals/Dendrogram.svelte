<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';

    let data;
    onMount(async () => {
        const response = await fetch('/data/middle_earth.json');
        data = await response.json();
        let selectedNode = null;
        if (data) {
            const width = 700;
            const radius = width / 2;
            
            const tooltip = d3.select('body').append('div')
                .attr('class', 'tooltip')
                .style('position', 'absolute')
                .style('background-color', 'rgba(255, 255, 255, 0.8)')
                .style('padding', '5px')
                .style('border-radius', '5px')
                .style('box-shadow', '0 0 5px rgba(0, 0, 0, 0.3)')
                .style('pointer-events', 'none')
                .style('display', 'none');



            const svg = d3.select('#dendrogram')
                .append('svg')
                .attr('width', width)
                .attr('height', width)
                .append('g')
                .attr('transform', `translate(${radius}, ${radius})`);

            const root = d3.hierarchy(data)
                .sum(d => d.value || 0)
                .sort((a, b) => (b.value || 0) - (a.value || 0));

            const cluster = d3.cluster().size([2 * Math.PI, radius - 100]);
            cluster(root);

            const colorMap = {
                "Valar": '#DAAD86', "Maiar": '#A2B5BB', "Elfos": '#379683',
                "Humanos": '#659DBD', "Enanos": '#8D8741', "Hobbits": '#BC986A',
                "Orcos": '#5D5C61', "Dragones": '#557A95', "Ainur": '#2E4057', "Otros": '#7395AE',
                "Arda": '#24A561'
            };
            root.color = colorMap[root.data.name] || '#F4A261';

            root.children.forEach(child => {
                const color = colorMap[child.data.name];
                child.descendants().forEach(descendant => {
                    descendant.color = color;
                });
            });

            const sizeScale = d3.scaleSqrt()
                .domain([0, d3.max(root.descendants(), d => d.value)])
                .range([2, 50]);
            // Update radial lines to start at the center and spread out radially
            svg.selectAll('path')
                .data(root.links())
                .join('path')
                .attr('d', d3.linkRadial()
                    .angle(d => d.x)
                    .radius(d => d.y))
                .attr('fill', 'none')
                .attr('stroke', d => d.target.color)
                .attr('stroke-width', 1.5);

            svg.selectAll('circle.node')
                .data(root.descendants().slice(0)) // skip root node to avoid duplicate
                .join('circle')
                .attr('class', 'node')
                .attr('transform', d => `rotate(${(d.x * 180 / Math.PI) - 90}) translate(${d.y},0)`)
                .attr('r', d => sizeScale(d.value))
                .attr('fill', d => d.color)
                .on('mouseover', (event, d) => {
                    tooltip.style('display', 'block')
                        .html(`${d.data.name} (${d.value})`);
                })
                .on('mousemove', (event) => {
                    tooltip.style('top', `${event.pageY + 10}px`)
                        .style('left', `${event.pageX + 10}px`);
                })
                .on('mouseout', () => {
                    tooltip.style('display', 'none');
                });
            
            svg.selectAll('text')
                .data(root.descendants())
                .join('text')
                .attr('transform', d => {
                    const angle = (d.x * 180 / Math.PI) - 90;
                    const translate = `translate(${d.y},0)`;
                    const rotate = d.children ? '' : `rotate(${d.x >= Math.PI ? 180 : 0})`;
                    return `rotate(${angle}) ${translate} ${rotate}`;
                })
                .attr('dy', '0.31em')
                .attr('x', d => d.x < Math.PI === !d.children ? 15 : -15)
                .attr('text-anchor', d => d.x < Math.PI === !d.children ? 'start' : 'end')
                .text(d => d.children ? '' : d.data.name) // Show text only for leaf nodes
                .attr('fill', d => d.color) // Use the inherited color for leaf nodes
                .style('font-size', '12px');

            const legend = d3.select('#legend')
                .append('svg')
                .attr('width', width)
                .attr('height', 50)
                .selectAll('g')
                .data(root.children)
                .join('g')
                .attr('transform', (d, i) => `translate(${i * 100}, 0)`);

            legend.append('rect')
                .attr('width', 15)
                .attr('height', 15)
                .attr('fill', d => colorMap[d.data.name]);

            legend.append('text')
                .attr('x', 20)
                .attr('y', 12)
                .text(d => d.data.name)
                .style('font-size', '12px')
                .attr('fill', '#333');


        } else {
            console.error("Data could not be loaded.");
        }
    });
</script>
<div class="flex flex-col">

<div id="dendrogram"></div>
<div id="legend"></div>
</div>
<style>
    #dendrogram {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .tooltip {
        font-size: 12px;
        color: #333;
    }
    #legend {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
</style>
