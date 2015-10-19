#如何运行
1. 如果你没有装过python，请记得安装python。推荐是python2.7【下载地址：https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi】
2. 安装pip： 教程：https://pip.pypa.io/en/stable/installing/
3. 安装Django： 方法：`pip install django` 这个pip是第二步安装的.如果第二步不成功，这个步骤就不会成功了。
4. 安装bootstrap3 方法：`pip install django-bootstrap3` [后期会删掉这个鬼东西]
4. 如果第三步完成了，下载本程序源码到一个没有汉字的目录中，比如 F:\notepad
5. 用`git clone https://github.com/pjkui/notepad.git` 或者直接打开https://github.com/pjkui/notepad/archive/master.zip 保存到你的文件夹中，一定不能有中文目录。
6. 然后解压文件，进入notepad文件夹，然后在有manage.py的目录下，运行`python manager runserver`
7. OK了 新建笔记 http://127.0.0.1:8000/create
8. 查看笔记 http://127.0.0.1:8000/view/?id=7 
    http://127.0.0.1:8000/view/?id=8
    http://127.0.0.1:8000/view/?id=9
如果新建一个笔记那么，会自动跳转到查看笔记的页面。
2015年10月18日23:38:54 到这个时间点 ，只有这两大功能。

#国内访问google的方法：【小福利】
https://github.com/racaljk/hosts/blob/master/hosts
用这个文件更新：C:\Windows\System32\drivers\etc\host 文件的内容后就可以访问google了。有时候还可以访问YouTube。

#2015年10月20日00:21:53
1. 如何修改，编辑之前的笔记 √
2. 如何删除发表的笔记 √
3. index如何编写，怎么用Django实现分页。√

#下次直播：
1. 用户注册
2. 用户管理
3. 用户角色及授权


#本源代码技术交流QQ群：196154886

# notepad
Quinn Pan's Notepad 
Just personal project to study Django.
2015-10-14 10:07:54
======================================
2015-10-15 16:34:59
#Naming rule
in the models:
all the variable should avoid use underline. use hump nomenclature.

=====
2015-10-17 11:55:50
#TODO
##internationalization:
1. support multiple language

## data export
1. export to PDF
2. export to DOC/DOCX
3. export to PNG/JPG/JPEG/BMP
4. export to c/c++/java/python/js

## program online[maybe]
1. support python
2. support php
3. support java 

##add Tag
let every note hava it owner class/tags

[TODO] add a button to switch menu show or not 

#Tools
1. IDE sublime3
2. python 2.7
3. pip ： install some app,framework
4. django : 安装方法： pip install django  

#todo
美化404页面