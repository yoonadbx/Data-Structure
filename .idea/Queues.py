#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: XF
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: Queues.py
@time: 2020/2/14 21:40
"""
class ArrayQueue:
    Default_Capacity = 10

    def __init__(self):
        """
        Create a empty queue.
        """
        self.data = [[]]*ArrayQueue.Default_Capacity
        self.__size = 0
        self.__front = -1

    def __len__(self):

        return self.__size

    def Is_Empty(self):
        return self.__size == 0

    def First(self):
        # if self.Is_Empty():
        #     raise Empty('Queue is empty')
        return self.__front

    def DeQueue(self):
        if self.Is_Empty():
            raise Empty('Queue is empty')
        self.__front = (self.__front + 1) % len(self.data)
        self.__size -= 1
        p = self.data[self.__front]
        # self.data[self.__front] = []
        # if self.Is_Empty():
        #     self.__front = 0
        # else:
        return p

    def EnQueue(self, e):
        avail = (self.__front + self.__size + 1) # % len(self.data)
        if self.__size == len(self.data) or avail>= len(self.data) :
            self.__ReSize(2*len(self.data))
        # avail = (self.__front + self.__size + 1) % len(self.data)
        self.data[avail] = e
        self.__size += 1
        return True

    def __ReSize(self, length):
        old = self.data
        self.data = [[]]*length
        # walk = self.__front
        # for k in range(len(old)):
        #     self.data[k] = old[walk]
        #     walk = (walk + 1) % len(old)
        # self.__front = -1
        self.data[:len(old)] = old
        return True
