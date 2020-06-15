# -*- coding: utf-8 -*-
# @Time : 2020/6/13 14:26
# @Author : ccs
"""
题目描述:
给定一个字符串，如何判断这个字符串是否是回文串？

分析与解法:
所谓回文串，是指正读和反读都一样的字符串，如 madam、我爱我。那么，如何通过程序判断一个字符串是否是回文串呢？

"""

"""
解法一：两头往中间扫

给定一个字符串，定义两个分别指向字符串的头和尾的指针，然后让这两个指针都往字符串的中间扫描，扫描的过程中，如果头和尾所指的字符至始至终都一样，则该字符串为回文串。
"""
def isPalindrome(string):
    #这个实现直白且效率不错，时间复杂度为O（n），空间复杂度为O（1）。

    if not string:
        return False
    left = 0
    right = len(string) - 1
    while (left < right):
        if string[left] != string[right]:
            return False
        left = left + 1
        right = right - 1
    return True




if __name__ == '__main__':
    string = "madam"
    rst = isPalindrome(string)
    print("rst is ",rst)

    string = "madamffff"
    rst = isPalindrome(string)
    print("rst is ", rst)