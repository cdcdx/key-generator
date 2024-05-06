<template>
  <div class="home">
    <!-- <Header /> -->
    <main>
      <div class="container">
        <!-- <div class="main-left">
          <img class="left-img" src="../assets/left-img.png" alt="" />
          <div class="title">{{ $t('main.title') }}</div>
          <div class="desc">{{ $t('main.intro') }}</div>
          <div class="address">{{ $t('main.githubUrl') }}</div>
          <a class="github" href="https://github.com/TP-Lab/key-generator" target="_blank">
            <div class="left">
              <img src="../assets/main/github.png" alt="" />
              <span>Github</span>
            </div>
            <img class="arrow" src="../assets/arrow.png" alt="" />
          </a>
        </div> -->
        <div class="main-right">

          <div class="mnemonic-item">
            <div class="mnemonic-name">{{ $t('main.mnemonic') }}</div>
            <textarea class="mnemonic-input" v-model="mnemonic" placeholder="mnemonic">
            </textarea>
          </div>

          <div class="chain-list">
            <div class="chain-item" :class="{ active: network === chain.network }" v-for="(chain, index) in chainList"
              :key="index" @click="onSelectChain(chain, index)">
              <img :src="chain.icon" alt="" />
              <span>{{ chain.name }}</span>
            </div>
          </div>
          <div class="key-content">
            <div>
              <div class="mobile-chain" @click="showMobileChain">
                <div class="left">
                  <img :src="chainObj[0].icon" alt="" />
                  <span>{{ chainObj[0].name }}</span>
                </div>
                <img class="arrow" src="../assets/arrow.png" alt="" />
              </div>
              <div class="title">{{ chainObj[0].name }} keys</div>
              <div class="warn">{{ $t('main.tips') }}</div>
              <div class="key-list">
                <div class="key-box ethereum" v-show="network === 'ETH'">
                  <KeyItem :title="$t('main.address')" :value="ethAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="ethPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="ethPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="ethUncompressPublicKey" />
                </div>
                <div class="key-box eos" v-show="network === 'EOS'">
                  <KeyItem :title="$t('main.address')" :value="eosAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="eosPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="eosPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="eosUncompressPublicKey" />
                </div>
                <div class="key-box dogecoin" v-show="network === 'DOGE'">
                  <KeyItem :title="$t('main.address')" :value="dogeAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="dogePrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="dogePublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="dogeUncompressPublicKey" />
                </div>
                <div class="key-box iost" v-show="network === 'IOST'">
                  <KeyItem :title="$t('main.address')" :value="iostAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="iostPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="iostPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="iostUncompressPublicKey" />
                </div>
                <div class="key-box tron" v-show="network === 'TRX'">
                  <KeyItem :title="$t('main.address')" :value="tronAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="tronPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="tronPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="tronUncompressPublicKey" />
                </div>
                <div class="key-box btc" v-show="network === 'BTC'">
                  <KeyItem :title="'P2PKH ' + $t('main.address')" :value="btcAddress" />
                  <KeyItem :title="'P2SH ' + $t('main.address')" :value="btcP2SHAddress" />
                  <KeyItem :title="'P2WPK ' + $t('main.address')" :value="btcSegwitAddress" />
                  <KeyItem :title="'Taproot ' + $t('main.address')" :value="btcTaprootAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="btcPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="btcPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="btcUncompressPublicKey" />
                </div>
                <div class="key-box cosmos" v-show="network === 'ATOM'">
                  <KeyItem :title="$t('main.address')" :value="cosmosAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="cosmosPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="cosmosPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="cosmosUncompressPublicKey" />
                </div>
                <div class="key-box binance" v-show="network === 'BNB'">
                  <KeyItem :title="$t('main.address')" :value="binanceAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="binancePrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="binancePublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="binanceUncompressPublicKey" />
                </div>
                <div class="key-box nervos" v-show="network === 'CKB'">
                  <KeyItem :title="$t('main.address')" :value="nervosAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="nervosPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="nervosPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="nervosUncompressPublicKey" />
                </div>
                <div class="key-box jingtum" v-show="network === 'JMB'">
                  <KeyItem :title="$t('main.publicKey')" :value="jingtumAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="jingtumPrivateKey" />
                </div>
                <div class="key-box solana" v-show="network === 'SOL'">
                  <KeyItem :title="$t('main.address')" :value="solanaAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="solanaPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="solanaPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="solanaUncompressPublicKey" />
                </div>
                <div class="key-box aptos" v-show="network === 'APT'">
                  <KeyItem :title="$t('main.address')" :value="aptosAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="aptosPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="aptosPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="aptosUncompressPublicKey" />
                </div>
                <div class="key-box polkadot" v-show="network === 'DOT'">
                  <KeyItem :title="$t('main.address')" :value="polkadotAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="polkadotPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="polkadotPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="polkadotUncompressPublicKey" />
                </div>
                <div class="key-box bch" v-show="network === 'BCH'">
                  <KeyItem :title="$t('main.address')" :value="bchAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="bchPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="bchPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="bchUncompressPublicKey" />
                </div>
                <div class="key-box ltc" v-show="network === 'LTC'">
                  <KeyItem :title="'SegWit ' + $t('main.address')" :value="ltcAddress" />
                  <KeyItem :title="'Legacy ' + $t('main.address')" :value="ltcP2SHAddress" />
                  <KeyItem :title="'Native SegWit ' + $t('main.address')" :value="ltcNativeSegwitAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="ltcPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="ltcPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="ltcUncompressPublicKey" />
                </div>
                <div class="key-box cfx" v-show="network === 'CFX'">
                  <KeyItem :title="$t('main.address')" :value="cfxAddress" />
                  <KeyItem :title="'Conflux Mainnet ' + $t('main.address')" :value="cfxMainnetAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="cfxPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="cfxPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="cfxUncompressPublicKey" />
                </div>
                <div class="key-box nostr" v-show="network === 'NOSTR'">
                  <KeyItem :title="$t('main.address')" :value="nostrAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="nostrPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="nostrPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="nostrUncompressPublicKey" />
                </div>
                <div class="key-box sui" v-show="network === 'SUI'">
                  <KeyItem :title="$t('main.address')" :value="suiAddress" />
                  <KeyItem :title="$t('main.privateKey')" :value="suiPrivateKey" />
                  <KeyItem :title="$t('main.publicKey')" :value="suiPublicKey" />
                  <KeyItem :title="$t('main.uncompressPublicKey')" :value="suiUncompressPublicKey" />
                </div>
              </div>
            </div>

            <div v-if="mnemonic" class="grid-container">
              <div class="generate-btn" @click="onGenerate">
                {{ $t('main.gen') }}
              </div>
              <div class="generate-btn" @click="onGenerateFromMnemonic">
                {{ $t('main.genFromMnemonic') }}
              </div>
            </div>
            <div v-if="!mnemonic">
              <div class="generate-btn" @click="onGenerate">
                {{ $t('main.gen') }}
              </div>
            </div>

          </div>
        </div>
      </div>
    </main>
    <!-- <Footer /> -->
    <!-- <div class="change-chain" v-show="isMobileChain">
      <div class="container">
        <div class="title-header">
          <span>{{ $t('main.changeChain') }}</span>
          <img src="../assets/share-close.png" alt="" @click="onClose" />
        </div>
        <div class="line"></div>
        <div class="mobile-chain-list">
          <div class="mobile-chain-item" v-for="(chain, index) in chainList" :key="index"
            @click="onSelectChain(chain, index)">
            <img :src="chain.icon" alt="" />
            <span>{{ chain.name }}</span>
          </div>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import BncClient from '@binance-chain/javascript-sdk';
