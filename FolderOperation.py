# -*- coding:utf-8 -*-
'''
这个文件用于指定文件夹下，所有文件的完整路径
完整路径是一个列表，列表中又包含很多列表：
[类型一的路径列表，类型二的路径列表，类型三的路径列表……]
'''
import glob,os



def FindInSingleDir(dirname):
    '''
    输入参数：路径名称，是一个文件夹，但不含有子文件夹
    输出：一个包含所有路径的列表，列表中又包含很多小列表
    [类型一的列表，类型二的列表，类型三的列表……]
    类型一是dll，类型二是exe,……
    '''
    allFile = []
    allDll = glob.glob(dirname+os.sep+'*.dll')
    allFile.append(allDll)
    allExe = glob.glob(dirname+os.sep+'*.exe')
    allFile.append(allExe)
    return allFile
    
def FindInEntireDir(dirname):
    '''
    输入参数：路径名称，是一个文件夹，包括了子文件夹
    输出参数：一个包含所有路径的列表，列表中又包含很多小列表
    [类型一的列表，类型二的列表，类型三的列表……]
    类型一是dll，类型二是exe,……
    '''
    allFile = []
    allDll = []
    allExe = []
    for(thisDir, subsHere, filesHere) in os.walk(dirname):
        subFile = FindInSingleDir(thisDir)
        allDll+=subFile[0]
        allExe+=subFile[1]
    allFile.append(allDll)
    allFile.append(allExe)
    return allFile
    
