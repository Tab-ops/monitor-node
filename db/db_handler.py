from conf import setting
def data_fmt(name,data):
    try:
        current_ver ='{}{}'.format(data,setting.node_dic[name]['fmt'])
        return eval(current_ver)
    except Exception as e:
        return '获取版本错误'

    

