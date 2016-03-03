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
    类型一是dll，类型二是exe,类型三是sys，类型四是.ext，类型五是.tpi……
    '''
    allFile = []
    allDll = glob.glob(dirname+os.sep+'*.dll')
    tempDll = []
    
    #删除后缀名为.dll的文件夹
    for rev in allDll:
        if os.path.isfile(rev):
            tempDll.append(rev)
            

    allFile.append(tempDll)
        
    allExe = glob.glob(dirname+os.sep+'*.exe')
    tempExe = []
    #删除后缀名为.exe的文件夹
    for rev in allExe:
        if os.path.isfile(rev):
            tempExe.append(rev)
         
    allFile.append(tempExe)

    allSys = glob.glob(dirname+os.sep+'*.sys')
    tempSys = []
    #删除后缀名为.sys的文件夹
    for rev in allSys:
        if os.path.isfile(rev):
            tempSys.append(rev)

    allFile.append(tempSys)

    allExt = glob.glob(dirname+os.sep+'*.ext')
    tempExt = []
    #删除后缀名为.ext的文件夹
    for rev in allExt:
        if os.path.isfile(rev):
            tempExt.append(rev)

    allFile.append(tempExt)

    allTpi = glob.glob(dirname+os.sep+'*.tpi')
    tempTpi = []
    #删除后缀名为.tpi的文件夹
    for rev in allTpi:
        if os.path.isfile(rev):
            tempTpi.append(rev)
    
    allFile.append(tempTpi)
    
    return allFile
    
def FindInEntireDir(dirname):
    '''
    输入参数：路径名称，是一个文件夹，包括了子文件夹
    输出参数：一个包含所有路径的列表，列表中又包含很多小列表
    [类型一的列表，类型二的列表，类型三的列表……]
    类型一是dll，类型二是exe,类型三是sys，类型四是ext，类型五是.tpi……
    '''
    allFile = []
    allDll = []
    allExe = []
    allSys = []
    allExt = []
    allTpi = []
    
    for(thisDir, subsHere, filesHere) in os.walk(dirname):
        subFile = FindInSingleDir(thisDir)
        allDll+=subFile[0]
        allExe+=subFile[1]
        allSys+=subFile[2]
        allExt+=subFile[3]
        allTpi+=subFile[4]
        
    allFile.append(allDll)
    allFile.append(allExe)
    allFile.append(allSys)
    allFile.append(allExt)
    allFile.append(allTpi)
    
    return allFile
