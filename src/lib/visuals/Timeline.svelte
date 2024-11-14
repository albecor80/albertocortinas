<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
 
    let data;
 
    onMount(async () => {
       // Fetch data from the local file
       const response = await fetch('/data/cv.json');
       data = await response.json();

      const annotationsResponse = await fetch('/data/cv_milestones.json');
      const annotations = await annotationsResponse.json();

      processAndRenderChart(annotations);

    });
 
    function processAndRenderChart(annotations) {
       // Extract categories
       const categories = Array.from(new Set(data.flatMap(d => d.values.map(v => v.name))));
       const preparedData = data.map(yearData => {
          const yearObj = { year: yearData.year };
          categories.forEach(cat => {
             const categoryData = yearData.values.find(v => v.name === cat);
             yearObj[cat] = categoryData ? categoryData.value : 0;
          });
          return yearObj;
       });
 
       // Set up dimensions and scales
       const margin = { top: 100, right: 30, bottom: 30, left: 50 };
       const width = 800 - margin.left - margin.right;
       const height = 400 - margin.top - margin.bottom;
 
       const svg = d3.select('#chart')
          .append('svg')
          .attr('width', width + margin.left + margin.right)
          .attr('height', height + margin.top + margin.bottom)
          .append('g')
          .attr('transform', `translate(${margin.left},${margin.top})`);
 
       const x = d3.scaleLinear()
          .domain(d3.extent(preparedData, d => d.year))
          .range([0, width]);
 
       const y = d3.scaleLinear()
          .domain([0, d3.max(preparedData, d => d3.sum(categories.map(cat => d[cat])))])
          .range([height, 0]);
 

         const categoryColors = {
            "Studying": "#4B6A9B",   // Soft Slate Blue
            "Leasure": "#F5A623",    // Warm Amber
            "Working": "#50B083",    // Jade Green
            "Family": "#D95D39"      // Burnt Coral
         };
      
      const color = d3.scaleOrdinal()
         .domain(categories)
         .range(categories.map(cat => categoryColors[cat]));

       const stack = d3.stack()
          .keys(categories)
          .order(d3.stackOrderNone)
          .offset(d3.stackOffsetNone);
 
       const stackedData = stack(preparedData);
         console.log(stackedData);
       const tooltip = d3.select("body")
         .append("div")
         .style("position", "absolute")
         .style("padding", "8px")
         .style("background", "rgba(0,0,0,0.7)")
         .style("color", "white")
         .style("border-radius", "4px")
         .style("pointer-events", "none")
         .style("opacity", 0);

       // Draw areas
       svg.selectAll('path')
         .data(stackedData)
         .enter().append('path')
         .attr('fill', d => color(d.key))
         .attr('d', d3.area()
            .x(d => x(d.data.year))
            .y0(d => y(d[0]))
            .y1(d => y(d[1]))
            .curve(d3.curveCatmullRom.alpha(0.8)))
         .on("mouseover", (event, d) => {
               tooltip.transition().duration(200).style("opacity", 0.9);
            })
         .on("mousemove", (event, d) => {
            // Calculate index based on mouse position
            const [xPos] = d3.pointer(event);
            const yearIndex = Math.round(x.invert(xPos));
            const index = yearIndex - 1998
            if (d[index]) {
               const value = d[index][1] - d[index][0];  // Calculate actual value
               tooltip.html(`<strong>${d.key}</strong><br>${value} hours/day`)
                  .style("left", (event.pageX + 10) + "px")
                  .style("top", (event.pageY - 20) + "px");
            }
            })
         .on("mouseout", () => {
               tooltip.transition().duration(200).style("opacity", 0);
         });

 
       // Add axes
       svg.append('g')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x).tickFormat(d3.format('d')))
            .call(d3.axisBottom(x).tickSize(0).tickPadding(10))
            .selectAll("text")  // Select all label text elements
            .style("font-size", "14px")  // Increase font size
            .style("fill", "gray");      // Set color to gray

      svg.selectAll(".domain").remove();

     // Add legend
     const legend = d3.select("#legend2")
         .append("svg")
         .attr("width", width)
         .attr("height", 50)
         .append("g")
         .attr("transform", `translate(${margin.left}, 10)`);

      categories.forEach((category, i) => {
         legend.append("rect")
            .attr("x", i * 150)
            .attr("y", 0)
            .attr("width", 15)
            .attr("height", 15)
            .attr("fill", categoryColors[category]);

         legend.append("text")
            .attr("x", i * 150 + 25)
            .attr("y", 10)
            .text(category)
            .style('font-size', '12px')
            .attr("alignment-baseline", "middle");
      });

      
      annotations.forEach(({ year, text, color, lineY1, lineY2, circleY, textXOffset, textYOffset }) => {
         const xPosition = x(year);

         // Draw line
         svg.append("line")
            .attr("x1", xPosition)
            .attr("x2", xPosition)
            .attr("y1", lineY1)
            .attr("y2", lineY2 )
            .attr("stroke", color)
            .attr("stroke-width", 2);

         // Draw circle
         svg.append("circle")
            .attr("cx", xPosition)
            .attr("cy", circleY - height)
            .attr("r", "3px")
            .attr("stroke", color)
            .attr("stroke-width", 2)
            .style("fill", "#fff");

         // Draw text
         svg.append("text")
            .attr("x", xPosition + textXOffset)
            .attr("y", textYOffset)
            .attr("text-anchor", "middle")
            .attr("fill", color)
            .style("font-size", "12px")
            .text(text);

    });
    } 
   
 </script>
 <div class="flex flex-col">
   <div id="chart"></div>
   <div id="legend2"></div>

</div>

 
 <style>
    /* Add styles if necessary */
 </style>
