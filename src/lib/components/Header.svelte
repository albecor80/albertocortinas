<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores'; // SvelteKit store to track route changes

    /**
	 * @type {string | null}
	 */
    let currentPath;

    // Function to update the active link styling based on the current path
    const updateActiveLink = () => {
        const menuLinks = document.querySelectorAll('.menu-link');
        menuLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('bg-turquoise', 'text-gray-50', 'font-bold');
                link.classList.remove('bg-white', 'text-gray-600');
            } else {
                link.classList.remove('bg-turquoise', 'text-gray-50', 'font-bold');
                link.classList.add('bg-white', 'text-gray-600');
            }
        });
    };

    // Runs only on the client after the component is mounted
    onMount(() => {
        currentPath = window.location.pathname; // Access window object only in browser
        updateActiveLink();
    });

    // Reactive block to update the active link when the route changes
    $: {
        if (typeof window !== 'undefined') {
            currentPath = $page.url.pathname;
            updateActiveLink();
        }
    }
</script>

<header class="container mx-auto top-0 h-32 flex w-full">
    <nav class="bg-white  w-full flex flex-col">
        <div class="container mx-auto px-6 py-4 flex items-center justify-between">
          <div class="flex mx-auto items-center space-x-8">
            <div class="flex space-x-6">
              <a href="/articles" class="menu-link tracking-widest text-center p-4 w-36 text-gray-600 ">ARTICLES</a>
              <a href="/projects" class="menu-link tracking-widest text-center p-4 w-36 text-gray-600 ">PROJECTS</a>
            </div>
            <a href="/" class="flex flex-col font-serif text-xl">
                <img src="/hero_picture.png" class="drop-shadow rounded-full h-16 w-16" alt="">
            </a>
            <div class="flex space-x-6">
              <a href="/about" class="menu-link tracking-widest text-center p-4 w-36 text-gray-600 ">ABOUT</a>
              <a href="/contact" class="menu-link tracking-widest text-center p-4 w-36 text-gray-600 ">CONTACT</a>
            </div>
          </div>
        </div>
        <div class="bg-turquoise h-px"></div>
        <div class="bg-turquoise h-px"></div>
      </nav>
</header>

