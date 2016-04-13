# -*- coding:utf-8 -*-
'''
这个文件用于读取指定文件夹下，所有文件的信息

1.读取给定文件夹的所有信息，一个文件夹的信息存储成一个字典
{文件一的健：文件一的值，文件二的健：文件二的值，文件三的健，文件三的值……}
2.文件的健，用文件的完整路径表示
3.文件的值，是一个列表，包括：
[文件的名称，文件的md5值，文件的版本号，文件被截断的名称……]
'''
from GetSingleInfo import *

def GetFullInfo(name_list):
    '''
    输入参数：文件列表，这个列表可能也包含多个列表
    返回：一个字典，包括这个文件夹下所有文件的信息
    '''
    fullInfo = {}
    for sublist in name_list:
        info = []
        for filepath in sublist:
            filepath = filepath
            filename = GetFileName(filepath)
            md5 = CalcMD5(filepath)
            version = GetFileVersion(filepath)            
            cut_filename = GetCutoffPath(filepath)
            info = [filename, md5, version, cut_filename]
            fullInfo[filepath] = info
            
    return fullInfo
    
