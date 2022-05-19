
from array import array
import os
import re
from unittest.mock import patch
import numpy as np

def read_list():
    filename = input("输入文件名(与程序保持在相同目录下):")
    path = os.path.dirname(__file__) + "/" + filename
    f = open(path, 'r', encoding='utf-8')
    src_list = f.readlines()
    real_list = []
    for i in src_list:
        i = list(i[:-1].split("\t"))
        real_list.append(i)
    f.close()
    return real_list
def get_only_element(lst):
    if len(lst) == 0:
        return []
    lst = np.array(lst)
    result = np.array([lst[0]])
    # print(lst.shape,result.shape)
    # print_lst(lst[0:,0:2])
    for item in lst[1:,:]:
        if item[0:2] not in result[0:,0:2] and item[-2::-1] not in result[0:,0:2]:
            result = np.row_stack((result,item))
    # print(result)
    return result

def write_list(lst):
    f = open("./result","w")
    for item in lst:
        f.write(str(item)+"\n")
    f.close()

def print_lst(lst):
    for item in lst:
        print(item)
if __name__=='__main__':
    lst = read_list()
    lst = get_only_element(lst)
    write_list(lst)
