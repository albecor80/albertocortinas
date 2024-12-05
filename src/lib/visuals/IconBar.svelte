<script>
    export let percentage = 35; // Cambia este valor para probar diferentes porcentajes
    const totalIcons = 10;
  
    $: coloredIcons = Math.floor((percentage / 100) * totalIcons);
    $: fractionalPart = ((percentage / 100) * totalIcons) % 1;

  </script>
  
  <div class="grid grid-cols-12 gap-1">
    {#each Array(10).fill(0) as _, index}
      <div class="icon">
        {#if index < coloredIcons}
            <div class="w-16 h-16 bg-[#96DBC9]"></div>
        {:else if index === coloredIcons}
          <!-- Cuadrado parcialmente coloreado -->
          <div class="relative w-16 h-16 overflow-hidden">
            <div
              class="absolute top-0 left-0 h-full"
              style="width: {fractionalPart * 100}%; background-color: #96DBC9;"
            ></div>
            <div
              class="absolute top-0 right-0 h-full"
              style="width: {(1 - fractionalPart) * 100}%; background-color: #ddd;"
            ></div>
          </div>
        {:else}
          <!-- Cuadrado completamente gris -->
          <div class="w-16 h-16 bg-[#ddd]"></div>
          {/if}
      </div>
    {/each}
  </div>
  
  <style>
    .flex {
      display: flex;
      gap: 4px; /* Espaciado entre cuadrados */
    }
  
    .icon {
      width: 24px;
      height: 24px;
      display: flex;
      overflow: hidden;
    }
  
    .colored {
      background-color: #f39c12; /* Color del cuadrado */
      height: 100%;
    }
  
    .gray {
      background-color: #ddd; /* Color gris */
      height: 100%;
    }
  
    .partial {
      display: flex;
      width: 100%;
      height: 100%;
    }
  </style>
  