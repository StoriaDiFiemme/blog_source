module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        roboto: ['Roboto Slab'],
        sans: ['Open Sans']
      },
      maxHeight: {
        'foo': '50%'
      },
      height: {
        'vw-1/2': '50vw',
        'vw-1/4': '25vw',
      }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
