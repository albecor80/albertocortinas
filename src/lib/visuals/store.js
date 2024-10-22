import { writable } from 'svelte/store';

// A writable store to hold the selected country
export const selectedCountry = writable(null);

export function updateDimensions(maxWidth = 800, aspectRatio = 0.8) {
    const width = Math.min(window.innerWidth * 0.9, maxWidth); // Set a maximum width
    const height = width * aspectRatio; // Adjust height based on width and aspect ratio
    return { width, height };
}
