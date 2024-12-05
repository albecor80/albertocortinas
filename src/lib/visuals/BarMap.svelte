<script>
    let data = [
      { category: 'Umbrellas', value: 3.9*3.5, value2: "38%", color: '#dd6fb2', icon: '\uf5ca' }, // FontAwesome Unicode for umbrella
      { category: 'Suitcases', value: 3.7*3.5, value2: "36%", color: '#96DBC9', icon: '\uf0b1' }, // FontAwesome Unicode for suitcase
    ];
    let svgWidth = 500;
    let svgHeight = 300;
    let iconSize = 24; // Size of each icon
    let spacing = 6; // Space between icons
    let barSpacing = 10; // Vertical space between bars
  </script>
  <div class="flex flex-col w-full h-full items-center justify-center mx-auto my-auto">
    <div class="h-24"></div>
    <svg class="ml-16 flex w-full h-full items-center justify-center mx-auto my-auto" width={svgWidth} height={svgHeight}>
        {#each data as { category,value2, value, color, icon }, i}
          <g transform={`translate(0, ${i * (iconSize + barSpacing)})`}>
            {#each Array(Math.floor(value)) as _, j}
              <!-- Full icons -->
              <text
                x={(j * (iconSize + spacing))}
                y={iconSize}
                font-size={iconSize}
                fill={color}
                style="font-family: FontAwesome;"
              >
                {icon}
              </text>
            {/each}
      
            {#if value % 1 > 0}
              <!-- Fractional icon -->
              <defs>
                <clipPath id={`clip-${i}`}>
                  <rect
                    x={Math.floor(value) * (iconSize + spacing)}
                    y="0"
                    width={(iconSize * (value % 1))}
                    height={iconSize}
                  />
                </clipPath>
              </defs>
              <text
                x={Math.floor(value) * (iconSize + spacing)}
                y={iconSize}
                font-size={iconSize}
                fill={color}
                style="font-family: FontAwesome;"
                clip-path={`url(#clip-${i})`}
              >
                {icon}
              </text>
              <text
                x={(Math.floor(value) + (value % 1 > 0 ? 1 : 0)) * (iconSize + spacing)}
                y={iconSize *0.65}
                font-size="16"
                fill={color}
                alignment-baseline="middle"
            >
                {value2}
                </text> 
            {/if}
          </g>
        {/each}
      </svg>
    
  </div>
  