/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        grotesque: ["Bricolage Grotesque", "Arial"],
        public: ["Public Sans", "Sans Serif"],
      },
      colors: {
        turquoise: '#44c0c9',
        pink: '#dd6fb2',
        mint: '#59bf7f',
      }
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
