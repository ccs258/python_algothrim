# -*- coding: utf-8 -*-
# @Time : 2020/6/20 11:04
# @Author : ccs
"""
给定一个整数N，输出如下顺序的矩阵。

示例：N=3

输出：

[[1,2,3],

[8,9,4],

[7,6,5]]



N=4

[[1,2,3,4],
[12,13,14,5],
[11,16,15,6],
[10,9,8,7]]


N=5

[[1,2,3,4,5],
[16,17,18,19,6],
[15,14,25,20,7],
[14,23,22,21,8],
[13,12,11,10,9]]



#python 二维列表（数组）赋值问题
https://blog.csdn.net/zzc15806/article/details/82629406
"""
# a = [[]] * 5
# for i in range(n):
#     a[i].append(0)


"""
思路：
观察规律：
先沿着行的方向走，走到最右边；
再沿着列的方向走，走到最下边；
再沿着行的反方向走，走到最左边；
再沿着列的反方向走，走到最上边；
.......

从上可以看出，
首先，观察总体的结束次数：
对于输入的n,上述每个步骤对应一行或者一列；由已知n，它的行列总数一定是确定的；观察规律可得到，n与这种螺旋填数的直线数量关系是2n-1;可以做终止条件；

其次，看每一次内部的参数与操作：
对于行而言：列遍历第一次是j++,第二次是j--,这个可以用方向参数来确定，下一次的当前方向取反；
对于列而言：行遍历第一次是i++,第二次是i--，同样用方向参数来确定，下一次的当前方向取反；
另外，
对于行而言：列遍历次数的第一次是n-1,第二次是n,因此需要定义列遍历的变量，可在函数内部定义临时变量用于循环；
对于列而言：行遍历次数的第一次是n-1,第二次是n,因此需要定义行遍历的变量，可在函数内部定义临时变量用于循环；


初始条件：由于第一次a[0][0]=0,需要在行处单独加if处理；


总结：可以看出，对于实现某一个算法，先要观察规律；确定是用循环还是递归，以及相应的终止条件，另外，要清楚需要定义多少个变量；对每个变量当前值与下一次值的关系表示；
对于循环实现，可以将函数输入进行循环赋值计算，更新函数输入参数，作为结果进行输出，下一次基于此结果再进行计算；


对于一个数组赋值，出现整个列赋值的情况：参考https://blog.csdn.net/zzc15806/article/details/82629406
这是因为 [[0]*5]*5 表示的是指向 [0]*5 这个列表的引用，所以当你修改某一个值时，整个列表都会被改变。
换一种初始化方式可以解决这个问题；
arr = [[0]*5 for _ in range(5)]




"""


def cal_x(all_x,i,j,flag_x):
    tmp = 0
    while ( tmp < all_x + 1):
        if a[i][j] == 0:
            a[i][j] = 1
        if (j +flag_x < n  and flag_x == 1) or (j +flag_x > -1 and flag_x == -1):
            print("i,j +flag_x is ",i,j +flag_x)
            a[i][j +flag_x] = a[i][j] + 1
            j = j +flag_x
        tmp = tmp + 1
    flag_x = -flag_x
    all_x = all_x - 1
    return all_x,i,j,flag_x

def cal_y(all_y,i,j,flag_y):
    tmp = 0
    while (tmp < all_y):
        a[i+flag_y][j] = a[i][j] + 1
        i = i + flag_y
        tmp = tmp + 1
    flag_y = -flag_y
    all_y = all_y -1
    return all_y,i,j,flag_y

def cal_mat_4(n):
    i = 0
    j = 0

    flag_x = 1
    flag_y = 1

    all_x = n
    all_y  = n
    for idx in range(2*n -1):
        if idx ==  0:
            all_x,i,j,flag_x = cal_x(all_x-1,i,j,flag_x)
            all_y,i,j,flag_y = cal_y(all_y-1, i,j, flag_y)
        else:
            all_x, i, j, flag_x = cal_x(all_x, i, j, flag_x)
            all_y, i, j, flag_y = cal_y(all_y, i, j, flag_y)
    print("a is ",a)

if __name__ == '__main__':
    n = 3
    a = [[0] * n for i in range(n)]

    cal_mat_4(n)

