import os
import re

PROJECT_PATH, _ = os.path.split(os.path.realpath(__file__))
PC_TRACER_RELATED_PATH = 'misc/tracer.js'
with open(os.path.join(PROJECT_PATH, PC_TRACER_RELATED_PATH), 'r') as f:
    PC_TRACER = f.read()
    PC_TRACER = PC_TRACER[9:]
    PC_TRACER = re.sub('\n|\t', '', PC_TRACER)

TYPED_AST_CODE_RELATED_PATH = 'misc/ast.js'
with open(os.path.join(PROJECT_PATH, TYPED_AST_CODE_RELATED_PATH), 'r') as f:
    TYPED_AST_CODE = f.read()

SOLCJS_CODE_RELATED_PATH = 'misc/solcjs.js'
with open(os.path.join(PROJECT_PATH, SOLCJS_CODE_RELATED_PATH), 'r') as f:
    SOLCJS_CODE = f.read()

CACHE_DIR = os.path.join(PROJECT_PATH, 'data/cache')

TMP_FILE_DIR = os.path.join(PROJECT_PATH, 'tmp')
if not os.path.exists(TMP_FILE_DIR):
    os.makedirs(TMP_FILE_DIR)

NODE_PATH = 'node'

SCAN_APIKEYS = {
    'Ethereum': [
        'https://api.etherscan.io/api?apikey=4QP6SY9V7XXDJDEJBGC1NAI3KXRIU5CDEE',
        'https://api.etherscan.io/api?apikey=Y3HRQPY2RXG6CQNJSV7QJXDZ1S2SCKTVTD',
        'https://api.etherscan.io/api?apikey=XIUCSG7G93C5X7QNEZICXBWRS9SKUZY7KW',
        'https://api.etherscan.io/api?apikey=3RDEEN6RNS694NQTCTENUKQPI7FY147KIA',
        'https://api.etherscan.io/api?apikey=AZI8P3UZBWIFY93UKDHUPN8QC9MVH26N2E',
        'https://api.etherscan.io/api?apikey=9DHD6VRXGI5747TFE6D8F2RAIY79ZST16I',
        'https://api.etherscan.io/api?apikey=VUX7GADFQWS3ZY667FIBU8M7U8PGYPQ42J',
        'https://api.etherscan.io/api?apikey=C7JHK7ZBEQJWMKC6AYTRUIMIJMMIFAF7K3',
        'https://api.etherscan.io/api?apikey=1S6HVVBYA9A1TH4UJ1HFPH5MXAATIZT3ER',
        'https://api.etherscan.io/api?apikey=64GTQD9HUSDKACZQ1H4AAPYWWF4GZUYA7I',
        'https://api.etherscan.io/api?apikey=XA7QR77WE59MEFSSZJ81QB6RCA9YKE8TYJ',
        'https://api.etherscan.io/api?apikey=H2WU5N2A1CQFCBA5N6MHJ7V4HWE3QK4VHS',
        'https://api.etherscan.io/api?apikey=KC2IM55M9UR13FC2JWW86EGY2SR3XNRWIA',
        'https://api.etherscan.io/api?apikey=32D4QMS1KB3XGEG1YG99MEBQX9XUEUSBNC',
        'https://api.etherscan.io/api?apikey=MCDE2ZV3GVKQBRSJ5V4VE82NHT32NM4A2Z',
        'https://api.etherscan.io/api?apikey=99B5J7A8RGP7ZQDSHSMN428NMS59J4DD51',
        'https://api.etherscan.io/api?apikey=1AHNVWUGE9K6HYHVHQIG5DUCHP7AM421GQ',
        'https://api.etherscan.io/api?apikey=HBV2JXKQ9P4BGWGCB7DJB5GJIVRB45N3UR',
        'https://api.etherscan.io/api?apikey=TE92WJABYJZV7IKEQGSE7PYPHYUZ8TVX2F',
        'https://api.etherscan.io/api?apikey=4JX4TB3WQTJH3J4D182NAFEZS9W19MAIZ9'
    ],
    'BNBChain': [
        'https://api.bscscan.com/api?apikey=3FYU1X8HNHNQ287PUIXZBFYWT78TBPG4P6',
        'https://api.bscscan.com/api?apikey=NYYFYM2GM9FPCFETAMHHBXN67X7PU46EB9',
        'https://api.bscscan.com/api?apikey=ZG2QVNZEMYM1CT1NU6DGI2K2A4DPNERTWG',
        'https://api.bscscan.com/api?apikey=7VR51MAFHY35ZPFUZH111IIZ5IMXG14HWA',
        'https://api.bscscan.com/api?apikey=PYTAMC2MXKD47UXU6Y5ERNDR1HZCYHUJ9Q',
        'https://api.bscscan.com/api?apikey=RU7VE149UMYSKE98KKI5ICKEBCA2C7F5UA',
        'https://api.bscscan.com/api?apikey=MT2DU9SZ9RJPV1WWFSUEUE9TK3R3VN7UXB',
        'https://api.bscscan.com/api?apikey=TF68S9DJ3UWMFA7GRPAFF7I9TSIQ3MJRSK'
    ],
}

JSONRPCS = {
    'Ethereum': [
        # 'https://mainnet.chainnodes.org/965e82de-fa68-404c-82b9-6f078bdb3c30',
        'https://mainnet.chainnodes.org/112ae60a-a46d-45a2-9e2e-322ca16d9ce4',
        'https://mainnet.chainnodes.org/965e82de-fa68-404c-82b9-6f078bdb3c30',
        'https://mainnet.chainnodes.org/c4cb0bc7-4b66-4b17-8429-ecef107ef315',
        'https://mainnet.chainnodes.org/9243a4a3-42c3-4ce0-b379-d505cd1e1d46',
        'https://mainnet.chainnodes.org/c2db8f3e-fd09-44d4-be0e-537b43dfb804',
    ],
    'BNBChain': [
        'https://bsc-mainnet.chainnodes.org/b148f00b-c9b4-48bf-b442-76ecf18bd85e',
        'https://bsc-mainnet.chainnodes.org/9c408170-0042-4ff0-bb1c-2f3e44284644',
        'https://bsc-mainnet.chainnodes.org/2b65aab8-473f-449f-8533-7959f521e579',
        'https://bsc-mainnet.chainnodes.org/f70d9d8b-58e7-4ef2-b87d-cf151571e23d',
        'https://bsc-mainnet.chainnodes.org/348f2d5b-c8d8-41fe-a471-8742bc4d777c',
    ]
}