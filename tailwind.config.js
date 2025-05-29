/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
    "./**/templates/**/*.html",
    "./**/static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        // Apple-like colors
        'apple-blue': {
          50: '#f0f7ff',
          100: '#e0f0ff',
          200: '#bae0ff',
          300: '#7cc5ff',
          400: '#36a9ff',
          500: '#0090ff',
          600: '#0070cc',
          700: '#005799',
          800: '#003d6b',
          900: '#002340',
        },
      },
      fontFamily: {
        'sf': ['SF Pro Display', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      boxShadow: {
        'apple': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'apple-hover': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      },
      borderRadius: {
        'apple': '1rem',
      },
      animation: {
        'apple-fade': 'fade 0.3s ease-in-out',
      },
      keyframes: {
        fade: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
} 