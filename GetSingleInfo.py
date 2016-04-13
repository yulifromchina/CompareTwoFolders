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
输入：文件的路径，从哪个字符开始截断这个路径（截断后的目录为“360safe_Windows”或者“360safe_Servers”的后面开始的目录）
输出：截断后的文件路径

GetPrefix:
输入：文件的路径，从哪个字符开始截断这个路径（截断后的目录为……\360safe_Windows或者……\360safe_Servers）
输出：截断符号前的文件路径
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

    #读取pe文件失败，抛出异常，返回空
    try:
        fp = pefile.PE(filepath)
    except:
        return 'NULL'

    #pe文件格式格式不全，输出文件路径，返回空
    try:
        temp = fp.FileInfo
    except AttributeError:
        print 'StrangeFile='
        print filepath
        return 'NULL'
    
    #如果不能通过'FileVersion'获取版本号，就通过'ProductVersion'获取
    try:
        FileVersion=fp.FileInfo[0].StringTable[0].entries['FileVersion']
    except:
        FileVersion=fp.FileInfo[0].StringTable[0].entries['ProductVersion']
    
    return FileVersion

def GetFileName(filepath):
    return os.path.split(filepath)[1]
    
def GetFatherPath(filepath):
    return os.path.split(filepath)[0]

def GetCutoffPath(filepath, cutoff=r'360safe_'):
    filepath = filepath
    start = filepath.find(cutoff)
    if (filepath.find(r'Windows')):
	start = start + len('360safe_Windows')+1
	#从360safe_windows处截断
    else:
	start = start + len('360safe_Servers')+1
	#从360safe_servers处截断
    return filepath[start:]

def GetPrefix(filepath, cutoff=r'360safe_'):
    filepath = filepath
    end = filepath.find(cutoff)
    if (filepath.find(r'Windows')):
	end = end + len('360safe_windows')+1
	#从360safe_windows处截断
    else:
	end = end + len('360safe_Servers')+1
	#从360safe_servers处截断

    return filepath[:end]
