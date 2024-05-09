export default {
  computed: {
    isTokenPocketPro() {
      if (window.location.hostname === 'key.tokenpocket.pro') {
        return true;
      } else {
        return false;
      }
    },
    twitterUrl() {
      if (this.isTokenPocketPro) {
        return 'https://twitter.com/TokenPocket_TP';
      } else {
        return 'https://twitter.com';
      }
    },
    telegramUrl() {
      if (this.isTokenPocketPro) {
        return 'https://t.me/tokenPocket_cn';
      } else {
        return 'https://t.me/cdcdx';
      }
    },
    tokenpocketUrl() {
      if (this.isTokenPocketPro) {
        return 'https://fans.tokenpocket.pro/';
      } else {
        return 'https://fans.tokenpocket.pro/';
      }
    },
    youtubeUrl() {
      if (this.isTokenPocketPro) {
        return 'https://www.youtube.com/channel/UCudaS5hcbqUaMtOGHmQ2e0A';
      } else {
        return 'https://www.youtube.com';
      }
    },
    discordUrl() {
      if (this.isTokenPocketPro) {
        return 'https://discord.com/invite/NKPM8TXFQk';
      } else {
        return 'https://discord.com';
      }
    },
    githubUrl() {
      if (this.isTokenPocketPro) {
        return 'https://github.com/TP-Lab/key-generator';
      } else {
        return 'https://github.com/cdcdx/key-generator';
      }
    },
    mediumUrl() {
      if (this.isTokenPocketPro) {
        return 'https://tokenpocket-gm.medium.com';
      } else {
        return 'https://medium.com';
      }
    },
  },
};
