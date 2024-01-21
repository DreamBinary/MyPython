import mod  #同级目录
import os
print('----------------')
mod.whs()

import sys
print(sys.path)

#不在同级 sys.path.append() 添加路径
print(__file__)  #打印当前脚本目录
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))





















