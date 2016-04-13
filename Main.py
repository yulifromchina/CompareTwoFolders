#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
接口函数：
filepath1: 旧包的路径
filepath2: 新包的路径
txt_path:  生成结果的路径
'''
from CompareInfo import *
from FolderOperation import *

if __name__ == '__main__':
#	filepath1 = r'C:\Users\Administrator\Desktop\compare\patch1\360safe_Servers'
#	filepath2 = r'C:\Users\Administrator\Desktop\compare\patch1\360safe_Windows'
	filepath1 = r'/home/share/released/1400/360safe_Windows'
	filepath2 = r'/home/share/360safe_Windows'
	txt_path = r'/mnt/share'
	Compare(filepath1, filepath2, txt_path)



