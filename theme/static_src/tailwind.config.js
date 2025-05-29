module.exports = {
    content: [
        '../templates/**/*.html',
        '../**/templates/**/*.html',
        '../**/templates/**/*.js',
    ],
    theme: {
        extend: {
            colors: {
                'apple-blue': {
                    100: '#E6F0FF',
                    500: '#007AFF',
                    600: '#0066CC',
                    700: '#0055AA',
                },
            },
        },
    },
    plugins: [],
} 