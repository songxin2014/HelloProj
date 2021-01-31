# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:RichardSong time:2021/01/25

def square(num):

    for i in range(1, num+1):
        print("---A---")
        yield
        print("---B---")


for i in square(5):
    print(i)


if __name__ == '__main__':
    print("Hello again!")





