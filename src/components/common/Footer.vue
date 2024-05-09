<template>
  <div class="footer">
    <div class="content">
      <div class="follow-wrap">
        <div class="footer-follows">
          <div
            class="footer-follow"
            v-for="(item, index) in followList"
            :key="index"
            :class="['footer-follow-' + (index + 1)]"
            @click="openFollow(item)"
          ></div>
          <a
            href="mailto:service@tokenpocket.pro"
            class="footer-follow footer-follow-8"
            target="_blank"
          ></a>
        </div>
        <div class="copyright">© TokenPocket Foundation Ltd.</div>
      </div>
    </div>
    <Modal v-if="show" @close="close" :url="url" />
  </div>
</template>

<script>

import TpWallet from '../../mixins/TpWallet';
import Modal from './Modal.vue';

export default {
  name: 'Footer',
  components: { Modal },
  mixins: [TpWallet],
  data() {
    return {
      email: '',
      show: false,
      url: '',
    };
  },
  computed: {
    followList() {
      return [
        { url: this.twitterUrl },
        { url: this.telegramUrl },
        { url: this.tokenpocketUrl },
        { url: this.youtubeUrl },
        { url: this.discordUrl },
        { url: this.githubUrl },
        { url: this.mediumUrl },
      ];
    },
    isZH() {
      return this.$i18n.locale === 'zh';
    },
  },
  methods: {
    openFollow(item) {
      if (item.isTelegram) {
        this.show = true;
        this.url = item.url;
      } else {
        window.open(item.url);
      }
    },
    close() {
      this.show = false;
    },
    footerUrl(item, el) {
      el.preventDefault();
      // return false
      if (item.scrollTop) {
        document.body.scrollTop = document.documentElement.scrollTop = 0;
        return false;
      }
      window.open(item.url);
    },
  },
};
</script>

<style lang="scss" scoped>
@for $i from 1 through 8 {
  .footer-follow-#{$i} {
    background: url(../../assets/footer/#{$i}.png) no-repeat 100% / contain;
    cursor: pointer;
    &:hover {
      background: url(../../assets/footer/#{$i}-on.png)
        no-repeat
        100% /
        contain;
    }
  }
}
.footer {
  background: #1c1c1f;
  .content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    padding: 20px 0 40px;
    .follow-wrap {
      .footer-follows {
        display: flex;
        margin: 32px 0 16px;
        .footer-follow {
          width: 32px;
          height: 32px;
          &:nth-child(n + 2) {
            margin-left: 10px;
          }
        }
      }
      .copyright {
        font-size: 12px;
        font-weight: 400;
        color: #6f7174;
        line-height: 20px;
      }
    }
  }
}

.footer-email {
  position: absolute;
  border: 1px solid #2980fe;
  border-radius: 4px;
  display: flex;
  align-items: center;
  height: 32px;
  font-size: 14px;
  input {
    outline: none;
    border: 0;
    color: #101010;
    width: 160px;
    height: 100%;
    margin: 0 0 0 10px;
    &::-webkit-input-placeholder {
      color: #b1b1b1;
    }

    &::-moz-placeholder {
      color: #b1b1b1;
    }

    &::-ms-placeholder {
      color: #b1b1b1;
    }
  }

  span {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-size: 12px;
    font-weight: 400;
    width: 80px;
    height: 32px;
    line-height: 32px;
    color: #fff;
    background: #2980fe;
    position: relative;
    border-radius: 0 4px 4px 0;
  }
}

.email-icon-right {
  display: inline-block;
  position: relative;
  margin-left: 5px;
  width: 6px;
  height: 6px;

  &:after {
    content: '';
    position: absolute;
    top: 0;
    left: 2px;
    width: 6px;
    height: 6px;
    border-top: 1px solid #fff;
    border-right: 1px solid #fff;
    transform: rotate(45deg);
  }
}

@media screen and (max-width: 1300px) {
  .footer {
    .content {
      padding: 40px 28px 20px;
    }
  }
}

@media screen and (max-width: 1200px) {
  .footer {
    .content {
      padding: 40px 28px 20px;
      flex-direction: column;
    }
  }
}

@media screen and (max-width: 768px) {
  @for $i from 1 through 8 {
    .footer-follow-#{$i} {
      background: url(../../assets/footer/#{$i}.png) no-repeat 100% / contain;
      cursor: pointer;
      &:hover {
        background: url(../../assets/footer/#{$i}.png) no-repeat 100% / contain;
      }
    }
  }
  .footer {
    .content {
      padding: 68px 28px 60px;
      .follow-wrap {
        .logo {
          width: 199px;
        }
        .footer-follows {
          margin: 41px 0 21px;
        }
        .copyright {
          font-size: 13px;
        }
      }
    }
  }
}

@media screen and (max-width: 575px) {
  .footer-link-wrap {
    display: flex;
    flex-wrap: wrap;
    .footer-link {
      width: 33%;
      &.width0 {
        width: 0;
      }
    }
  }

  .footer-list {
    margin-bottom: 10px;
  }

  .footer-link h3 {
    margin-bottom: 0px;
  }

  .footer-link a {
    margin-bottom: 0;
  }

  .footer-email {
    input {
      width: 200px;
    }
  }
}
</style>
