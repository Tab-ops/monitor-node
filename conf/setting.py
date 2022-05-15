import os 
DIR_PATH=os.path.dirname(os.path.dirname(__file__))
# print(DIR_PATH)
BASE_LOG= os.path.join(DIR_PATH,'log')
# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(BASE_LOG):
    os.mkdir(BASE_LOG)

# log文件的全路径
logfile_path = os.path.join(BASE_LOG, 'node-version.log')

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*5*1024,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },


    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

node_dic = {
    "btc":{
        "node_url":"https://mainnet-node.bitcharm.com/btc",
        "office_url":"https://api.github.com/repos/bitcoin/bitcoin/releases/latest",
        "method":"POST",
        "user":"bitcoin",
        "passwd":"G3aNIjgOOp383UI5LBCRCJwe8wsFthXzUqA3yvVBd1M=",
        "m":"getnetworkinfo",
        "fmt":"['result']['subversion'].split(':')[1][:-1]"
    },
    "ltc":{
        "node_url":"https://mainnet-node.bitcharm.com/ltc",
        "office_url":"https://api.github.com/repos/litecoin-project/litecoin/releases/latest",
        "method":"POST",
        "user":"btcex_ltc",
        "passwd":"qtoyVQ6sCT9-1aBpFTuL3s9gbFRVFQLhnorB7WyaCGo=",
        "m":"getnetworkinfo",
        "fmt":"['result']['subversion'].split(':')[1][:-1]"
    },
    "eth":{
        "node_url":"https://mainnet-node.bitcharm.com/eth",
        "office_url":"https://api.github.com/repos/ethereum/go-ethereum/releases/latest",
        "method":"POST",
        "user":"",
        "passwd":"",
        "m":"web3_clientVersion",
        "fmt":"['result'].split('/')[1].split('-')[0]"
    },
    "bsc":{
        "node_url":"https://mainnet-node.bitcharm.com/bsc",
        "office_url":"https://api.github.com/repos/binance-chain/bsc/releases/latest",
        "method":"POST",
        "user":"",
        "passwd":"",
        "m":"web3_clientVersion",
        "fmt":"['result'].split('/')[1].split('-')[0]"
    },
    "trx":{
        "node_url":"https://mainnet-node.bitcharm.com/trx/wallet/getnodeinfo",
        "office_url" :"https://api.github.com/repos/tronprotocol/java-tron/releases/latest",
        "method":"GET",
        "user":"",
        "passwd":"",
        "m":"",
        "fmt":"['configNodeInfo']['codeVersion']"
    },
    "sol":{
        "node_url":"https://mainnet-node.bitcharm.com/sol",
        "office_url":"https://api.mainnet-beta.solana.com",
        "method":"POST",
        "user":"",
        "passwd":"",
        "m":"getVersion",
        "fmt":"['result']['solana-core']"
    },
    "dot":{
        "node_url":"https://mainnet-node.bitcharm.com/dot-rpc",
        "office_url":"https://api.github.com/repos/paritytech/polkadot/releases/latest",
        "method":"POST",
        "user":"",
        "passwd":"",
        "m":"system_version",
        "fmt":"['result'].split('-')[0]"
    },
    "xrp":{
        "node_url":"https://mainnet-node.bitcharm.com/xrp",
        "office_url":"https://api.github.com/repos/ripple/rippled/releases/latest",
        "method":"POST",
        "user":"",
        "passwd":"",
        "m":"server_info",
        "fmt":"['result']['info']['build_version']"
    },
    "klay":{
        "node_url":"https://mainnet-node.bitcharm.com/klay",
        "office_url":"https://api.github.com/repos/klaytn/klaytn/releases/latest",
        "method":"POST",
        "user":"",
        "passwd":"",
        "m":"klay_clientVersion",
        "fmt":"['result'].split('/')[1].split('+')[0]"
    },
    "luna":{
        "node_url":"https://mainnet-node.bitcharm.com/luna-api/node_info",
        "office_url":"https://api.github.com/repos/terra-money/core/releases/latest",
        "method":"GET",
        "user":"",
        "passwd":"",
        "m":"",
        "fmt":"['application_version']['version']"
    },
    "atom":{
        "node_url":"https://mainnet-node.bitcharm.com/gaia-api/node_info",
        "office_url":"https://api.github.com/repos/cosmos/gaia/releases/latest",
        "method":"GET",
        "user":"",
        "passwd":"",
        "m":"",
        "fmt":"['application_version']['version']"
    }
}

