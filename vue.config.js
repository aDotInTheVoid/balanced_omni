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
  pwa: {
    name: 'Balanced',
    themeColor: '#00967f',
    iconPaths: {
      favicon32: 'img/icons/favicon-32x32.png',
      favicon16: 'img/icons/favicon-16x16.png',
      appleTouchIcon: 'img/icons/apple-touch-icon.png',
      maskIcon: 'img/icons/safari-pinned-tab.svg',
      msTileImage: 'img/icons/mstile-150x150.png',
    },

  },
};
