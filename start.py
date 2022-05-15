from requests import head


# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File    :   start.py
@Time    :   2022/05/15 21:05:58
@Author  :   taobo
@Version :   1.0
@Contact :   taobo@btcex.com
@License :   (C)Copyright 2019-2022
@Desc    :   None
"""

import sys,os
#将环境目录增加到path目录
path=os.path.dirname(__file__)
# print(path)
sys.path.append(path)

from core import src

if __name__ == '__main__':
    src.run()