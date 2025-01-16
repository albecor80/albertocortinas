<script>
    export let pages = [];
    export let currentPageIndex = 0;
  </script>
  
  <div class="flex items-center justify-center space-x-4">
    {#each pages as page, index}
      <div class="flex items-center">
        <div
          class={`h-24 w-24 rounded-full flex items-center justify-center text-gray-600 font-bold text-sm bg-gray-300 border-2 ${
            index <= currentPageIndex ? 'border-gray-700 bg-gray-700 text-gray-200 ' : 'border-black-gray-200 text-gray-400'
          }`}
        >
          {page.title}
        </div>
        {#if index < pages.length - 1}
          <div
            class={`h-1 w-16 border-2 border-gray-700 ${
              index < currentPageIndex ? 'border-gray-700 ' : 'border-gray-200'
            }`}
          ></div>
        {/if}
      </div>
    {/each}
  </div>
  