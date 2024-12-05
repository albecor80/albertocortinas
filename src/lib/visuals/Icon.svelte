<script>
    export let color = '#000';
    export let percentage = 100;

</script>

<div
  style="background-color: {color}; opacity: {2 * (percentage - 10) / 100};"
  class="flex items-center justify-center w-8 h-8 relative"
>
  <!-- Capa de texto separada -->
  <p
    class="absolute text-[0.6rem] text-black"
    style="opacity: 1;"
  >
    {percentage}%
  </p>
</div>


