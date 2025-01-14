/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{html,js,svelte,ts}'
  ],
  theme: {
    extend: {
      fontFamily: {
        baskerville: ['Libre Baskerville', 'sans-serif'],
        bebas: ['Bebas Neue', 'sans-serif'],
      }
    },
  },
  plugins: [],
};
