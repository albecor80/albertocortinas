<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";
  
    let chart;
  
    onMount(() => {
      const data = {
        nodes: [

            { name: "Valoració Servei distribuïdor" },
            { name: "Valoració Consumidor" },
            { name: "Valoració FFVV" },
            { name: "Valoració XXSS" },
            { name: "Valoració Empreses IB" },
            
            { name: "Cens i preu compra competència" },
            { name: "PVP productes Damm" },
            { name: "PVP productes No Damm" },
            { name: "Ticket Damm / No Damm" },
            { name: "Detecció Events propers" },

            { name: "Condicions Comercials" },
            { name: "Morositat Prospects" },
            { name: "Morositat Clients Damm" },
        ],
        links: [

            { source: 0, target: 15, value: 10 },
            { source: 0, target: 16, value: 50 },
            { source: 0, target: 17, value: 10 },
            { source: 1, target: 18, value: 10 },
            { source: 2, target: 16, value: 10 },
            { source: 2, target: 17, value: 10 },
            { source: 2, target: 19, value: 10 },

        ]
      };
  
      const width = 600;
    const height = 300;
    const nodeWidth = 15;
    const nodePadding = 20;

    const svg = d3
      .select(chart)
      .attr("width", width)
      .attr("height", height);

    // Calculate total flow value for proportions
    const totalValue = d3.sum(data.links, (d) => d.value);

    // Assign node positions (source: left, targets: right)
    const nodeHeightScale = d3
      .scaleLinear()
      .domain([0, totalValue])
      .range([0, height - (data.nodes.length - 1) * nodePadding]);

    data.nodes.forEach((node, i) => {
      const incomingLinks = data.links.filter((link) => link.target === i);
      const outgoingLinks = data.links.filter((link) => link.source === i);

      node.value = d3.sum(incomingLinks, (d) => d.value) || d3.sum(outgoingLinks, (d) => d.value);

      if (i === 0) {
        node.x = 0;
        node.y = (height - nodeHeightScale(node.value)) / 2;
      } else {
        node.x = width - nodeWidth;
        const prevNodeIndex = data.links.find((link) => link.target === i).source;
        node.y =
          data.nodes[prevNodeIndex].y + (i - 1) * (nodePadding + nodeHeightScale(node.value));
      }

      node.height = nodeHeightScale(node.value);
    });

    // Draw nodes
    svg
      .append("g")
      .selectAll("rect")
      .data(data.nodes)
      .join("rect")
      .attr("x", (d) => d.x)
      .attr("y", (d) => d.y)
      .attr("width", nodeWidth)
      .attr("height", (d) => d.height)
      .attr("fill", "steelblue");

    // Draw links
    svg
      .append("g")
      .selectAll("path")
      .data(data.links)
      .join("path")
      .attr("d", (d) => {
        const sourceNode = data.nodes[d.source];
        const targetNode = data.nodes[d.target];
        const midX = (sourceNode.x + nodeWidth + targetNode.x) / 2;

        return `
          M${sourceNode.x + nodeWidth},${sourceNode.y + sourceNode.height / 2}
          C${midX},${sourceNode.y + sourceNode.height / 2}
          ${midX},${targetNode.y + targetNode.height / 2}
          ${targetNode.x},${targetNode.y + targetNode.height / 2}
        `;
      })
      .attr("fill", "none")
      .attr("stroke", "#aaa")
      .attr("stroke-width", (d) => (d.value / totalValue) * 10);
  });
</script>

<svg bind:this={chart}></svg>
