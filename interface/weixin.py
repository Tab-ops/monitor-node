import requests
from lib import common
headers = {"Content-Type": "application/json"}
send_logger=common.get_logger('发送消息')
send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b13a9432-b84d-460d-b48d-7cc7db7f659f"
def send_msg(d):
    send_data = {
        "msgtype": "text",
        "text": {
            "content": "{}".format(d)
        }
    }
    try:
        res = requests.request("POST",url=send_url, headers=headers, json=send_data)
        send_logger.info('发送消息成功,message:%s'%(res.text)) 
        return True,res.text
    except Exception as e:
        send_logger.info('发送消息失败,message:%s'%(e)) 
        return '发送消息失败'