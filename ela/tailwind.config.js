/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./templates/**/*.html'
	],
	theme: {
		extend: {
			colors: {
				customColor: 'hsl(238, 57%, 9%)',
				color: 'hsl(234, 44%, 16%)',
			  },
		},
	},
	plugins: [],
}


