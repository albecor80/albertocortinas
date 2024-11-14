<script>
    import Card from "$lib/components/Card.svelte";
    const articles = [
        { id: 1, title: 'Bad practices in data visualization', img: 'bad_visual_front.jpg' },
        { id: 2, title: 'Visualizing The Lord of the Rings Characters', img: 'dendrogram.png' },
        { id: 3, title: 'A Life Timeline: Major Milestones and Time Allocation', img: 'timeline.png' },
        { id: 4, title: 'Mapping Bar Density in Badalona with a Contour Plot', img: 'contour.png' },
    ];
    </script>
<section class="container w-10/12 mx-auto">
    <h1 class=" text-center">My writings</h1>
    <p class="pb-6 text-center text-gray-500 mt-2 ">A collection of articles I've been writing as I am learning about data and visualization</p>
    <!-- 3-column grid with fixed gap -->
    <ul class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4 justify-items-center">
      {#each articles as article}
        <li class="w-full">
          <!-- Card component with consistent spacing -->
          <Card id={article.id} title={article.title} img={article.img} />
        </li>
      {/each}
    </ul>
  </section>
  

