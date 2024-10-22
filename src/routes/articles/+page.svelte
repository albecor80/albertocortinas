<script>
    import Card from "$lib/components/Card.svelte";
    const articles = [
        { id: 1, title: 'Bad practices in data visualization', img: 'bad_visual_front.jpg' },
        { id: 2, title: 'Good practices in data visualization', img: 'good_practice_front.jpg' },
    ];
    </script>
<section class="container w-10/12 mx-auto">
    <h1 class="text-2xl font-bold mb-6 text-center">Articles</h1>
  
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
  