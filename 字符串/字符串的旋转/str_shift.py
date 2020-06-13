# -*- coding: utf-8 -*-
# @Time : 2020/6/13 9:17
# @Author : ccs
"""
题目描述
给定一个字符串，要求将字符串前面的若干个字符移到字符串的尾部。
例如，将字符串" abcdef"的前3个字符a、b和c移到字符串的尾部，那么原字符串将变成defabc"。请写一个函数实现此功能。
"""


def reverse_string(string, start, end):
    while start < end:
        tmp = string[start]
        string[start] = string[end]
        string[end] = tmp
        start = start + 1
        end = end - 1
    print(('').join(string))
    return string


def left_rotate_string(string, n, m):
    reverse_string(string, 0, m - 1)
    reverse_string(string, m, n - 1)
    reverse_string(string, 0, n - 1)


if __name__ == '__main__':
    # 注意字符串不能改写，因此需要先转换成列表再赋值；
    input_string = list('abcdef')  # 输出为defabc
    left_rotate_string(input_string, 6, 3)  # 6代表总的字符串长度，3代表需要迭代单元反转的最小长度

    input_string = list('I am a student.')  # 输出为 "student. a am I"
    left_rotate_string(input_string, len(input_string), len('student.')-1)
