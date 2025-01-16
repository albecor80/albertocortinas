<script>
  import { createEventDispatcher } from 'svelte';
  export let equip;
  export let isHovered = false;
  export let isSelected = false;
  export let width = 'w-12'; // Default width
  const dispatch = createEventDispatcher();

  // Handler for click events
  const handleClick = () => {
      dispatch('select', equip);
  };

  // Handler for keyboard events (Enter and Space)
  const handleKeyDown = (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault(); // Prevent default scrolling behavior for Space
          dispatch('select', equip);
      }
  };
</script>

<style>
  /* Optional: Add any component-specific styles here */
  .equip-card {
      transition: border-color 0.3s ease-in-out;
  }
</style>

<div
  class="equip-card flex items-center cursor-pointer border-2 {isSelected ? 'border-blue-500' : 'border-transparent'} rounded transition-colors duration-300 ease-in-out"
  role="button"
  tabindex="0"
  aria-pressed={isSelected}
  on:click={handleClick}
  on:keydown={handleKeyDown}
  on:mouseover={() => isHovered = true}
  on:mouseleave={() => isHovered = false}
  on:focus={() => isHovered = true}
  on:blur={() => isHovered = false}
>
  <div class="{width} overflow-hidden rounded-full">
      <img
          class="w-full h-full object-cover transition-all duration-300 ease-in-out"
          class:brightness-100={isHovered}
          class:brightness-75={!isHovered}
          src={equip.img}
          alt={equip.nom}
      />
  </div>
</div>