import { toHEX } from "@mysten/bcs";
import { Ed25519Keypair } from '@mysten/sui.js';
import Address from '@nervosnetwork/ckb-sdk-address';
import * as secp256k1 from '@noble/secp256k1';
import Keyring from '@polkadot/keyring';
import { u8aToHex } from '@polkadot/util';
import {
cryptoWaitReady,
mnemonicGenerate,
mnemonicToMiniSecret,
} from '@polkadot/util-crypto';
import { bech32 } from '@scure/base';
import { Keypair } from '@solana/web3.js';
// npm install @tronscan/client
import { pkToAddress } from "@tronscan/client/src/utils/crypto";
import { AptosAccount } from 'aptos';
import { generateMnemonic, mnemonicToSeed, mnemonicToSeedSync } from 'bip39';
import {
Address as BCHAddress,
PrivateKey as BCHPrivateKey,
PublicKey as BCHPublicKey,
crypto as BCHcrypto,
} from 'bitcore-lib-cash';
import bs58 from 'bs58';
import { ec as EC } from 'elliptic';
import ecc from 'eosjs-ecc';
// import ethers from 'ethers';
import iost from 'iost';
import Irisnet from 'irisnet-crypto';
import { Wallet } from 'jingtum-base-lib';
import { format } from 'js-conflux-sdk';
import { generatePrivateKey, getPublicKey } from 'nostr-tools';
import TronWeb from 'tronweb';
import Web3 from 'web3';
const ethers = require("ethers");
// const ethUtil = require('ethereumjs-util');

const Bech32MaxSize = 5000;

const ec = new EC('secp256k1');

import BIP32Factory from 'bip32';
import * as bitcoin from 'bitcoinjs-lib';
import eccObj from '../utils/ecc';
bitcoin.initEccLib(eccObj);
const bip32Obj = BIP32Factory(eccObj);

import Footer from '../components/common/Footer.vue';
import Header from '../components/common/Header.vue';
import KeyItem from '../components/common/KeyItem.vue';

