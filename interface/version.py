from conf import setting
from lib import common
import requests
import json
version_logger=common.get_logger('获取版本')
headers = {
  'Content-Type': 'application/json'
}
def payload(name):
    if name == 'xrp':
        data = json.dumps({
            "method": "{}".format(setting.node_dic[name]['m']),
            "params": [
                {
                    "api_version": 1
                }
            ]
        })
    else:
        data = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "{}".format(setting.node_dic[name]['m'])
        })
    return data

def NodeVersion_interface(name):
    try:
        if  setting.node_dic[name]['method'] == 'POST':
            response = requests.request(method=setting.node_dic[name]['method'], url=setting.node_dic[name]['node_url'], auth=(setting.node_dic[name]['user'],setting.node_dic[name]['passwd']),headers=headers, data=payload(name))
            version_logger.info('%s 获取本地版本正确'%(name))
            return response.json()
        elif setting.node_dic[name]['method'] == 'POST' and setting.node_dic[name] == "xrp":
            response = requests.request(method=setting.node_dic[name]['method'], url=setting.node_dic[name]['node_url'], auth=(setting.node_dic[name]['user'],setting.node_dic[name]['passwd']),headers=headers, data=payload(name))
            version_logger.info('%s 获取本地版本正确'%(name))
            return response.json()
        elif setting.node_dic[name]['method'] == 'GET':
            response = requests.request(method=setting.node_dic[name]['method'], url=setting.node_dic[name]['node_url'])
            version_logger.info('%s 获取本地版本正确'%(name))
            return response.json()
        else:
            print('ok')   
    except Exception as e:
        version_logger.info('%s 获取本地版本错误,message:%s'%(name,e))
        return '获取版本错误'

def OfficeVersion_interface(name):
    try:
        if name == 'sol':
            response = requests.request(method=setting.node_dic[name]['method'], url=setting.node_dic[name]['office_url'],headers=headers,data=payload(name))
            version_logger.info('%s 获取官方版本正确'%(name))
            return response.json()['result']['solana-core']
        else:
            response = requests.request(method="GET",url=setting.node_dic[name]['office_url'])
            # return response.json()
            version_logger.info('%s 获取官方版本正确'%(name))
            return response.json()['tag_name']
    except Exception as e:
        version_logger.info('%s 获取官方版本错误,message:%s'%(name,e))
        return '获取版本错误'