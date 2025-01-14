<script>
    import { onMount } from 'svelte';

    let images = []; // Para los equipos
    let fotos_jugadors = []; // Para los jugadores
    onMount(async () => {
      // Fetch de imágenes de equipos
      const res = await fetch('/api/images/teams');
      images = await res.json();
  
      // Fetch de imágenes de jugadores
      const jugadoresRes = await fetch('/api/images/players');
      fotos_jugadors = (await jugadoresRes.json()).slice(0,18);
      console.log(fotos_jugadors);
    });


  </script>
  
  <div class="flex min-h-screen items-center justify-center">
      <!-- Sección de equipos -->
      <a href="players/">

      <div class="bg-[url('img/etiqueta_jugadors.jpg')] m-2 w-[300px] h-[400px] border-4 border-slate-700 flex flex-col items-center justify-start">
          <h1 class="text-7xl text-slate-700 tracking-wider font-bebas mt-2">
              PLAYERS
          </h1>
          <div class="w-[90%] h-[2px] bg-slate-700"></div>
          <p class="m-2 text-sm text-slate-700 text-center italic font-baskerville">
              Every team has a story. Explore the journey of each team through the season.
          </p>
      </div>
        </a>
      <!-- Sección de jugadores -->
    <a href="teams/">
        <div class="bg-[url('img/etiqueta_equips.jpg')] m-2 w-[300px] h-[400px] border-4 border-slate-700 flex flex-col items-center justify-end">
            <p class="m-2 text-sm text-slate-700 text-center italic font-baskerville">
                Basketball is a team game but, sometimes, a single player can make the difference.
            </p>
            <div class="w-[90%] h-[2px] bg-slate-700"></div>
            <h1 class="text-7xl text-slate-700 font-bebas mt-2">
                TEAMS
            </h1>
        </div>
  
    </a>
  </div>
  