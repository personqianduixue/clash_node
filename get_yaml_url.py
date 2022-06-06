import os
import shutil
from tkinter import Tk
import time
import pyperclip

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileCreateTime(filePath):
    # '''获取文件的创建时间'''
    # filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath,mode = 'timestamp'):
    # '''获取文件的修改时间'''
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    if mode == 'timestamp':
        return t
    else:
        return TimeStampToTime(t)


def get_FileAccessTime(filePath):
    # '''获取文件的访问时间'''
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


def get_FileSize(filePath):
    # '''获取文件的大小,结果保留两位小数，单位为MB'''
    # filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def get_file_all_path(path, filetype, isjoin=True):
    """
    获取当前文件夹下的以.xlsx结尾的文件，不包括子文件夹
    :param path: 路径
    :param filetype:文件类型，如：'.xlsx'
    :return:文件全路径名 列表
    """
    files = []
    for file in os.listdir(path):
        if file.endswith(filetype):
            if isjoin:
                temp_path = os.path.join(path, file)
            else:
                temp_path = file
            files.append(temp_path)
    return files


def writelist(file, list_):
    with open(file, 'w') as f:
        f.write(','.join(list_))


def readlist(file):
    with open(file, 'r') as f:
        list_ = f.readline().split(',')
    return list_


def removelistfromlist(biglist, smalllist):
    for x in smalllist:
        if x in biglist:
            biglist.remove(x)


def addToClipboard(string):
    r = Tk()
    r.withdraw()
    r.clipboard_append(string)
    r.update()
    r.destroy()


def getClipboard():
    r = Tk()
    r.withdraw()
    tmp = r.clipboard_get()
    r.destroy()
    return tmp


# dir = './'
# old_filelist = readlist('old_list.txt')
# new_filelist = get_file_all_path(dir, 'yaml', False)
# writelist('old_list.txt', new_filelist)
# removelistfromlist(new_filelist, old_filelist)
# push_filelist = new_filelist
#
# url1 = 'https://cdn.staticaly.com/gh/personqianduixue/clash_node/master/'  # 20220606.yaml
# url2 = 'https://fastly.jsdelivr.net/gh/personqianduixue/clash_node@master/'
# for file in push_filelist:
#     url = url1 + file
#     addToClipboard(url)

url1 = 'https://cdn.staticaly.com/gh/personqianduixue/clash_node/master/'  # 20220606.yaml
url2 = 'https://fastly.jsdelivr.net/gh/personqianduixue/clash_node@master/'
dir = './'
old_file = 'old_time.txt'
if not os.path.exists(dir+old_file):
    old_time = 0.0
else:
    with open(dir+old_file,'r') as f:
        old_time = f.read()
        if old_time:
            old_time = float(old_time)
        else:
            old_time = 0.0
filelist = get_file_all_path(dir, 'yaml', False)
pushlist = []
new_time = 0
for file in filelist:
    filetime = get_FileModifyTime(file,mode = 'timestamp')
    if filetime > new_time:
        new_time = filetime
    if filetime > old_time:
        url = url1 + file
        print(url)
        # addToClipboard(url)
        pyperclip.copy(url)

with open(dir + old_file, 'w') as f:
    f.write(str(new_time))
