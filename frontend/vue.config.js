const pages = {
  index: {
    entry: "src/main.js",
  },
};

module.exports = {
  publicPath: "/static/vue/",
  outputDir: "./build/static/vue/",
  indexPath: "../../templates/vue_index.html",

  pages: pages,
};