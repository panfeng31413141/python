#the Standard Library
#os库
#shutil库
#glob库
#sys库
#argparse库
#re库
#math库
#random库
#statistics库
#urllib库
#smtplib库
#datetime库
#zlib库
#timeit库
#doctest库
#unittest库

#os:提供与操作系统交互的功能
import os
os.getcwd()#返回当前目录
print(os.getcwd())

import os
dir(os)#返回os库所有属性


import os
help(os)#获取os的帮助信息


#shutil:提供文件操作功能,例如复制、删除、移动等操作
import shutil
shutil.copyfile("data.db","archive.db")#文件复制,将data.db的文件复制到archive.db
shutil.move("/build/executables","installdir")#将文件或目录移到新的位置

#glob:
import glob
glob.glob("*.py")

#sys





