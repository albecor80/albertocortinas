export const ages = [
    {
        "country": "Ireland",
        "age": 26.9,
    },{
        "country": "Belgium",
        "age": 26.3,
    },{
        "country": "Luxembourg",
        "age": 26.9,
    },{
        "country": "Sweden",
        "age": 21.4,
    },{
        "country": "Finland",
        "age": 21.3,
    },{
        "country": "Denmark",
        "age": 21.7,
    },{
        "country": "Latvia",
        "age": 26.8,
    },{
        "country": "Poland",
        "age": 28.9,
    },{
        "country": "Estonia",
        "age": 22.7,
    },{
        "country": "Lithuania",
        "age": 24.7,
    },{
        "country": "Netherlands",
        "age": 23.0,
    },{
        "country": "France",
        "age": 23.4,
    },{
        "country": "Germany",
        "age": 23.8,
    },
    {
        "country": "Spain",
        "age": 30.3,
    },
    {
        "country": "Portugal",
        "age": 29.7,
    },
    {
        "country": "Italy",
        "age": 30.0,
    },
    {
        "country": "Malta",
        "age": 30.1,
    },
    {
        "country": "Austria",
        "age": 25.3,
    },
    {
        "country": "Czech Republic",
        "age": 25.9,
    },
    {
        "country": "Slovenia",
        "age": 29.4,
    },
    {
        "country": "Croatia",
        "age": 33.4,
    },
    {
        "country": "Slovakia",
        "age": 30.8,
    },
    {
        "country": "Romania",
        "age": 27.7,
    },
    {
        "country": "Hungary",
        "age": 27.1,
    },
    {
        "country": "Bulgaria",
        "age": 30.3,
    },
    {
        "country": "Greece",
        "age": 30.7,
    },
    {
        "country": "Cyprus",
        "age": 27.5,
    },

]

export const europeanAverage = 26.4;

export const ageDifferences = ages.map(d => ({
    ...d,
    difference: d.age - europeanAverage
})).sort((a, b) => b.difference - a.difference);
