<script>
    import Timeline from "$lib/visuals/Timeline.svelte";
    let title = "A Life Timeline: Major Milestones and Time Allocation"
    let date = "2024-11-08"
    let author = "Alberto Cortinas"
    let summary = "Visualizing the key events in my life and how time is spent across different areas"
</script>

<div class="flex flex-col h-full w-2/3 mx-auto mt-8">
    <h1>
        {title}
    </h1>
    <p class="font-grotesque mt-0 flex justify-end text-gray-500">By {author},  {date}</p>
    <p class="font-grotesque mt-4 text-xl text-gray-500">"{summary}"</p>
    <div class="bg-gray-500 mt-4 h-px"></div>
    <div class="mt-4 mb-16">
        <Timeline />
    </div>
    <h3 class="mt-8">What is a Timeline Visualization?</h3>
    <p>Timelines are used to display a chronological sequence of events along a continuous line, with markers or annotations indicating specific moments. They have been used historically to show everything from project milestones to historical events. In our case, the timeline serves as a visual diary, showing the major milestones and the distribution of time spent on different areas of life over the years.</p>
    <h3 class="mt-8">Personal Timeline Overview</h3>
    <p>This timeline begins at age 18 and follows significant life events, or milestones, year by year. In addition to marking important events, it includes a breakdown of time dedicated to various pursuits (e.g., hours spent working, with family, studying, etc.). For instance, in 2010, we see 9 hours allocated to work and 2 to family each day, reflecting shifts in priorities over time.</p>
    <h3 class="mt-8">Data Requirements and Limitations</h3>
    <p>Timelines work best with chronological data, including both quantitative and qualitative details for each event. They can become cluttered if overloaded with events, so it's advisable to focus on key milestones. Here, we’ve chosen only the most impactful events to create a clear, easily navigable visualization that still captures meaningful trends in time allocation.</p>
    <h3 class="mt-8">Purpose and Insights</h3>
    <p>This timeline aims to provide a comprehensive view of life’s key events and how time commitments change with age and circumstance. By showcasing both milestones and time allocation, the timeline offers a unique look at the evolution of priorities, helping to identify patterns and shifts that might otherwise go unnoticed. It's a powerful tool for both reflection and planning.</p>


</div>

