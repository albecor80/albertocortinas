export const ages = [
    {
        "country": "Ireland",
        "age": 24.7,
    },{
        "country": "Belgium",
        "age": 29.0,
    },{
        "country": "Luxembourg",
        "age": 26.9,
    },{
        "country": "Sweden",
        "age": 22.3,
    },{
        "country": "Finland",
        "age": 15.3,
    },{
        "country": "Denmark",
        "age": 25.1,
    },{
        "country": "Latvia",
        "age": 16.3,
    },{
        "country": "Poland",
        "age": 23.4,
    },{
        "country": "Estonia",
        "age": 21.7,
    },{
        "country": "Lithuania",
        "age": 8.6,
    },{
        "country": "Netherlands",
        "age": 18.4,
    },{
        "country": "France",
        "age": 18.6,
    },{
        "country": "Germany",
        "age": 16.8,
    },
    {
        "country": "Spain",
        "age": 25.6,
    },
    {
        "country": "Portugal",
        "age": 58.1,
    },
    {
        "country": "Italy",
        "age": 35.5,
    },
    {
        "country": "Austria",
        "age": 18.3,
    },
    {
        "country": "Czech Republic",
        "age": 24.9,
    },
    {
        "country": "Slovenia",
        "age": 27.3,
    },
    {
        "country": "Slovakia",
        "age": 36.9,
    },
    {
        "country": "Romania",
        "age": 26.8,
    },
    {
        "country": "Hungary",
        "age": 33.7,
    },
    {
        "country": "Bulgaria",
        "age": 30.3,
    },
    {
        "country": "Greece",
        "age": 27.3,
    },
    {
        "country": "Cyprus",
        "age": 22,
    },

]

export const europeanAverage = 26.4;

export const ageDifferences = ages.map(d => ({
    ...d,
    difference: d.age - europeanAverage
})).sort((a, b) => b.difference - a.difference);
