# -*- coding:utf-8 -*-
'''
这个文件用于获取单个文件的信息
CalcSha1:
输入：文件的路径  输出：文件的hash值

CalcMD5:
输入:文件的路径  输出：文件的MD5

GetFileVersion:
输入：文件的路径 输出：文件的版本号

GetFileName:
输入：文件的路径 输出：文件名称

GetFatherPath:
输入：文件的路径  输出：文件路径（去掉了文件名）

GetCutoffPath:
输入：文件的路径，从哪个字符开始截断这个路径（默认为360）
输出：截断后的文件路径

GetPrefix:
输入：文件的路径，从哪个字符开始截断这个路径（默认为360）
输出：截断符号签名的文件路径
'''
import hashlib
import os,sys
import pefile

def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash
 
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        MD5 = md5obj.hexdigest() 
        return MD5

def GetFileVersion(filepath):
    try:
        fp = pefile.PE(filepath)
    except:
        return 'NULL'
    FileVersion=fp.FileInfo[0].StringTable[0].entries['FileVersion']
    return FileVersion

def GetFileName(filepath):
    return os.path.split(filepath)[1]
    
def GetFatherPath(filepath):
    return os.path.split(filepath)[0]

def GetCutoffPath(filepath, cutoff='360'):
    start = filepath.find(cutoff)
    return filepath[start:]

def GetPrefix(filepath, cutoff='360'):
    end = filepath.find(cutoff)
    return filepath[:end]
