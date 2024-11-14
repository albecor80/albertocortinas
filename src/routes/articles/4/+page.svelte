<script>
    import ContourPlot from "$lib/visuals/ContourPlot.svelte";

    let title = "Mapping Bar Density in Badalona with a Contour Plot"
    let date = "2024-11-12"
    let author = "Alberto Cortinas"
    let summary = "Using a contour plot to visualize the density of bars in Badalona"


</script>

<div class="flex flex-col h-full w-2/3 mx-auto mt-8">
    <h1>
        {title}
    </h1>
    <p class="font-grotesque mt-0 flex justify-end text-gray-500">By {author},  {date}</p>
    <p class="font-grotesque mt-4 text-xl text-gray-500">"{summary}"</p>
    <div class="bg-gray-500 mt-4 h-px"></div>
    <div class="mt-4 mb-16">
        <ContourPlot />
    </div>
    <h3 class="mt-8">What is a Contour Plot?</h3>
    <p>Contour plots, originally developed in cartography, are commonly used to show variations of a continuous variable across a 2D surface. They display isovalue lines (contours) that connect points with the same data value, revealing areas with varying levels of intensity. This technique is widely used in geography, weather forecasting, and urban analysis.</p>
    <h3 class="mt-8">Badalona Bar Density Contour Plot</h3>
    <p>In this example, a contour plot visualizes the density of bars in Badalona, a city known for its vibrant social scene. By mapping the density of bars in different areas, we can identify zones with higher or lower concentrations. Each contour line represents areas with the same bar density, making it easy to spot hotspots.</p>
    <h3 class="mt-8">Data Requirements and Limitations</h3>
    <p>Contour plots require quantitative data distributed across a 2D plane. For this visualization, we use geographic coordinates (latitude and longitude) to mark the location of each bar. While contour plots can sometimes be limited by sparse data, a sufficient number of data points ensures an accurate and insightful representation.</p>
    <h3 class="mt-8">Purpose and Insights</h3>
    <p>The goal of this contour plot is to uncover patterns in the distribution of bars across Badalona, highlighting high-density areas that may be popular social hubs. This visualization is particularly valuable for business and urban planning, as it reveals areas with high competition or social interest. It serves as a practical tool for understanding urban trends and identifying opportunities for business placement or urban development.</p>
    <div class="mt-16"></div>

</div>

