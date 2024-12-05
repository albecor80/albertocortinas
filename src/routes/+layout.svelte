<script>
    import "../app.css";
    import Header from "$lib/components/Header.svelte";
    import { page } from "$app/stores";

    $: hideHeader = ['/articles/5', '/articles/5/problem','/articles/5/solution','/articles/5/summer1', '/articles/5/hosts', '/articles/5/hosts1', '/articles/5/hosts2', '/articles/5/conclusion'].includes($page.url.pathname);
</script>
<div class="flex flex-col h-full w-full mx-auto max-w-screen-xl">
    {#if !hideHeader}
        <Header />
    {/if}
    <slot />
</div>
  