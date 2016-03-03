# CompareTwoFolders
Compare the  versions, MD5 and paths between two Folders.
安装一个应用程序，生成安装目录A；安装这个应用程序的新版本，生成安装目录B；现在需要比较这两个安装目录的文件，是否有增加或减少；相同的文件，如果有改动，那么版本号应该要提升，没有的话，应该列出提示。

此python 程序实现该功能。
1.0 版，实现了print输出PE文件的比较情况。

1.1版本，进行了以下更改：
1)修复bug:对于以.dll和.exe结尾的文件夹，把它们当做成了文件
2)对于不能获取FileVersion的文件，改为获取ProductVersion

1.2版本，在1.1的基础上进行了以下修改：
1）增加对于PE文件：.ext，.sys，.tpi的对比
2）输出对比结果到txt文件

