# -*- coding: gbk -*-
# @Time    : 2018-11-07 18:02
# @Author  : Edward
# @File    : ipytopdf.py
# @Software: PyCharm
import sys
import os
import subprocess
import pdfkit
from mergepdf import *
file_dir =os.getcwd()
#ipynb转pdf
for root, dirs, files in os.walk(file_dir):
    #print(root) #当前目录路径
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    L = []
    for file in files:
        if os.path.splitext(file)[1] == '.ipynb':
            L.append(os.path.join(root, file))
            #print(file)
            command = 'jupyter nbconvert --to html ' + file
            subprocess.call(command, shell=True)
            temp_html = file[0:file.rfind('.')] + '.html'
            output_file = file[0:file.rfind('.')] + '.pdf'
            #print(temp_html,output_file)
            command_to=('wkhtmltopdf '+temp_html+' '+output_file)
            subprocess.call(command_to,shell=True )
            command_rm='del '+temp_html
            #print(command_rm)
            subprocess.call(command_rm, shell=True)
#合并pdf文档
v_path=os.path._getfinalpathname(file_dir)
file_name=v_path[v_path.rfind('\\')+1:]
out = file_name+".pdf"
MergePDF(file_dir, out)