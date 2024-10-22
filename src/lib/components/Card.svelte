<script>
    export let title;
    export let img;
    export let id;

</script>

<a href={`/articles/${id}`} class="relative block w-64 h-64 bg-black group">
    <div>
        <img src={img} alt={title} class="w-full h-full object-cover">
        <p class="text-white">{title}</p>
    </div>
    
    <!-- Overlay and text on hover -->
    <div class="absolute inset-0 bg-turquoise bg-opacity-70 flex justify-center items-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
        <p class="text-white text-center font-bold text-xl">{title}</p>
    </div>
</a>