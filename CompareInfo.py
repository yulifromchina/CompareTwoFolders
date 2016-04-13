# -*- coding:utf-8 -*-
'''
这个文件用于比较并输入两个文件夹内，所有有差异的文件的信息
输入：
旧包文件夹所在路径
新包文件夹所在路径
输出结果所在路径（可选，不填写则默认为/mnt/share）

输出的信息有：
旧包删除的文件
新包增加的文件
版本号应该提升，但没有提升的文件

'''
from FolderOperation import *
from FolderFullInfo import *
from GetSingleInfo import *

def Compare(path1, path2, txt_path = r'/mnt/share'):
    '''
    输入：两个文件夹的路径 
    '''

    #分别获取这两个文件夹下的文件路径列表
    #每个列表又包含很多小列表
    #例如：allFile1[0]=[exe文件的路径]zbxc，allFile1[1]=[dll文件的路径]
    allFile1 = FindInEntireDir(path1)
    allFile2 = FindInEntireDir(path2)

    #分别获取这两个文件夹的整个信息字典
    fullInfo1 = GetFullInfo(allFile1)
    fullInfo2 = GetFullInfo(allFile2)

    #默认前一个路径为旧包路径，后一个路径为新包路径
    
    #取各个文件夹下的文件路径，都去除前缀，来做交、并的集合操作
    list1 = []
    list2 = []
    for sub_file in allFile1:
        for sub_sub_file in sub_file:
            list1.append(GetCutoffPath(sub_sub_file))

    for sub_file in allFile2:
        for sub_sub_file in sub_file:
            list2.append(GetCutoffPath(sub_sub_file))

    set1 = set(list1)
    set2 = set(list2)

    #获取新包删除了的文件
    delete_file = []
    delete_file = set1-set2

    temp_name = os.path.join(txt_path, 'delete_file.txt')
    fp1 = open(temp_name,'w')
    #加上旧包的前缀，输出这些文件在旧包的名称和路径
    prefix1 = GetPrefix(allFile1[0][0])
    for name in delete_file:       
        name1 = os.path.join(prefix1,name)
        print >>fp1,fullInfo1[name1][0]
        print >>fp1,name1
    fp1.close()


    #获取新包增加的文件
    add_file = []
    add_file = set2- set1

    temp_name = os.path.join(txt_path, 'add_file.txt')
    fp2 = open(temp_name,'w')
    #加上新包的前缀，输出这些文件在新包的名称和路径
    prefix2 = GetPrefix(allFile2[0][0])
    for name in add_file:
        name2 = os.path.join(prefix2,name)
        print >>fp2,fullInfo2[name2][0]
        print >>fp2,name2
    fp2.close()


    #获取版本号没提升的文件
    temp_name = os.path.join(txt_path, 'version_error.txt')
    fp3 = open(temp_name,'w')
    #获取新旧包共有的文件
    common_file = []
    common_file = set1 & set2
    for name in common_file:
        name1 = os.path.join(prefix1, name)
        name2 = os.path.join(prefix2, name)
        #如果文件MD5不同，但版本号相同，则输出
        if fullInfo1[name1][1] != fullInfo2[name2][1]:
            if fullInfo1[name1][2] == fullInfo2[name2][2]:
                print >>fp3,name
                print >>fp3,fullInfo1[name1][2]
                print >>fp3,fullInfo2[name2][2]
    fp3.close()
    


    

        
    
            
    
