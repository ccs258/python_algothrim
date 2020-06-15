# -*- coding: utf-8 -*-
# @Time : 2020/6/14 16:39
# @Author : ccs
"""


"""

def mutil_sum(data,length,sum,flag,flag_size):
    if (length <= 0 | sum <= 0 ):
        return None
    if (sum == data[length-1]):
        i = 0
        while(i<flag_size):
            if flag[i] == 1:
                print("%d+"%data[i])
            i = i+1
        print("%d\n"%data[length-1])
    flag[length-1] = 1
    mutil_sum(data,length-1,sum-data[length-1],flag,flag_size)
    flag[length-1] = 0
    mutil_sum(data,length-1,sum,flag,flag_size)
if __name__ == '__main__':
    data = [1, 2, 3, 4, 6, 4, 5, 7, 1, 3, 4, 0, 2]
    length = len(data)
    sum = 6
    flag = [0] * length
    flag_size = len(flag)
    mutil_sum(data, length, sum, flag, flag_size)