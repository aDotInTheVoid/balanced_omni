module.exports = {
  lintOnSave: false,
  publicPath: (process.env.CI === 'true' ? '/balanced_omni/' : ''),
  productionSourceMap: false,
  pluginOptions: {
    cordovaPath: 'src-cordova',
  },
  transpileDependencies: [
    'vuetify',
  ],
};
