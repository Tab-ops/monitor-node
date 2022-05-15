from unicodedata import name
from interface import version,weixin
from conf import setting
from db import db_handler
v = []
def NodeVersion(name):
    ver = version.NodeVersion_interface(name)
    current_ver = db_handler.data_fmt(name,ver)
    return current_ver

def OfficeVersion(name):
    latest_ver = version.OfficeVersion_interface(name)
    return latest_ver

def getversion():
    for i in setting.node_dic:
        current = NodeVersion(i)
        latest = OfficeVersion(i)
        v.append('{}:当前:{},最新:{}'.format(i, current, latest))
    return v

def send_msg():
    ver = getversion()
    d = '\n'.join(ver)
    flag,msg = weixin.send_msg(d)
    if flag:
        print(msg)
    else:
        print(msg)
def run():
    send_msg()