export default {
  name: 'HomeView',
  components: { Header, Footer, KeyItem },
  data() {
    return {
      dogeAddress: '',
      dogePrivateKey: '',
      dogePublicKey: '',
      dogeUncompressPublicKey: '',
      nostrAddress: '',
      nostrPrivateKey: '',
      nostrPublicKey: '',
      nostrUncompressPublicKey: '',
      suiAddress: '',
      suiPrivateKey: '',
      suiPublicKey: '',
      suiUncompressPublicKey: '',
      cfxMainnetAddress: '',
      cfxAddress: '',
      cfxPrivateKey: '',
      cfxPublicKey: '',
      cfxUncompressPublicKey: '',
      ltcAddress: '',
      ltcP2SHAddress: '',
      ltcNativeSegwitAddress: '',
      ltcPrivateKey: '',
      ltcPublicKey: '',
      ltcUncompressPublicKey: '',
      bchAddress: '',
      bchPrivateKey: '',
      bchPublicKey: '',
      bchUncompressPublicKey: '',
      polkadotAddress: '',
      polkadotPrivateKey: '',
      polkadotPublicKey: '',
      polkadotUncompressPublicKey: '',
      aptosAddress: '',
      aptosPrivateKey: '',
      aptosPublicKey: '',
      aptosUncompressPublicKey: '',
      solanaAddress: '',
      solanaPrivateKey: '',
      solanaPublicKey: '',
      solanaUncompressPublicKey: '',
      eosAddress: '',
      eosPrivateKey: '',
      eosPublicKey: '',
      eosUncompressPublicKey: '',
      ethAddress: '',
      ethPrivateKey: '',
      ethPublicKey: '',
      ethUncompressPublicKey: '',
      iostAddress: '',
      iostPrivateKey: '',
      iostPublicKey: '',
      iostUncompressPublicKey: '',
      tronAddress: '',
      tronPrivateKey: '',
      tronPublicKey: '',
      tronUncompressPublicKey: '',
      binanceAddress: '',
      binancePrivateKey: '',
      binancePublicKey: '',
      binanceUncompressPublicKey: '',
      cosmosAddress: '',
      cosmosPrivateKey: '',
      cosmosPublicKey: '',
      cosmosUncompressPublicKey: '',
      nervosAddress: '',
      nervosPrivateKey: '',
      nervosPublicKey: '',
      nervosUncompressPublicKey: '',
      jingtumAddress: '',
      jingtumPrivateKey: '',
      btcAddress: '',
      btcPrivateKey: '',
      btcPublicKey: '',
      btcUncompressPublicKey: '',
      btcP2SHAddress: '',
      btcSegwitAddress: '',
      btcTaprootAddress: '',
      copyEnable: true,
      clipboard: '',
      clipboard1: '',
      tronWeb: '',
      web3: '',
      BncClient: '',
      crypto: '',
      network: 'ETH',
      chainId: '',
      ss58: '',
      curIndex: 12,
      isMobileChain: false,
      mnemonic: localStorage.getItem('setmnemonic'),  // cookie
    };
  },

  computed: {
    chainList() {
      return [
        {
          network: 'BTC',
          icon: require('../assets/main/btc.png'),
          name: this.$t('chain.btc'),
        },
        {
          network: 'ETH',
          icon: require('../assets/main/eth.png'),
          name: this.$t('chain.ethereum'),
        },
        {
          chainId: 728126428,
          network: 'TRX',
          icon: require('../assets/main/tron.png'),
          name: this.$t('chain.tron'),
        },
        {
          network: 'SOL',
          icon: require('../assets/main/solana.png'),
          name: this.$t('chain.solana'),
        },
        {
          network: 'APT',
          icon: require('../assets/main/aptos.png'),
          name: this.$t('chain.aptos'),
        },
        {
          network: 'SUI',
          icon: require('../assets/main/sui.png'),
          name: this.$t('chain.sui'),
        },
        {
          chainId: 1030,
          network: 'CFX',
          icon: require('../assets/main/conflux.png'),
          name: this.$t('chain.conflux'),
        },
        {
          network: 'DOGE',
          icon: require('../assets/main/dogecoin.png'),
          name: this.$t('chain.dogecoin'),
        },
        {
          network: 'EOS',
          icon: require('../assets/main/eos.png'),
          name: this.$t('chain.eos'),
        },
        {
          network: 'ATOM',
          icon: require('../assets/main/cosmos.png'),
          name: this.$t('chain.cosmos'),
        },
        {
          network: 'IOST',
          icon: require('../assets/main/iost.png'),
          name: this.$t('chain.iost'),
        },
        {
          network: 'DOT',
          ss58: '0',
          icon: require('../assets/main/Polkadot.png'),
          name: this.$t('chain.polkadot'),
        },
        {
          network: 'CKB',
          icon: require('../assets/main/nervos.png'),
          name: this.$t('chain.nervos'),
        },
        {
          network: 'BNB',
          icon: require('../assets/main/binance.png'),
          name: this.$t('chain.binance'),
        },
        {
          network: 'NOSTR',
          icon: require('../assets/main/nostr.jpg'),
          name: this.$t('chain.nostr'),
        },
        {
          network: 'BCH',
          icon: require('../assets/main/bch.png'),
          name: this.$t('chain.bch'),
        },
        {
          network: 'LTC',
          icon: require('../assets/main/ltc.png'),
          name: this.$t('chain.ltc'),
        },
        {
          network: 'JMB',
          icon: require('../assets/main/jingtum.png'),
          name: this.$t('chain.jingtum'),
        },
      ];
    },
    urlObj() {
      let obj = {
        network: this.network,
      };
      if (this.ss58) {
        obj.ss58 = this.ss58;
      }
      if (this.chainId) {
        obj.chainId = this.chainId;
      }
      return obj;
    },
    chainObj() {
      return this.chainList.filter((item) => item.network === this.network);
    },
  },

  watch: {
    urlObj(n) {
      this.$router.replace({
        path: `/`,
        query: { ...n },
      });
    },
  },

  created() {
    const { network, chainId, ss58 } = this.$route.query;
    this.network = network || 'BTC';
    this.chainId = chainId || '';
    this.ss58 = ss58 || '';
    this.tronWeb = new TronWeb({
      fullHost: 'https://api.trongrid.io',
      privateKey: '',
    });

    this.web3 = new Web3(
      new Web3.providers.HttpProvider('https://eth49he73m.jccdex.cn'),
    );

    this.BncClient = BncClient;
    this.crypto = Irisnet.getCrypto('cosmos');
  },

  mounted() {
    setTimeout(() => {
      if (this.mnemonic == null) {
        this.genEosKey();
        this.genEthKey();
        this.genIostKey();
        this.genBtcKey();
        this.genNervosKey();
        this.genTronKey();
        this.genBinanceKey();
        this.genCosmosKey();
        this.genJingtumKey();
        this.genSolanaKey();
        this.genAptosKey();
        this.genPolkadotKey();
        this.genLTCKey();
        this.genBCHKey();
        this.genConfluxKey();
        this.genSuiKey();
        this.genNostrKey();
        this.genDogeKey();
      } else {
        this.genEosKeyfromMnemonic();
        this.genEthKeyfromMnemonic();
        this.genIostKeyfromMnemonic();
        this.genBtcKeyfromMnemonic();
        this.genNervosKeyfromMnemonic();
        this.genTronKeyfromMnemonic();
        this.genBinanceKeyfromMnemonic();
        this.genCosmosKeyfromMnemonic();
        this.genJingtumKey();
        this.genSolanaKeyfromMnemonic();
        this.genAptosKeyfromMnemonic();
        this.genPolkadotKeyfromMnemonic();
        this.genLTCKeyfromMnemonic();
        this.genBCHKeyfromMnemonic();
        this.genConfluxKeyfromMnemonic();
        this.genSuiKeyfromMnemonic();
        this.genNostrKeyfromMnemonic();
        this.genDogeKeyfromMnemonic(); 
      }
    }, 1000);
  },

  methods: {
    async genDogeKey() {
      const DOGE_NETWORK = {
        messagePrefix: '\x19Dogecoin Signed Message:\n',
        bip32: {
          public: 0x02facafd,
          private: 0x02fac398,
        },
        pubKeyHash: 0x1e,
        scripthash: 0x16,
        wif: 0x9e,
      };
      const doge_path = "m/44'/3'/0'/0/0";
      const mnemonic = generateMnemonic();
      const seed = await mnemonicToSeed(mnemonic);
      const doge_master = bip32Obj.fromSeed(seed, DOGE_NETWORK);
      const doge_keypair = doge_master.derivePath(doge_path);
      const doge_data = bitcoin.payments.p2pkh({
        pubkey: doge_keypair.publicKey,
        network: DOGE_NETWORK,
      });
      this.dogeAddress = doge_data.address;
      this.dogePrivateKey = doge_keypair.toWIF();
      this.dogePublicKey = Buffer.from(doge_keypair.publicKey).toString('hex');
    },

    async genDogeKeyfromMnemonic() {
      const DOGE_NETWORK = {
        messagePrefix: '\x19Dogecoin Signed Message:\n',
        bip32: {
          public: 0x02facafd,
          private: 0x02fac398,
        },
        pubKeyHash: 0x1e,
        scripthash: 0x16,
        wif: 0x9e,
      };
      const doge_path = "m/44'/3'/0'/0/0";
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = await mnemonicToSeed(mnemonic);
      // // log
      // console.log('mnemonic:', mnemonic);
      // console.log('seed:', seed);

      const doge_master = bip32Obj.fromSeed(seed, DOGE_NETWORK);
      const doge_keypair = doge_master.derivePath(doge_path);
      const doge_data = bitcoin.payments.p2pkh({
        pubkey: doge_keypair.publicKey,
        network: DOGE_NETWORK,
      });
      this.dogeAddress = doge_data.address;
      this.dogePrivateKey = doge_keypair.toWIF();
      this.dogePublicKey = Buffer.from(doge_keypair.publicKey).toString('hex');
    },

    // ---------- 
    genNostrKey() {
      let sk = generatePrivateKey(); // `sk` is a hex string
      let pk = getPublicKey(sk); // `pk` is a hex string
      this.nostrPrivateKey = this.nsecEncode(sk);
      this.nostrAddress = this.npubEncode(pk);
      this.nostrPublicKey = pk;
    },

    genNostrKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/1237'/0'/0/0";
      const walletMnemonic = ethers.Wallet.fromMnemonic(mnemonic, child);
      const privateKey = walletMnemonic.privateKey;
      let sk = privateKey.replace('0x', '').replace('0X', '').replace(' ', ''); // `sk` is a hex string
      let pk = getPublicKey(sk); // `pk` is a hex string
      this.nostrPrivateKey = this.nsecEncode(sk);
      this.nostrAddress = this.npubEncode(pk);
      this.nostrPublicKey = pk;
    },

    nsecEncode(hex) {
      return this.encodeBytes('nsec', hex);
    },

    npubEncode(hex) {
      return this.encodeBytes('npub', hex);
    },

    encodeBytes(prefix, hex) {
      let data = secp256k1.utils.hexToBytes(hex);
      let words = bech32.toWords(data);
      return bech32.encode(prefix, words, Bech32MaxSize);
    },

    // ---------- 
    genSuiKey() {
      const keypair = new Ed25519Keypair();
      this.suiAddress = keypair.getPublicKey().toSuiAddress();
      this.suiPublicKey = keypair.getPublicKey();
      this.suiPrivateKey = toHEX(keypair.keypair.secretKey.slice(0, 32));
    },

    genSuiKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/784'/0'/0'/0'".toString();
      const keypair = Ed25519Keypair.deriveKeypair(mnemonic, child);
      this.suiAddress = keypair.getPublicKey().toSuiAddress();
      this.suiPublicKey = keypair.getPublicKey();
      this.suiPrivateKey = toHEX(keypair.keypair.secretKey.slice(0, 32));
    },

    // ---------- 
    genConfluxKey() {
      const randomWallet = ethers.Wallet.createRandom();
      this.cfxAddress = randomWallet.address;
      this.cfxPrivateKey = randomWallet.privateKey;
      const publicKey = randomWallet.publicKey.toString('hex');
      this.cfxUncompressPublicKey = publicKey;
      this.cfxPublicKey = '0x' + compressPublicKey(publicKey);
      // console.log('publicKey:', publicKey);
      // console.log('this.ethPublicKey:', this.ethPublicKey);
      this.cfxMainnetAddress = format.address(
        `0x1${randomWallet.address.toLowerCase().slice(3)}`,
        1029
      );

      // var account = this.web3.eth.accounts.create();
      // this.cfxAddress = account.address;
      // this.cfxPrivateKey = account.privateKey;
      // this.cfxMainnetAddress = format.address(
      //   `0x1${account.address.toLowerCase().slice(3)}`,
      //   1029
      // );
    },

    genConfluxKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/60'/0'/0/0";
      const walletMnemonic = ethers.Wallet.fromMnemonic(mnemonic, child);
      this.cfxAddress = walletMnemonic.address;
      this.cfxPrivateKey = walletMnemonic.privateKey;
      const publicKey = walletMnemonic.publicKey.toString('hex');
      this.cfxUncompressPublicKey = publicKey;
      this.cfxPublicKey = '0x' + compressPublicKey(publicKey);
      // console.log('publicKey:', publicKey);
      // console.log('this.ethPublicKey:', this.ethPublicKey);
      this.cfxMainnetAddress = format.address(
        `0x1${walletMnemonic.address.toLowerCase().slice(3)}`,
        1029
      );
    },

    // ---------- 
    genBCHKey() {
      let privateKey = new BCHPrivateKey();
      // console.log("privateKey:",privateKey);
      this.bchPrivateKey = privateKey.toWIF();
      let publicKey = new BCHPublicKey(privateKey);
      this.bchPublicKey = publicKey.toString();
      let address = new BCHAddress(publicKey);
      this.bchAddress = address.toString().slice(12);
    },

    genBCHKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }

      var value = new Buffer(mnemonic);
      var hash = BCHcrypto.Hash.sha256(value);
      var bn = BCHcrypto.BN.fromBuffer(hash);
      let privateKey = new BCHPrivateKey(bn);
      // console.log("privateKey:", privateKey);
      this.bchPrivateKey = privateKey.toWIF();
      let publicKey = new BCHPublicKey(privateKey);
      this.bchPublicKey = publicKey.toString();
      let address = new BCHAddress(publicKey);
      this.bchAddress = address.toString().slice(12);
    },

    // ---------- 
    // generate LTC path
    getLTCPath(type) {
      let path = '';
      // p2pkh
      if (type == 'p2pkh') {
        path = "m/44'/2'/0'/0/0";
      }
      // p2sh-p2wpkh
      else if (type == 'p2sh-p2wpkh') {
        path = "m/49'/2'/0'/0/0";
      }
      // p2wpkh
      else if (type == 'p2wpkh') {
        path = "m/84'/2'/0'/0/0";
      }
      return path;
    },

     // generate LTC address
    getLTCAddress(type, keyPair, network) {
      var data;
      // p2pkh
      if (type == 'p2pkh') {
        data = bitcoin.payments.p2pkh({
          pubkey: keyPair.publicKey,
          network: network,
        });
      }
      // p2sh-p2wpkh
      else if (type == 'p2sh-p2wpkh') {
        data = bitcoin.payments.p2sh({
          redeem: bitcoin.payments.p2wpkh({
            pubkey: keyPair.publicKey,
            network: network,
          }),
        });
      }
      // p2wpkh
      else if (type == 'p2wpkh') {
        data = bitcoin.payments.p2wpkh({
          pubkey: keyPair.publicKey,
          network: network,
        });
      }

      if (typeof data == 'undefined') {
        return '';
      }

      return data.address;
    },

    async genLTCKey() {
      const addressTypes = ['p2pkh', 'p2sh-p2wpkh', 'p2wpkh'];
      const LTC_NETWORK = {
        messagePrefix: '\x19Litecoin Signed Message:\n',
        bech32: 'ltc',
        bip32: {
          public: 0x019da462,
            private: 0x019d9cfe,
        },
        pubKeyHash: 0x30,
        scriptHash: 0x32,
        wif: 0xb0,
      };
      const mnemonic = generateMnemonic();
      const seed = await mnemonicToSeed(mnemonic);
      const master = bip32Obj.fromSeed(seed, LTC_NETWORK);
      const path = this.getLTCPath(addressTypes[0]);
      const keyPair = master.derivePath(path);
      this.ltcPrivateKey = keyPair.toWIF();
      this.ltcPublicKey = Buffer.from(keyPair.publicKey).toString('hex');
       for (let index = 0; index < addressTypes.length; index++) {
        let addressType = addressTypes[index];
        switch (index) {
          case 0:
            this.ltcAddress = this.getLTCAddress(
              addressType,
              keyPair,
              LTC_NETWORK
            );
            break;
          case 1:
            this.ltcP2SHAddress = this.getLTCAddress(
              addressType,
              keyPair,
              LTC_NETWORK
            );
            break;
          case 2:
            this.ltcNativeSegwitAddress = this.getLTCAddress(
              addressType,
              keyPair,
              LTC_NETWORK
            );
            break;
          default:
            break;
        }
      }
    },

    async genLTCKeyfromMnemonic() {
      const addressTypes = ['p2pkh', 'p2sh-p2wpkh', 'p2wpkh'];
      const LTC_NETWORK = {
        messagePrefix: '\x19Litecoin Signed Message:\n',
        bech32: 'ltc',
        bip32: {
          public: 0x019da462,
          private: 0x019d9cfe,
        },
        pubKeyHash: 0x30,
        scriptHash: 0x32,
        wif: 0xb0,
      };
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = await mnemonicToSeed(mnemonic);
      // // log
      // console.log('mnemonic:', mnemonic);
      // console.log('seed:', seed);

      const master = bip32Obj.fromSeed(seed, LTC_NETWORK);
      const path = this.getLTCPath(addressTypes[0]);
      const keyPair = master.derivePath(path);
      this.ltcPrivateKey = keyPair.toWIF();
      this.ltcPublicKey = Buffer.from(keyPair.publicKey).toString('hex');
      for (let index = 0; index < addressTypes.length; index++) {
        let addressType = addressTypes[index];
        switch (index) {
          case 0:
            this.ltcAddress = this.getLTCAddress(
              addressType,
              keyPair,
              LTC_NETWORK
            );
            break;
          case 1:
            this.ltcP2SHAddress = this.getLTCAddress(
              addressType,
              keyPair,
              LTC_NETWORK
            );
            break;
          case 2:
            this.ltcNativeSegwitAddress = this.getLTCAddress(
              addressType,
              keyPair,
              LTC_NETWORK
            );
            break;
          default:
            break;
        }
      }
    },

    // ---------- 
    async genPolkadotKey() {
      const mnemonic = mnemonicGenerate(12);
      // PrivateKey
      const seed = mnemonicToMiniSecret(mnemonic);
      this.polkadotPrivateKey = u8aToHex(seed);
      // address
      await cryptoWaitReady();
      const keyring = new Keyring({
        ss58Format: '0',
        type: 'sr25519',
      });
      const pair = keyring.addFromUri(mnemonic);
      this.polkadotAddress = pair.address;
      this.polkadotPublicKey = u8aToHex(pair.publicKey);
    },

    async genPolkadotKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      // PrivateKey
      const seed = mnemonicToMiniSecret(mnemonic);
      this.polkadotPrivateKey = u8aToHex(seed);
      // // log
      // console.log('mnemonic:', mnemonic);
      // console.log('seed:', seed);
      // console.log('this.polkadotPrivateKey:', this.polkadotPrivateKey);

      // address
      await cryptoWaitReady();
      const keyring = new Keyring({
        ss58Format: '0',
        type: 'sr25519',
      });
      const pair = keyring.addFromUri(mnemonic);
      this.polkadotAddress = pair.address;
      this.polkadotPublicKey = u8aToHex(pair.publicKey);
    },

    // ---------- 
    genAptosKey() {
      const account = new AptosAccount();
      this.aptosAddress = account.authKey().hexString;
      this.aptosPrivateKey = account.toPrivateKeyObject().privateKeyHex;
      this.aptosPublicKey = account.toPrivateKeyObject().publicKeyHex;
    },

    genAptosKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/637'/0'/0'/0'".toString();
      const account = AptosAccount.fromDerivePath(child, this.mnemonic);
      this.aptosAddress = account.authKey().hexString;
      this.aptosPrivateKey = account.toPrivateKeyObject().privateKeyHex;
      this.aptosPublicKey = account.toPrivateKeyObject().publicKeyHex;
    },

    // ---------- 
    genSolanaKey() {
      const account = Keypair.generate();
      this.solanaAddress = account.publicKey.toBase58();
      this.solanaPrivateKey = bs58.encode(account.secretKey);
      this.solanaPublicKey = account.publicKey;
    },

    async genSolanaKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = mnemonicToSeedSync(mnemonic);
      const account = Keypair.fromSeed(seed.slice(0, 32));
      // // log
      // console.log('mnemonic:', mnemonic);
      // console.log('seed:', seed);
      // console.log('account:',account);

      this.solanaAddress = account.publicKey.toBase58();
      this.solanaPrivateKey = bs58.encode(account.secretKey);
      this.solanaPublicKey = account.publicKey;
    },

    // ---------- 
    genEosKey() {
      ecc.randomKey().then((privateKey) => {
        this.eosPrivateKey = privateKey;
        this.eosPublicKey = ecc.privateToPublic(privateKey);
        this.eosAddress = ecc.privateToPublic(privateKey);
      });
    },

    genEosKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = mnemonicToSeedSync(mnemonic);
      const privateKey = ecc.seedPrivate(seed.toString());
      this.eosPrivateKey = privateKey;
      this.eosPublicKey = ecc.privateToPublic(privateKey);
      this.eosAddress = ecc.privateToPublic(privateKey);
    },

    // ---------- 
    genBinanceKey() {
      this.binancePrivateKey = BncClient.crypto.generatePrivateKey();
      const publicKey = BncClient.crypto.getPublicKeyFromPrivateKey(this.binancePrivateKey);
      this.binanceUncompressPublicKey = publicKey;
      this.binancePublicKey = compressPublicKey(publicKey);
      // console.log("publicKey:", publicKey);
      // console.log("this.binancePublicKey:", this.binancePublicKey);
      this.binanceAddress = BncClient.crypto.getAddressFromPrivateKey(
        this.binancePrivateKey,
        'bnb'
      );
    },

    genBinanceKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      this.binancePrivateKey = BncClient.crypto.getPrivateKeyFromMnemonic(mnemonic);
      const publicKey = BncClient.crypto.getPublicKeyFromPrivateKey(this.binancePrivateKey);
      this.binanceUncompressPublicKey = publicKey;
      this.binancePublicKey = compressPublicKey(publicKey);
      // console.log("publicKey:", publicKey);
      // console.log("this.binancePublicKey:", this.binancePublicKey);
      this.binanceAddress = BncClient.crypto.getAddressFromPrivateKey(
        this.binancePrivateKey,
        'bnb'
      );
    },

    // ---------- 
    genJingtumKey() {
      let wallet = Wallet.generate();
      this.jingtumAddress = wallet.address;
      this.jingtumPrivateKey = wallet.secret;
    },

    // ---------- 
    genCosmosKey() {
      let account = this.crypto.create();
      this.cosmosAddress = account.address;
      this.cosmosPrivateKey = account.privateKey;
      this.cosmosPublicKey = account.publicKey;
    },

    genCosmosKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/60'/0'/0/0".toString();
      let account = this.crypto.recover(mnemonic, "constants.Language.EN", child);
      this.cosmosAddress = account.address;
      this.cosmosPrivateKey = account.privateKey;
      this.cosmosPublicKey = account.publicKey;
    },

    // ---------- 
    genEthKey() {
      const randomWallet = ethers.Wallet.createRandom();
      // console.log('randomWallet:', randomWallet);
      this.ethAddress = randomWallet.address;
      this.ethPrivateKey = randomWallet.privateKey;
      // this.ethPublicKey = ethers.utils.computePublicKey(randomWallet.privateKey, true);
      const publicKey = randomWallet.publicKey.toString('hex');
      this.ethUncompressPublicKey = publicKey;
      this.ethPublicKey = '0x' + compressPublicKey(publicKey);
      // console.log('publicKey:', publicKey);
      // console.log('this.ethPublicKey:', this.ethPublicKey);

      // var account = this.web3.eth.accounts.create();
      // this.ethAddress = account.address;
      // this.ethPrivateKey = account.privateKey;
    },

    genEthKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/60'/0'/0/0";
      const walletMnemonic = ethers.Wallet.fromMnemonic(mnemonic, child);
      // console.log('walletMnemonic:', walletMnemonic);
      this.ethAddress = walletMnemonic.address;
      this.ethPrivateKey = walletMnemonic.privateKey;
      // this.ethPublicKey = ethers.utils.computePublicKey(walletMnemonic.privateKey,true);
      const publicKey = walletMnemonic.publicKey.toString('hex');
      this.ethUncompressPublicKey = publicKey;
      this.ethPublicKey = '0x' + compressPublicKey(publicKey);
      // console.log('publicKey:', publicKey);
      // console.log('this.ethPublicKey:', this.ethPublicKey);
    },

    // ---------- 
    genTronKey() {
      const mnemonic = mnemonicGenerate(12);
      const seed = mnemonicToSeedSync(mnemonic);
      const node = bip32Obj.fromSeed(seed);
      const child = node.derivePath("m/44'/195'/0'/0/0");
      const privateKey = child.privateKey.toString('hex');
      const publicKey = child.publicKey.toString('hex');
      const address = pkToAddress(privateKey).toString("hex");
      this.tronAddress = address;
      this.tronPrivateKey = privateKey;
      this.tronPublicKey = publicKey;

      // this.tronWeb.createAccount().then((res) => {
      //   this.tronAddress = res.address.base58;
      //   this.tronPrivateKey = res.privateKey;
      // });
    },

    genTronKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = mnemonicToSeedSync(mnemonic);
      const node = bip32Obj.fromSeed(seed);
      const child = node.derivePath("m/44'/195'/0'/0/0");
      const privateKey = child.privateKey.toString('hex');
      const publicKey = child.publicKey.toString('hex');
      const address = pkToAddress(privateKey).toString("hex");
      this.tronAddress = address;
      this.tronPrivateKey = privateKey;
      this.tronPublicKey = publicKey;
    },

    // ---------- 
    genIostKey() {
      var kp = iost.KeyPair.newKeyPair();
      this.iostPrivateKey = kp.B58SecKey();
      this.iostPublicKey = kp.B58PubKey();
      this.iostAddress = kp.B58PubKey();
    },

    genIostKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = mnemonicToSeedSync(mnemonic);
      var kp = new iost.KeyPair(seed);
      this.iostPrivateKey = kp.B58SecKey();
      this.iostPublicKey = kp.B58PubKey();
      this.iostAddress = kp.B58PubKey();
    },

    // ---------- 
    // generate path
    getBtcPath(type) {
      let path = '';
      // p2pkh
      if (type == 'p2pkh') {
        path = "m/44'/0'/0'/0/0";
      }
      // p2sh-p2wpkh
      else if (type == 'p2sh-p2wpkh') {
        path = "m/49'/0'/0'/0/0";
      }
      // p2wpkh
      else if (type == 'p2wpkh') {
        path = "m/84'/0'/0'/0/0";
      }
      // taproot
      else if (type == 'p2tr') {
        path = "m/86'/0'/0'/0/0";
      }
      return path;
    },

    // generate address
    getBtcAddress(type, keyPair, network) {
      var data;
      // p2pkh
      if (type == 'p2pkh') {
        data = bitcoin.payments.p2pkh({
          pubkey: keyPair.publicKey,
          network: network,
        });
      }
      // p2sh-p2wpkh
      else if (type == 'p2sh-p2wpkh') {
        data = bitcoin.payments.p2sh({
          redeem: bitcoin.payments.p2wpkh({
            pubkey: keyPair.publicKey,
            network: network,
          }),
        });
      }
      // p2wpkh
      else if (type == 'p2wpkh') {
        data = bitcoin.payments.p2wpkh({
          pubkey: keyPair.publicKey,
          network: network,
        });
      }
      // taproot
      else if (type == 'p2tr') {
        data = bitcoin.payments.p2tr({
          internalPubkey: keyPair.publicKey.slice(1, 33),
        });
      }
      if (typeof data == 'undefined') {
        return '';
      }

      return data.address;
    },

    async genBtcKey() {
      const addressTypes = ['p2pkh', 'p2sh-p2wpkh', 'p2wpkh', 'p2tr'];
      const network = bitcoin.networks.bitcoin;
      const mnemonic = generateMnemonic();
      const seed = await mnemonicToSeedSync(mnemonic);
      const master = bip32Obj.fromSeed(seed, network);
      const path = this.getBtcPath(addressTypes[0]);
      const keyPair = master.derivePath(path);
      this.btcPrivateKey = keyPair.toWIF();
      this.btcPublicKey = Buffer.from(keyPair.publicKey).toString('hex');
      for (let index = 0; index < addressTypes.length; index++) {
        let addressType = addressTypes[index];
        switch (index) {
          case 0:
            this.btcAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          case 1:
            this.btcP2SHAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          case 2:
            this.btcSegwitAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          case 3:
            this.btcTaprootAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          default:
            break;
        }
      }
    },

    async genBtcKeyfromMnemonic() {
      const addressTypes = ['p2pkh', 'p2sh-p2wpkh', 'p2wpkh', 'p2tr'];
      const network = bitcoin.networks.bitcoin;
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const seed = await mnemonicToSeedSync(mnemonic);
      // // log
      // console.log('mnemonic:', mnemonic);
      // console.log('seed:', seed);

      const master = bip32Obj.fromSeed(seed, network);
      const path = this.getBtcPath(addressTypes[0]);
      const keyPair = master.derivePath(path);
      this.btcPrivateKey = keyPair.toWIF();
      this.btcPublicKey = Buffer.from(keyPair.publicKey).toString('hex');
      for (let index = 0; index < addressTypes.length; index++) {
        let addressType = addressTypes[index];
        switch (index) {
          case 0:
            this.btcAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          case 1:
            this.btcP2SHAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          case 2:
            this.btcSegwitAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          case 3:
            this.btcTaprootAddress = this.getBtcAddress(
              addressType,
              keyPair,
              network
            );
            break;
          default:
            break;
        }
      }
    },

    // ---------- 
    genNervosKey() {
      let privateKey = ec.genKeyPair().priv;
      let address = new Address(privateKey, { prefix: 'ckb' });
      this.nervosPrivateKey = '0x' + address.getPrivateKey();
      this.nervosPublicKey = '0x' + address.publicKey;
      this.nervosAddress = address.value;
    },

    genNervosKeyfromMnemonic() {
      const mnemonic = this.mnemonic;
      if (!mnemonic) {
        return
      }
      if (!isMnemonic(mnemonic)) {
        console.log("Input is not a mnemonic");
        alert("Input is not a mnemonic");
        return
      }
      const child = "m/44'/309'/0'/0/0";
      const walletMnemonic = ethers.Wallet.fromMnemonic(mnemonic, child);

      let privateKey = walletMnemonic.privateKey;
      let address = new Address(privateKey, { prefix: 'ckb' });
      this.nervosPrivateKey = '0x' + address.getPrivateKey();
      this.nervosPublicKey = '0x' + address.publicKey;
      this.nervosAddress = address.value;
    },

    // ---------- ---------- ----------
    onGenerate() {
      switch (this.network) {
        case 'ETH':
          this.genEthKey();
          break;
        case 'EOS':
          this.genEosKey();
          break;
        case 'DOGE':
          this.genDogeKey();
          break;
        case 'IOST':
          this.genIostKey();
          break;
        case 'TRX':
          this.genTronKey();
          break;
        case 'BTC':
          this.genBtcKey();
          break;
        case 'ATOM':
          this.genCosmosKey();
          break;
        case 'BNB':
          this.genBinanceKey();
          break;
        case 'CKB':
          this.genNervosKey();
          break;
        case 'JMB':
          this.genJingtumKey();
          break;
        case 'SOL':
          this.genSolanaKey();
          break;
        case 'APT':
          this.genAptosKey();
          break;
        case 'DOT':
          this.genPolkadotKey();
          break;
        case 'BCH':
          this.genBCHKey();
          break;
        case 'LTC':
          this.genLTCKey();
          break;
        case 'CFX':
          this.genConfluxKey();
          break;
        case 'NOSTR':
          this.genNostrKey();
          break;
        case 'SUI':
          this.genSuiKey();
          break;
        default:
          break;
      }
    },

    onGenerateFromMnemonic() {
      localStorage.setItem('setmnemonic', this.mnemonic);  // cookie

      switch (this.network) {
        case 'ETH':
          this.genEthKeyfromMnemonic();
          break;
        case 'EOS':
          this.genEosKeyfromMnemonic();
          break;
        case 'DOGE':
          this.genDogeKeyfromMnemonic();
          break;
        case 'IOST':
          this.genIostKeyfromMnemonic();
          break;
        case 'TRX':
          this.genTronKeyfromMnemonic();
          break;
        case 'BTC':
          this.genBtcKeyfromMnemonic();
          break;
        case 'ATOM':
          this.genCosmosKeyfromMnemonic();
          break;
        case 'BNB':
          this.genBinanceKeyfromMnemonic();
          break;
        case 'CKB':
          this.genNervosKeyfromMnemonic();
          break;
        case 'JMB':
          this.genJingtumKey();
          break;
        case 'SOL':
          this.genSolanaKeyfromMnemonic();
          break;
        case 'APT':
          this.genAptosKeyfromMnemonic();
          break;
        case 'DOT':
          this.genPolkadotKeyfromMnemonic();
          break;
        case 'BCH':
          this.genBCHKeyfromMnemonic();
          break;
        case 'LTC':
          this.genLTCKeyfromMnemonic();
          break;
        case 'CFX':
          this.genConfluxKeyfromMnemonic();
          break;
        case 'NOSTR':
          this.genNostrKeyfromMnemonic();
          break;
        case 'SUI':
          this.genSuiKeyfromMnemonic();
          break;
        default:
          break;
      }
    },

    onSelectChain(chain, index) {
      this.network = chain.network;
      this.chainId = chain.chainId;
      this.ss58 = chain.ss58;
      this.curIndex = index;
      this.isMobileChain = false;
    },

    showMobileChain() {
      this.isMobileChain = true;
    },

    onClose() {
      this.isMobileChain = false;
    },
  },
};

