# -*- coding: utf-8 -*-
# @Time : 2020/6/13 10:26
# @Author : ccs
"""
题目描述输入一个字符串，打印出该字符串中字符的所有排列。
例如，输入字符串"abe"，则输出由字符a'、b、c所能排列出来的所有字符串
"abc”、"acb"、"bac"、"bca"、"cab"和"cba"
"""

"""
解法一：递归实现从字符串中选出一个字符作为排列的第一个字符，然后对剩余的字符进行全排列。如此递归处理，从而得到所有字符的全排列。以对字符串"abc"进行全排列为例，可以按下述步骤执行。
·将a固定在第一位，求后面bc的排列，得到："abc"和"acb"。
将b固定在第一位，求后面ac的排列，得到："bac"和"bca"。
将c固定在第一位，求后面ba的排列，得到："cba"和"cab"。


把s[0]固定在位置0上，[1,n-1]位置的数字全排（递归）
把s[1]固定在位置0上（把s[1]和s[0]交换），[1,n-1]位置的数字全排（递归）
……
如果第i个数字在前面出现过，则跳过
……
把s[n-1]固定在位置0上（把s[n-1]和s[0]交换），[1,n-1]位置的数字全排（递归）



用sketch画图
"""
from copy import deepcopy

def is_duplicate(li,n,t):
    while n < t:
        if li[n] == li[t]:
            return True
        n = n + 1
        return False

def swap(li,i,j):
    if i == j:
        return None
    temp = li[j]
    li[j] = li[i]
    li[i] = temp

def permutation(li,size,n,result):
    """
     [n,size]位置的数字全排
    :param li:字符串数组
    :param size: 字符串长度
    :param n: 要交换的位置
    :param result: 保留结果
    """
    if n == size - 1:
        result.append(deepcopy(li)) # 分别把(size-n)个数字固定到位置n #此处深拷贝li,li变化时，result不会变化；
        return None
    for i in list(range(n,size)): ## 如果位置n出现过数字li[i]，跳过
        if is_duplicate(li,n,i):
            continue  #如果有重复的，就跳过；否则，执行第i个值和起始n的替换；
        swap(li,i,n) ## 把s[n]和s[i]交换，把s[i]固定到位置n
        permutation(li,size,n+1,result) # [n+1,size-1]位置的数字全排  #执行size和   #递归执行等到return的时候，就运行下一行；
        swap(li,i,n)# 把s[n]和s[i]交换回来

def Permutation(ss):
    print("SS is ",ss)
    list = []
    if len(ss) <= 1:
        return ss
    for i in range(len(ss)):
        for j in map(lambda x: ss[i]+x, Permutation(ss[:i]+ss[i+1:])):
            if j not in list:
                print("J is ",j)
                print("list is ",list)
                print("***********************")

                list.append(j)
    return list


if __name__ == '__main__':
    li = [1, 2, 2, 3] #可变对象
    size = len(li)
    n = 0
    result = []
    # permutation(li, size, n, result)
    # for i in result:
    #     print(i)

    rst = Permutation("abc")
    print("rst is ",rst)

#代码参考：https://blog.csdn.net/weixin_42018258/article/details/80683826

"""
深拷贝和浅拷贝的区别：

因此，在下次我们遇到这类问题时，我们说出以下关键点，基本就很稳了

由于 Python 内部引用计数的特性，对于不可变对象，浅拷贝和深拷贝的作用是一致的，就相当于复制了一份副本，原对象内部的不可变对象的改变，不会影响到复制对象

浅拷贝的拷贝。其实是拷贝了原始元素的引用（内存地址），所以当拷贝可变对象时，原对象内可变对象的对应元素的改变，会在复制对象的对应元素上，有所体现

深拷贝在遇到可变对象时，又在内部做了新建了一个副本。所以，不管它内部的元素如何变化，都不会影响到原来副本的可变对象


"""