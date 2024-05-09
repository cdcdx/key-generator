// import normalNav from './normal'
import LinkMethods from '../../mixins/LinkMethods';
import TpWallet from '../../mixins/TpWallet';

export default {
  name: 'HeaderLayout',
  mixins: [LinkMethods, TpWallet],
  components: {
    // normalNav
  },
  props: {
    navLogo: {
      type: String,
      default: require('../../assets/logo.png'),
    },
    navTitleColor: {
      type: String,
      default: '#fff',
    },
    navIconColor: {
      type: String,
      default: '#fff',
    },
    arrowClass: {
      type: String,
      default: 'icon-down-333',
    },
    langClass: {
      type: String,
      default: 'icon-earth',
    },
  },
  data() {
    return {
      navIndex: '',
      menuState: false,
      clientWidth: 0,
      // eventListen: null,
    };
  },

  computed: {
    titleLang() {
      switch (this.$i18n.locale) {
        case 'zh':
          return '中文简体';
        case 'zh-tw':
          return '中文繁体';
        case 'en':
          return 'English';
        case 'ko':
          return '한국어';
        case 'ru':
          return 'Русский';
        case 'es':
          return 'Español';
        case 'hi':
          return 'हिन्दी';
        case 'fil':
          return 'Filipino';
        case 'pt':
          return 'Português';
        case 'ja':
          return '日本語';
        case 'vi':
          return 'Tiếng Việt';
        case 'th':
          return 'ภาษาไทย';
        default:
          return '中文';
      }
    },
    navList() {
      return [
        {
          title: this.$t('github.title'),
          url: this.githubUrl,
        },
        {
          title: '',
        },
        {
          title: this.titleLang,
          lang: true,
          class: 'language-changes',
          children: [
            { title: '简体中文', lang: 'zh', link: '/zh', class: 'locale-zh' },
            { title: 'English', lang: 'en', link: '/en', class: 'locale-en' },
            { title: '日本語', lang: 'ja', link: '/ja', class: 'locale-ja' },
            { title: '한국어', lang: 'ko', link: '/ko', class: 'locale-ko' },
          ],
        },
      ];
    },
  },
  watch: {
    clientWidth() {
      this.navIndex = '';
    },
  },
  mounted() {
    this.clientWidth = document.body.clientWidth;
    this.navState();
    this.windowChange();
  },
  // beforeDestroy() {
  //   document.removeEventListener('click', this.eventListen);
  // },
  methods: {
    changeMenuState() {
      this.menuState = !this.menuState;
      this.navIndex = '';
    },

    navState(el) {
      document.addEventListener(
        'click',
        (e) => {
          if (this.clientWidth > 768) {
            if (this.$refs.navMain && !this.$refs.navMain.contains(e.target)) {
              this.navIndex = '';
            }
          }
        },
        false
      );
    },

    navGo(item, index, el) {
      el.preventDefault();
      if (item.children) {
        index === this.navIndex
          ? (this.navIndex = '')
          : (this.navIndex = index);
      }
      if (item.url && !item.local) {
        return window.open(item.url);
      }
      if (item.url && item.local) {
        this.$router.push(item.url);
      }
      // return false
    },
    navEnter(item, index, el) {
      el.preventDefault();
      if (item.children) {
        index === this.navIndex
          ? (this.navIndex = '')
          : (this.navIndex = index);
      }
      if (item.url && !item.local && item.children) {
        return window.open(item.url);
      }
      if (item.url && item.local && item.children) {
        this.$router.push(item.url);
      }
    },
    navLeave(item, index, el) {
      el.preventDefault();
      if (item.children) {
        index === this.navIndex
          ? (this.navIndex = '')
          : (this.navIndex = index);
      }
      this.navIndex = '';
    },

    navChildrenGo(item, el) {
      if (el) el.preventDefault();
      if (item.url && !item.local) {
        return window.open(item.url);
      }

      if (item.url && item.local && !item.lang) {
        return this.$router.push(item.url);
      }

      if (item.lang) {
        this.$i18n.locale = item.lang;
        localStorage.setItem('locale', item.lang);
        this.updateDocumentTitle(item.lang)
      }
      this.navIndex = '';
    },

    updateDocumentTitle(lang) {
      switch (lang) {
        case 'en':
          document.title = 'Key Generator | TokenPocket';
          break;
        case 'zh':
          document.title = '公私钥生成器 | TokenPocket';
          break;
        case 'ko':
          document.title = '키 생성기 | TokenPocket';
          break;
        case 'ja':
          document.title = 'キージェネレーター | TokenPocket';
          break;
        default:
          break;
      }
    },

    windowChange() {
      window.addEventListener('resize', (e) => {
        this.clientWidth = e.target.screen.width;
      });
    },
  },
};