function isMnemonic(input) {
  let words = input.trim().split(/\s+/);
  return words.length >= 12 && words.length <= 24;
}
function isPrivateKey(input) {
  let hex = input.trim();
  return hex.length === 64 && /^[0-9a-fA-F]+$/.test(hex);
}
function compressPublicKey(publicKey) {
  publicKey = publicKey.replace('0x', '').replace('0X', '').replace(' ', '');
  console.log("publicKey.length:", publicKey.length);
  var compressedKeyIndex;
  if (publicKey.substring(0, 2) !== "04") {
    throw "Invalid public key format";
  }
  if (parseInt(publicKey.substring(128, 130), 16) % 2 !== 0) {
    compressedKeyIndex = "03";
  } else {
    compressedKeyIndex = "02";
  }
  var result = compressedKeyIndex + publicKey.substring(2, 66);
  return result;
  // return result.toLowerCase(); // 转换为小写
}
</script>

<style lang="scss">
@import '../style/home.scss';
.mnemonic-item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 74px;
  transform: translate3d(0, -100%, 0);

  .mnemonic-name {
    font-size: 16px;
    color: #828282;
  }

  .mnemonic-input {
    width: 100%;
    height: 19px;
    padding: 8px 10px;
    border-radius: 8px;
    overflow: auto;
    position: absolute;
    vertical-align: middle;
    background: #f5f6f7;
  }
}
</style>
