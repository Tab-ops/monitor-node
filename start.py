import sys,os
#将环境目录增加到path目录
path=os.path.dirname(__file__)
# print(path)
sys.path.append(path)

from core import src

if __name__ == '__main__':
    src.run()