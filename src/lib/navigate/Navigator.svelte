<script lang="ts">
    import { goto } from '$app/navigation';
    import { page } from '$app/stores'; // Access the current page's store
    import { derived, get } from 'svelte/store';

    // Define your pages in order
    const pages = ['/articles/5', '/articles/5/problem', '/articles/5/solution', '/articles/5/summer1' ,'/articles/5/hosts','/articles/5/hosts1','/articles/5/hosts2', '/articles/5/conclusion'];

    // Get the current page index dynamically based on the current path
    const currentPage = derived(page, ($page) => pages.indexOf($page.url.pathname));

    function handleKeydown(event: KeyboardEvent) {
        const currentIndex = get(currentPage); // Get the current index value from the store

        if (event.key === 'ArrowRight') {
            if (currentIndex === pages.length - 1) return; // Already at the last page
            const nextPageIndex = currentIndex + 1;
            goto(pages[nextPageIndex]);
        }

        if (event.key === 'ArrowLeft') {
            if (currentIndex <= 0) return; // Already at the first page
            const previousPageIndex = currentIndex - 1;
            goto(pages[previousPageIndex]);
        }
    }
</script>

<svelte:window on:keydown={handleKeydown} />
