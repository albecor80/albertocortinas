<script lang="ts">
    const fechaNacimiento = new Date(1980,9,28);
    const añoActual = new Date().getFullYear();


    function getTodayWeekday() {
        const weekdays = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
        return weekdays[new Date().getDay()];
    }

    function calcularEdad(fechaNacimiento: Date) {
        const today = new Date();
        let age = today.getFullYear() - fechaNacimiento.getFullYear();
        const monthDiff = today.getMonth() - fechaNacimiento.getMonth() +1;
        const dayDiff = today.getDate() - fechaNacimiento.getDate();
        console.log(age);
        console.log(monthDiff, dayDiff);
        // Si aún no ha pasado su cumpleaños este año, restar 1 a la edad
        if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
            age--;
        }

        return age;
    }

    $: edad = calcularEdad(fechaNacimiento);
    $: diaSemana = getTodayWeekday();
    $: mensaje = 
        añoActual === 2025 ? "Este año me he propuesto " :
        añoActual === 2026 ? "El año pasado me propuse " :
        "En 2025 me propuse ";

</script>

<div class="flex text-gray-700 font-baskerville text-md leading-7 mt-16 flex-col w-1/2 text-center mx-auto">

    <p class=" ">
        Hola 👋 ¡Feliz {diaSemana}!
    </p>

    <p class="mt-8" >
        Mi nombre es Alberto Cortinas
    </p>
    <p class="mt-8" >
        Tengo {edad} años y vivo en Badalona con M, mi persona favorita, y mis dos hijos D y E.
    </p>

    <p class="mt-8">
        Soy ingeniero industrial de formación y tras años trabajando en diferentes sectores, actualmente me dedico a realizar proyectos relacionados con datos e inteligencia artificial.
    </p>
    <p class="mt-8">
        Si tuviera que definirme con una sola palabra, sería curioso. Me encanta aprender cosas 
        nuevas y enfrentarme a nuevos retos. Cuando encuentro algo que me gusta especialmente o me llama la atención,
        tengo la necesidad de investigar y aprender todo lo que pueda sobre ello... ¿cómo se hace? ¿por qué? ¿para qué?
    </p>
    <p class="mt-8">
        {mensaje} destinar una parte del tiempo que dedico a aprender sobre temas que me interesan (y el que pierdo en cosas inútiles...) 
        a escribir sobre ellos y compartirlo
    </p>
    <p class="mt-8">
        ¿Y cuáles son estos temas? Pues principalmente datos e inteligencia artificial e historia, pero vamos a empezar
        por el principio: aprender a parar, reflexionar de forma pausada y escribir en mi primer newsletter <a href="https://laintrospectiva.substack.com" class="underline decoration-4 text-rose-400 decoration-rose-400 underline-offset-6">La Introspectiva</a>
    </p>

</div>


<style>
@reference "tailwindcss/theme";
:global(html) {
    background-color: theme(--color-white);
}
</style>