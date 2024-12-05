<script>

    import IconArray from "$lib/visuals/IconArray.svelte";
	import RadialLines from "$lib/visuals/RadialLines.svelte";
    import TimelineFull from "$lib/visuals/TimelineFull.svelte";
    const series = [
    {
        name: 'City',
        color: '#96DBC9',
        values: [
            { date: '2015-07-01', value: 68.9 },
            { date: '2015-08-01', value: 51.1 },
            { date: '2015-09-01', value: 44.5 },
            { date: '2015-10-01', value: 39.5 },
            { date: '2015-11-01', value: 24.7 },
            { date: '2015-12-01', value: 42.2 },
            { date: '2016-01-01', value: 32.6 },
            { date: '2016-02-01', value: 39.6 },
            { date: '2016-03-01', value: 36.7 },
            { date: '2016-04-01', value: 43.5 },
            { date: '2016-05-01', value: 39.7 },
            { date: '2016-06-01', value: 44.2 },
            { date: '2016-07-01', value: 33.5 },
            { date: '2016-08-01', value: 37.2 },
            { date: '2016-09-01', value: 40.9 },
            { date: '2016-10-01', value: 46.7 },
            { date: '2016-11-01', value: 44.3 },
            { date: '2016-12-01', value: 43.8 },
            { date: '2017-01-01', value: 44.5 },
            { date: '2017-02-01', value: 37.9 },
            { date: '2017-03-01', value: 38.0 },
            { date: '2017-04-01', value: 49.3 },
            { date: '2017-05-01', value: 49.0 },
            { date: '2017-06-01', value: 45.9 },
            { date: '2017-07-01', value: 37.4 },
            { date: '2017-08-01', value: 36.0 },
        ]
    },
    {
        name: 'Resort',
        color: '#dd6fb2',
        values: [
            { date: '2015-07-01', value: 23.5 },
            { date: '2015-08-01', value: 26.3 },
            { date: '2015-09-01', value: 34.6 },
            { date: '2015-10-01', value: 26.3 },
            { date: '2015-11-01', value: 17.1 },
            { date: '2015-12-01', value: 24.6 },
            { date: '2016-01-01', value: 13.7 },
            { date: '2016-02-01', value: 27.2 },
            { date: '2016-03-01', value: 21.0 },
            { date: '2016-04-01', value: 28.5 },
            { date: '2016-05-01', value: 26.9 },
            { date: '2016-06-01', value: 27.9 },
            { date: '2016-07-01', value: 31.9 },
            { date: '2016-08-01', value: 34.5 },
            { date: '2016-09-01', value: 30.0 },
            { date: '2016-10-01', value: 28.8 },
            { date: '2016-11-01', value: 21.0 },
            { date: '2016-12-01', value: 24.4 },
            { date: '2017-01-01', value: 15.8 },
            { date: '2017-02-01', value: 24.7 },
            { date: '2017-03-01', value: 25.6 },
            { date: '2017-04-01', value: 31.0 },
            { date: '2017-05-01', value: 31.3 },
            { date: '2017-06-01', value: 37.8 },
            { date: '2017-07-01', value: 37.9 },
            { date: '2017-08-01', value: 38.7 },        ]
    }   
    ];
    const city_weekly ={
        "mon": 38.9,
        "tue": 38.5,
        "wed": 42.2,
        "thu": 49.1,
        "fri": 44.6,
        "sat": 44.1,
        "sun": 34.6
    };
    const resort_weekly ={
        "mon": 25.9,
        "tue": 23.9,
        "wed": 24.2,
        "thu": 26.2,
        "fri": 32.6,
        "sat": 33.2,
        "sun": 28.6
    }
    const city_monthly ={
        "jan": 40.2,
        "feb": 38.7,
        "mar": 37.4,
        "apr": 46.6,
        "may": 44.9,
        "jun": 45.1,
        "jul": 41.3,
        "aug": 40.5,
        "sep": 42.6,
        "oct": 43.5,
        "nov": 38.8,
        "dec": 43.2
    };
    const list_resort_monthly = [
        15.0,
        25.9,
        23.1,
        29.7,
        33.4,
        31.7,
        33.7,
        33.7,
        32.3,
        27.7,
        19.2,
        24.5
    ];

    const list_city_monthly = [
        40.2,
        38.7,
        37.4,
        46.6,
        44.9,
        45.1,
        41.3,
        40.5,
        42.6,
        43.5,
        38.8,
        43.2
    ];

    const resort_monthly ={
        "jan": 15.0,
        "feb": 25.9,
        "mar": 23.1,
        "apr": 29.7,
        "may": 33.4,
        "jun": 31.7,
        "jul": 33.7,
        "aug": 33.7,
        "sep": 32.3,
        "oct": 27.7,
        "nov": 19.2,
        "dec": 24.5
    };

    let serie1 = list_city_monthly;
    let serie2 = list_resort_monthly;

</script>


<div class="flex flex-col w-full min-h-screen">
    <div class="flex flex-col p-4 pl-24 pr-24 bg-[#96DBC9]">
        <h1 class="pt-8">Evolution of cancellations in time</h1>
        <p class="flex mx-auto text-lg text-gray-600">City hotels reservation cancellations are typically higher than Resorts with an exception in summer months</p>
    </div>

    <div class="flex  flex-col p-4 mt-8">
        <TimelineFull {series} />
    </div>
</div>




