<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';
    import * as Plot from '@observablehq/plot';

    let map;
    let data;
    let svgLayer;

    onMount(async () => {
        const L = await import('leaflet');
        await import('leaflet/dist/leaflet.css'); // Load Leaflet CSS

        // Load data for the contour plot
        data = await d3.csv('/data/bares_badalona.csv', d => ({
            Latitude: parseFloat(d.Latitude),
            Longitude: parseFloat(d.Longitude),
            Name: d.Name
        }));

        // Initialize the Leaflet map centered on Badalona
        map = L.map('map', {
            zoomControl: false,
            dragging: false,
            zoomSnap: 0.1,
        }).setView([41.45, 2.24], 14);

        // Add a tile layer for the base map (OpenStreetMap or other provider)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // Create and add the contour plot overlay initially
        drawContour();

        // Redraw the contour plot on map move and zoom to maintain alignment
        map.on('moveend', drawContour);
        map.on('zoomend', drawContour);
    });
    $: if (data) drawContour();

    function drawContour() {
        // Remove the previous contour plot if it exists
        if (svgLayer) {
            svgLayer.remove();
        }

        // Get the current map bounds and dimensions
        const bounds = map.getBounds();
        const topLeft = map.latLngToLayerPoint(bounds.getNorthWest());
        const bottomRight = map.latLngToLayerPoint(bounds.getSouthEast());

        // Generate a new contour plot using Observable Plot
        svgLayer = Plot.plot({
            width: bottomRight.x - topLeft.x,
            height: bottomRight.y - topLeft.y,
            style: {
                position: 'absolute',
                left: `${topLeft.x}px`,
                top: `${topLeft.y}px`
            },
            marks: [
                Plot.density(data, {
                    x: 'Longitude',
                    y: 'Latitude',
                    fill: 'density',
                    thresholds: 20,
                    bandwidth: 10,
                    fillOpacity: 0.5,
                    stroke: "currentColor"
                })
            ],
            x: {
                domain: [bounds.getWest(), bounds.getEast()],
            },
            y: {
                domain: [bounds.getSouth(), bounds.getNorth()]
            }
        });

        // Create a Leaflet SVG overlay with the contour plot, adjusting bounds to the current map view
        const overlayBounds = [
            [bounds.getSouth(), bounds.getWest()],
            [bounds.getNorth(), bounds.getEast()]
        ];

        // Use `L.svgOverlay` to add the contour plot as an overlay to the map
        L.svgOverlay(svgLayer, overlayBounds).addTo(map);
    }
</script>

<style>
    #map {
        width: 100%;
        height: 600px;
        position: relative;
    }
</style>

<div id="map"></div>