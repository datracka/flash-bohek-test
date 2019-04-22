var path = require("path");

module.exports = {
  output: {
    path: __dirname + "/diysna/static",
    filename: "main.js",
    publicPath: __dirname + "/diysna/static"
  },
  devServer: {
    contentBase: path.join(__dirname, "/diysna/templates"),
    compress: true,
    port: 9000
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
