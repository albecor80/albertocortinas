<script>
    import Dendrogram from "$lib/visuals/Dendrogram.svelte";

    let title = "Visualizing The Lord of the Rings Characters"
    let date = "2024-11-02"
    let author = "Alberto Cortinas"
    let summary = "Using a Circular Dendrogram to show the relationships between characters in the Lord of the Rings"


</script>

<div class="flex flex-col h-full w-2/3 mx-auto mt-8">
    <h1>
        {title}
    </h1>
    <p class="font-grotesque mt-0 flex justify-end text-gray-500">By {author},  {date}</p>
    <p class="font-grotesque mt-4 text-xl text-gray-500">"{summary}"</p>
    <div class="bg-gray-500 mt-4 h-px"></div>
    <div class="mt-4 mb-16">
        <Dendrogram />
    </div>
    <h3 class="mt-8">What is a Circular Dendrogram?</h3>
    <p>The circular dendrogram is a type of hierarchical visualization that originated in biology, traditionally used to show evolutionary relationships among species. In this visualization, nodes are arranged in a circular layout, with connections indicating hierarchical relationships. Each node represents a category or individual, and connections reveal relationships within and across levels.</p>
    <h3 class="mt-8">The Lord of the Rings Dendrogram</h3>
    <p>In our example, we use a circular dendrogram to visualize characters from The Lord of the Rings, organized by type (Wizards, Elves, Men, etc.). Each character is represented as a node, with node size reflecting their significance in the story. This approach highlights the major players in each group, helping us quickly see which characters are most influential within their category.</p>
    <h3 class="mt-8">Data Requirements and Limitations</h3>
    <p>A circular dendrogram is best suited for hierarchical, qualitative data. It works well when the dataset is limited in size, as too many nodes can make the visualization difficult to interpret. For optimal clarity, this Lord of the Rings dendrogram includes only key characters, allowing for a more focused view of character relationships within and across typologies.</p>
    <h3 class="mt-8">Purpose and Insights</h3>
    <p>The goal of this dendrogram is to provide an engaging and easy-to-follow look at The Lord of the Rings character types and their relative prominence within the saga. This visualization allows fans to explore the connections among characters and see which figures stand out in their categories, making it ideal for storytelling and educational purposes.</p>


</div>

