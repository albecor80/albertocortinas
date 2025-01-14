<script>
    export let nom;
    export let imatge;
    export let width;
    export let height;
    let isHovered = false;

</script>
<!-- svelte-ignore a11y_interactive_supports_focus -->
<div
  class="flex my-auto mb-1"
  role="button"
  tabindex="0"
  on:mouseover={() => isHovered = true}
  on:mouseleave={() => isHovered = false}
  on:focus={() => isHovered = true}
  on:blur={() => isHovered = false}
  on:keydown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      // Simulate a click or other action
      isHovered = !isHovered;
    }
  }}
>

  <div class=" {width} {height} overflow-hidden">
    <img
      class="w-full h-full transition-all duration-300 ease-in-out"
      class:brightness-100={isHovered}
      class:brightness-75={!isHovered}
      src={imatge}
      alt={nom}
    />
  </div>
</div>
