<script>
    import { tick } from 'svelte'; // To wait for DOM updates

    import { onMount } from 'svelte';
    import { page } from '$app/stores'; // SvelteKit store to track route changes
    import Equip from "$lib/components/Equip.svelte";
    import equips_ordenats from "$lib/data/equips.js";
	import Titulo from '$lib/components/Titulo.svelte';
	import LocalSVG from '$lib/components/LocalSVG.svelte';
	import VisitantSvg from '$lib/components/VisitantSVG.svelte';
	import LocalSvg from '$lib/components/LocalSVG.svelte';

    /**
     * @type {string | null}
     */
     let currentPath;

    // Function to update the active link styling
    const updateActiveLink = async () => {
        await tick(); // Ensure DOM is updated
        const menuLinks = document.querySelectorAll('.menu-link');
        menuLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('text-slate-700', 'border-slate-700', 'font-bold');
                link.classList.remove( 'border-white','text-slate-300');
            } else {
                
                link.classList.add('border-white', 'text-slate-300');
                link.classList.remove('text-slate-700', 'border-slate-700', 'font-bold');
            }
        });
    };
    onMount(() => {
        updateActiveLink();
    });

    // Reactive block to update the active link when the route changes
    $: currentPath = $page.url.pathname;

</script>

<header class="container mx-auto top-0 h-10 flex mb-4 w-full">
<nav class="bg-white w-full flex flex-col">
    <div class="container mx-auto px-6 flex items-center justify-between">
        <div class="flex mx-auto items-center space-x-8">
            <div class="flex space-x-6">
                <a href="/teams" class="menu-link tracking-widest  text-center p-4 w-36 text-slate-700">WINS/LOSSES</a>
                <a href="/teams/points" class="menu-link tracking-widest text-center p-4 w-36 text-slate-700">POINTS</a>
            </div>
            <div class="flex space-x-6">
                <a href="/about" class="menu-link tracking-widest  text-center p-4 w-36 text-slate-700">ABOUT</a>
                <a href="/contact" class="menu-link tracking-widest  text-center p-4 w-36 text-slate-700">CONTACT</a>
            </div>
        </div>
    </div>
    <div class="bg-turquoise h-px"></div>
    <div class="bg-turquoise h-px"></div>
</nav>
</header>

<div class="flex container items-center justify-between mx-auto h-screen ">
    <div class="w-1/2 flex flex-col mx-auto h-full">
        <Titulo titulo="Wins and losses through the season" subtitulo="Each team did his own journey through the season, with some good moments and also bad ones"/>
        <div class="flex pt-1 pl-1 flex-col h-full">
            {#each equips_ordenats as equip}
                <div class="flex">
                    <Equip nom={equip.nom} imatge={equip.img} width="w-7" height="h-7" />
                    <div class="flex ml-4 my-auto gap-1">
                        {#each equip.matches as match}
                            <div
                                class="w-2 h-2 md:w-3 md:h-3"
                                class:bg-green-500={match === 1}
                                class:bg-gray-300={match === 0}
                            ></div>
                        {/each}
                    </div>
                </div>
            {/each}
        </div>

    </div>
    <div class="flex flex-col w-1/2 h-full ">
        <Titulo titulo="BEST AND WORST STREAKS" subtitulo="Every team experienced highs and lows, with impressive winning streaks and challenging losing runs defining their season." />
        <div class="flex ">
            <div class="flex items-center justify-center flex-col w-1/2">
                <Equip nom="Unicaja" imatge="img/equips/unicaja.png" width="w-44" height="h-44" />
                <div class="flex flex-col">
                    <div class="flex items-center">
                        <svg class="m-2" height="20" width="20" style={{ fill: 'green', verticalAlign: 'middle' }}>
                            <polygon points="10,0 20,20 0,20" fill="#48bb78" />
                        </svg>
                    
                        <h2 class="text-4xl font-baskerville italic">14 wins</h2>
    
                    </div>
                    <p class="text-lg text-center font-baskerville italic"> starting at week 5</p>

                </div>
            </div>
            <div class="flex flex-col items-center w-1/2">
                <Equip nom="Zunder Palencia" imatge="img/equips/palencia.png" width="w-52" height="h-52" />
                <div class="flex flex-col">
                    <div class="flex items-center">
                        <svg class="m-2" height="20" width="20" style={{ fill: 'green', verticalAlign: 'middle' }}>
                            <polygon points="0,0 20, 0 10,20" fill="#EE3333" />
                        </svg>
                        <h2 class="text-4xl font-baskerville italic">10 losses</h2>
                    </div>
                        <p class="text-lg text-center font-baskerville italic"> starting at week 16</p>
                </div>
            </div>
        </div>
        <div class="flex  h-full mt-8 flex-col justify-center my-auto">
            <Titulo titulo="HOME AND AWAY" subtitulo="Some teams were stronger at home, while others were more successful on the road." />
            <div class="flex mx-auto mt-8 h-full">
                <div class="flex flex-col">
                    <div class="flex">
                        <LocalSvg /><LocalSvg /><LocalSvg /><LocalSvg /><LocalSvg /><LocalSvg /><VisitantSvg /><VisitantSvg /><VisitantSvg /><VisitantSvg />

                    </div>
                    <di class="text-4xl text-center font-baskerville italic">
                        59% wins at home
                    </div>
                </div>
            </div>
        </div>


    </div>  
    
    
