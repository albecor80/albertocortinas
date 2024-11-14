
<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { afterUpdate } from 'svelte';

    let locations = [];

    let map;
    let mapReady = false;

    function initMap() {
        console.log("initMap called");
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 41.45, lng: 2.23 },
            zoom: 13,
        });
        mapReady = true;
        plotContours();
    }

    function plotContours() {
        console.log("plotContours called");

        if (!mapReady || locations.length === 0) {
            console.log("Waiting for map or locations to be ready");
            return;
        }

        const overlay = new google.maps.OverlayView();

        overlay.onAdd = function () {
            const layer = d3.select(this.getPanes().overlayMouseTarget)
                .append("div")
                .attr("class", "contour-layer");

            overlay.draw = function () {
                const projection = overlay.getProjection();
                if (!projection) {
                    console.error("Projection is not available in draw");
                    return;
                }

                const dataPoints = locations.map(location => {
                    const latLng = new google.maps.LatLng(location.latitude, location.longitude);
                    const point = projection.fromLatLngToDivPixel(latLng);
                    return [point.x, point.y];
                });
                console.log("Data points:", dataPoints);
                const contourData = d3.contourDensity()
                    .x(d => d[0])
                    .y(d => d[1])
                    .size([map.getDiv().offsetWidth, map.getDiv().offsetHeight])
                    .bandwidth(30)(dataPoints);

                layer.selectAll("path").remove();
                
                // Adding paths for contours
                layer.selectAll("path")
                    .data(contourData)
                    .enter().append("path")
                    .attr("d", d3.geoPath(d3.geoIdentity().scale(1)))
                    .attr("fill", "rgba(0, 100, 255, 0.4)")
                    .attr("stroke", "#000")
                    .attr("stroke-width", 0.5);
            };
        };

        overlay.setMap(map);
    }

    afterUpdate(() => {
        if (mapReady && locations.length > 0) {
            plotContours();
        }
    });

    onMount(async () => {
        const existingScript = document.querySelector("script[src*='maps.googleapis.com']");
        if (existingScript) {
            existingScript.remove();
        }

        locations = await d3.csv('/data/bares_badalona.csv', d => ({
            latitude: parseFloat(d.Latitude),
            longitude: parseFloat(d.Longitude)
        }));

        
        const script = document.createElement("script");
        script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyBAc8vxTFxFeBRInMbuy_cgWxtav25eQyI&callback=initMap&v=weekly`;
        script.async = true;
        script.defer = true;

        script.onerror = () => console.error("Google Maps API script failed to load");
        
        window.initMap = initMap;
        document.head.appendChild(script);
        plotContours();

    });
</script>

<style>
    .contour-layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }
    #map {
        height: 400px;
        width: 100%;
    }
</style>

<div id="map"></div>
