import re

# --------------------------------------------------------------------
"""
Bitcoin (BTC): 地址有 P2PKH、P2SH 和 Bech32 格式。
    - P2PKH:  以 1/3 开头，           后面跟随 26 到 33 个 Base58 编码字符。     正则表达式: ^[13][1-9A-HJ-NP-Za-km-z]{26,33}$
    - P2SH:   以 3 开头，             后面跟随 26 到 33 个 Base58 编码字符。     正则表达式: ^[3][1-9A-HJ-NP-Za-km-z]{26,33}$
    - Bech32: 以 bc1 开头，           后面跟随 2 到 87 个 Bech32 编码字符。      正则表达式: ^bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{2,87}$
BitcoinCash (BCH): 地址有 P2PKH、P2SH 和 Bech32 格式。
    - P2PKH: 以 1/3 开头，            后面跟随 25 到 33 个 Base58 编码字符。     正则表达式: ^[13][1-9A-HJ-NP-Za-km-z]{25,33}$
    - P2SH:  以 3 开头，              后面跟随 25 到 33 个 Base58 编码字符。     正则表达式: ^[3][1-9A-HJ-NP-Za-km-z]{25,33}$
    - Bech32: 以 bitcoincash: 开头，  后面跟随  2 到 87 个 Bech32 编码字符。     正则表达式: ^bitcoincash:[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{2,87}$
Dogecoin (DOGE): 地址有 P2PKH 和 P2SH 格式。
    - P2PKH: 以 D/d 开头，     后面跟随 25 到 33 个 Base58 编码字符。             正则表达式: ^[Dd][1-9A-HJ-NP-Za-km-z]{25,33}$
    - P2SH:  以 7/A 开头，     后面跟随 25 到 33 个 Base58 编码字符。             正则表达式: ^[7A][1-9A-HJ-NP-Za-km-z]{25,33}$
Litecoin (LTC): 地址有 P2PKH 和 P2SH 格式。
    - P2PKH: 以 L/M 开头，     后面跟随 25 到 33 个 Base58 编码字符。             正则表达式: ^[LM][1-9A-HJ-NP-Za-km-z]{25,33}$
    - P2SH:  以 3 开头，       后面跟随 25 到 33 个 Base58 编码字符。             正则表达式: ^[3][1-9A-HJ-NP-Za-km-z]{25,33}$
Filecoin (FIL): 地址有 f1 和 f3 类型。
    - f1: 以 f1 开头，后面跟随 38 个 Base32 编码字符。                        正则表达式: ^f1[1-9A-HJ-NP-Za-km-z]{38}$
    - f3: 以 f3 开头，后面跟随 84 个 Base32 编码字符。                        正则表达式: ^f3[1-9A-HJ-NP-Za-km-z]{84}$

Solana:    有 44 个 Base58 编码字符。                                        正则表达式: ^[1-9A-HJ-NP-Za-km-z]{44}$
Ethereum:  以 0x 开头，     后面跟随 40 个十六进制字符（0-9, a-f, A-F）。      正则表达式: ^0x[a-fA-F0-9]{40}$
SUI/Aptos: 以 0x 开头，     后面跟随 64 个十六进制字符（0-9, a-f, A-F）。      正则表达式: ^0x[a-fA-F0-9]{64}$
Polkadot:  以 1 开头，      后面跟随 31 个字母数字字符（a-z, A-Z, 0-9）。      正则表达式: ^1[a-zA-Z0-9]{31}$
TRON:      以 T 开头，      后面跟随 33 个字母数字字符（a-z, A-Z, 1-9）。      正则表达式: ^T[a-zA-Z1-9]{33}$
EOS:       以 EOS 开头，    后面跟随 12 个字母字符（a-z, A-Z, 1-5）。          正则表达式: ^EOS[a-zA-Z1-5]{12}$
COSMOS:    以 cosmos1 开头，后面跟随 38 个字母数字字符（a-z, 0-9）。           正则表达式: ^cosmos1[a-z0-9]{38}$
Binance:   以 bnb1 开头，   后面跟随 38 个字母数字字符（a-z, 0-9）。           正则表达式: ^bnb1[a-z0-9]{38}$
"""
# --------------------------------------------------------------------

# 通用钱包地址
def is_wallet_address(address: str) -> bool:
    patterns = [
        r'^0x[a-fA-F0-9]{40}$',  # Ethereum
        r'^[1][1-9A-HJ-NP-Za-km-z]{26,33}$',  # Bitcoin P2PKH
        r'^[3][1-9A-HJ-NP-Za-km-z]{26,33}$',  # Bitcoin P2SH
        r'^bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{2,87}$',  # Bitcoin Bech32
        r'^1[a-zA-Z0-9]{31}$',  # Polkadot
        r'^T[a-zA-Z1-9]{33}$'  # TRON
        r'^[1-9A-HJ-NP-Za-km-z]{44}$'  # Solana
        r'^f1[1-9A-HJ-NP-Za-km-z]{38}$'  # Filecoin f1
        r'^f3[1-9A-HJ-NP-Za-km-z]{84}$'  # Filecoin f3
        r'^0x[a-fA-F0-9]{64}$',  # SUI / Aptos
        r'^[Dd][1-9A-HJ-NP-Za-km-z]{25,33}$',  # Dogecoin P2PKH
        r'^[7A][1-9A-HJ-NP-Za-km-z]{25,33}$',  # Dogecoin P2SH
        r'^EOS[a-zA-Z1-5]{12}$',  # EOS
        r'^cosmos1[a-z0-9]{38}$',  # COSMOS
        r'^bnb1[a-z0-9]{38}$',  # Binance
        r'^[LM][1-9A-HJ-NP-Za-km-z]{25,33}$',  # Litecoin P2PKH
        r'^[3][1-9A-HJ-NP-Za-km-z]{25,33}$',  # Litecoin P2SH
        r'^bitcoincash:[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{2,87}$'  # BitcoinCash Bech32
    ]
    return any(bool(re.match(pattern, address)) for pattern in patterns)

print(is_wallet_address("0x742d35Cc6634C0532925a3b844Bc454e4438f44e"))  # 输出: True

# 增加 ETH BTC Polkadot TRON Solana Filecoin sui aptos Dogecoin EOS COSMOS Binance LTC BCH 等钱包地址校验
# 说出 ETH BTC Polkadot TRON Solana Filecoin sui aptos Dogecoin EOS COSMOS Binance LTC BCH 等钱包地址正则校验原理
