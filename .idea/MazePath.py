#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: XF
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: MazePath.py
@time: 2020/2/15 15:21
"""
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from Queues import  ArrayQueue as AQ
# ----------------------------------------------------------------------------------------------------------------------
# 按照广度优先搜索最短路径
# 此时的队列类似于分叉树
# 注意广度优先意味着所有的可能性同时比赛，最先找到出口的就是最短路径
def Mazepath(xi, yi, xf, yf):
    Q = AQ()
    e = [xi, yi, -1]
    Q.EnQueue(e)
    Maze[xi, yi] = -1# 避免重复搜索
    # print("ok")
    while not Q.Is_Empty():
        e = Q.DeQueue()
        x, y, pre = e
        if x == xf & y == yf:
            Findmin(Q)
            return True
        for di in range(4):
            if di == 0:
                _x = x - 1
                _y = y
            if di == 1:
                _y = y + 1
                _x = x
            if di == 2:
                _x = x + 1
                _y = y
            if di == 3:
                _y = y - 1
                _x = x
            if Maze[_x, _y] == 0:
                e = [_x, _y, Q.First()]
                Q.EnQueue(e)
                Maze[_x, _y] = -1
                # print('ok')
    return False
# ----------------------------------------------------------------------------------------------------------------------
# 寻找最短路径
def Findmin(Q):
    k = Q.First()
    path = []
    while k != -1:
        j = k
        k = Q.data[j][2]
        path.append([Q.data[j][0], Q.data[j][1]])
        print("(%d,%d)<-"%(Q.data[j][0], Q.data[j][1]))
        # if n % 5 == 0:
        #     print("\n")
    # path = list(reversed(path))
    ShowPath(path)
# ----------------------------------------------------------------------------------------------------------------------
def ShowPath(path):
    Cyan = (0, 255, 255)
    Black = (0, 0, 0)
    Green = (0, 255, 0)
    Maze_map = np.zeros((10,10,3))
    for row in range(np.size(Maze, 0)):
        for col in range(np.size(Maze, 1)):
            if Maze[row, col] == 1:
                Maze_map[row, col, :] = Black
            if Maze[row, col] == 0:
                Maze_map[row, col, :] = Cyan
            if [row, col] in path:
                Maze_map[row, col, :] = Green
    Maze_map = Maze_map.astype(int)
    print(Maze_map)
    plt.imshow(Maze_map)
    plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# 求解M*N迷宫问题
if __name__ == "__main__":
    M = 8
    N = 8
    # 设置一个list，其中的元素的状态表示方块的状态
    # 0-》通路
    # 1-》障碍物
    # 此外，在迷宫再加一道围墙限制算法所路径的范围
    Maze = np.array([
                    [1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,1,0,0,0,1,0,1],
                    [1,0,0,1,0,0,0,1,0,1],
                    [1,0,0,0,0,1,1,0,0,1],
                    [1,0,1,1,1,0,0,0,0,1],
                    [1,0,0,0,1,0,0,0,0,1],
                    [1,0,1,0,0,0,1,0,0,1],
                    [1,0,1,1,1,0,1,1,0,1],
                    [1,1,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1],
                     ])
    # 入口在[1,1]或者[1][1]
    # 出口在[8,8]或者[8][8]
    Mazepath(1, 1, 8, 8)
# ---------------------------------------------------------------------------------- 



# ---------------------------------------------------------------------------------- 



# ---------------------------------------------------------------------------------- 