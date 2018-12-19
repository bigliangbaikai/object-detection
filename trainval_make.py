# -*- coding:utf-8 -*-

# @Time    : 2018-12-14 10:56

# @Author  : Swing


with open('trainval.txt', 'w') as f:
    for i in range(155):
        num = str(i).zfill(4)
        f.write(num + "\n")

