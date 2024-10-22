<script>
    import MapWithBars from "$lib/visuals/MapWithBars.svelte";

    let title = "Bad practices in data visualization"
    let date = "2024-10-15"
    let author = "Alberto Cortinas"
    let summary = "Criticism of a data visualization proposal that could be improved"
</script>

<div class="flex flex-col h-full w-2/3 mx-auto mt-16">
    <h1>
        {title}
    </h1>
    <p class="font-grotesque mt-0 flex justify-end text-gray-500">By {author},  {date}</p>
    <p class="font-grotesque mt-4 text-xl text-gray-500">"{summary}"</p>
    <div class="bg-gray-500 mt-4 h-px"></div>
    <div class="mt-4 mb-16">

        <p>
            The visualization I've chosen to do this study on bad practices in data visualization is this publication from <span class="italic">Eurostat</span> in which the creator wants to answer the question *When Europeans fly nest?*.
        </p>
        <img src="/bad_practice.webp" alt="Bad practice in data visualization" class="mx-auto w-2/3 mt-4">
        <p>
            The source data is the average age at which young people leave the parental house in several european countries, and the technical solution that the creator has implemented is a bubble chart where every country is a bubble and each bubble has:
        </p>
        <ul class="ml-8 mt-5 list-disc">
            <li>
                The name of the country
            </li>
            <li>
                The average age
            </li>
            <li>
                A color defining the cluster of age that the country belongs to.
            </li>
            <li>
                The bubble diameter correlated to the age (bigger bubble for countries with grater age).
            </li>
        </ul>
        <p>
        The problems I see in this approach are: 
        </p>
        <h3 class="mt-6">

            It is not as self-explanatory as it should
        </h3>
        <p>
            It is difficult to understand that the bubble are located in the place the country is in the real world as the <span class="font-bold">shape of the visual</span> 
            is far from the shape of Europe. In addition, <span class="font-bold">color scales</span>  do not help the user to see which cluster has greater average age
            than the other: <span class="italic">why do green countries leave parent house at older age than blue ones?</span>. Some different colors are similar 
            and they are difficult to differentiate (blue vs violet).

        </p>
        <h3 class="mt-6">
            Difficulty in contextualizing data
        </h3>
        <p>
            This visual does not help to easily answer some questions like:
        </p>
        <ul class="ml-8 mt-5 list-disc">
            <li>
                Which is the country with people leaving parental home older? And younger?
            </li>
            <li>
                What's the difference between countries?
            </li>
            <li>
                Which is the position vs European average?
            </li>
        </ul>
        <p>
            A good visualization must help comparing data of different countries and infer relationships between them

        </p>    
        <h3 class="mt-6">

            My proposal
        </h3>
        <p>
            My proposal to improve the visual, as it's representing geographical data, is to present it using a <span class="font-bold">colorpleth map</span> in which each country will be painted with a color saturation that represents the average 
            age at wich young people leave the parental household. 
        </p>

        <p>

            The color scale will be a gradient from blue to white, where blue represents the youngest age and white the oldest. 
            The user can hover over the countries to see the detailed data.
        </p>

        <p>

            I will add a bar graph that will rank all the countries in descendant order and it will be easy to see the difference versus European averages.
        </p>

        <p>

            The legend will be placed at the bottom of the map to help the user understand the color scale.

        </p>
        <div class="mt-8">
            <MapWithBars />

        </div>

        <p>
            With this approach, I improve some aspects of the visual:
        </p>
        <ul class="ml-8 mt-5 list-disc">
            <li>
                It is easier to identify each country
            </li>
            <li>
                User can infer relationships between data (mediterranean, nordic)
            </li>
            <li>
                Comparison of different countries it is more clear and easy
            </li>
    </div>


</div>