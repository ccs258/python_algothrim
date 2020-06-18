# -*- coding: utf-8 -*-
# @Time : 2020/6/18 20:36
# @Author : ccs
import time
from typing import List


class Solution_1:
    def longesetCommonPrefix(self,strs):
        """
        按行扫描，每个列表元素进行逐次比较
        """
        if not strs:
            return ""

        prefix,count = strs[0],len(strs)
        for i in range(1,count):  #时间复杂度为n个元素
            prefix = self.lcp(prefix,strs[i]) #prefix为每次两两的公共前缀；第一次为两个字符的公共前缀；第二次为前缀与字符元素的前缀；
            if not prefix:
                break
        return prefix

    def lcp(self,str1,str2):
        length,index = min(len(str1),len(str2)),0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

class Solution_2():
    """
    按列进行比较：时间复杂度为m*n;
    空间复杂度：O(1)。使用的额外空间复杂度为常数。
    """
    def longesetCommonPrefix(self,strs:List[str]):
        if not strs:
            return ""
        length,count = len(strs[0]),len(strs)
        for i in range(length): #时间复杂度，平均每个字符串的长度m
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1,count)): #时间复杂度为列表共有多少个元素n
                return strs[0][:i]
        return strs[0]

class Solution_3():
    """
    分治法：
    复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 是字符串数组中的字符串的平均长度，nn 是字符串的数量。时间复杂度的递推式是 T(n)=2 \cdot T(\frac{n}{2})+O(m)T(n)=2⋅T(
\n)+O(m)，通过计算可得 T(n)=O(mn)T(n)=O(mn)。

空间复杂度：O(m \log n)O(mlogn)，其中 mm 是字符串数组中的字符串的平均长度，nn 是字符串的数量。空间复杂度主要取决于递归调用的层数，层数最大为 \log nlogn，每层需要 mm 的空间存储返回结果。


    """
    def longesetCommonPrefix(self,strs:List[str]):
        def lcp(start,end):
            if start == end:
                return strs[start]
            mid = (start+end)/2
            lcpLeft,lcpRight = lcp(start,mid),lcp(mid+1,end)
            minLength = min(len(lcpLeft),len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]
        return "" if not strs else lcp(0,len(strs)-1)




if __name__ == '__main__':
    time_start = time.time()
    for i in range(0,1000000):
        if "a"*100000 == "b"*100000:
            print("haha")
    time_end = time.time()
    print("time costs",time_end-time_start)

    """
    在1000000次循环里面：
    大小为100000的单个字符串比较耗时：
    time costs 12.34592056274414
    大小为1的单个字符比较耗时：
    time costs 0.054911136627197266
    
    """
