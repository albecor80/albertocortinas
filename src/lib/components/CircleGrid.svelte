<script>
    export let filledCircles = 0; // Número de círculos rellenos en naranja
    export let highlightedCircle = 0; // Círculo con borde negro
  
    const rows = 10;
    const cols = 10;
  
    // Generar la matriz de círculos
    const circles = Array.from({ length: rows * cols }, (_, index) => {
      // Calcular índice en la disposición correcta
      const row = Math.floor(index / cols);
      const col = index % cols;
      const adjustedIndex = (rows - 1 - row) * cols + col; // Ajustar para empezar desde abajo y avanzar horizontalmente
  
      return {
        filled: adjustedIndex < filledCircles,
        highlighted: adjustedIndex === highlightedCircle - 1, // Ajustar índice para 1-based
      };
    });
</script>
<div class="flex flex-col">
    <div class="grid grid-cols-10 gap-1 m-2">
        {#each circles as circle, i}
            <div
            class={`w-4 h-4 rounded-full ${
                circle.filled ? 'bg-orange-500' : 'bg-gray-300'
            } ${circle.highlighted ? ' bg-gray-500' : ''}`}
            ></div>
        {/each}
    </div>
    <div class="font-baskerville italic text-sm">
        <div class="h-[2px] w-[90%] items-center justify-center mx-auto bg-gray-300 " />

        <p class="text-orange-500 font-baskerville italic">team's percentage</p>
        <p class="text-gray-500 font-baskerville italic">average league percentage</p>
        
    </div>
</div>

