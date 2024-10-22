<script>
    import "../app.css";
    import Header from "$lib/components/Header.svelte";
</script>
<div class="flex flex-col h-full w-full  mx-auto max-w-screen-xl">
    <Header />
    <slot />
</div>
  