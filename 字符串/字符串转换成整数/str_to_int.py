# -*- coding: utf-8 -*-
# @Time : 2020/6/13 14:01
# @Author : ccs
"""
输入一个由数字组成的字符串，请把它转换成整数并输出。例如，输入字符串
"123"，输出整数123。
函数原型为 int str toInt（ const char*str），请实现字符串转换成整数的功能，不能使用库函数aoi

"""

"""
分析与解法本题实际上考查的是把字符串转换成整数的问题，或者说要你自行实现atoi函数。那么，如何把由数字组成的字符串正确地转换成整数呢？
下面以"123”为例，说明这一转换过程。
（1）当扫描到字符串的第一个字符时，因为这是第一位，所以得到整数1。
（2）当扫描到第二个字符2时，因为之前已有一个1（相当于10），所以得到的整数为1×10+2=12。
（3）继续扫描到第三个字符3，因为3的前面已经有了12（相当于120），所以最终得到的数为12×10+3=123。
因此，此题的基本思路便是：从左至右扫描字符串中的每个字符，把之前扫描得到的数字乘以10，再加上当前字符表示的数字。

但是上述代码忽略了以下几个细节：
最好判断一下输入是否为空。
如果字符串的第一个字符是号，最终得到的整数必为负整数。
输入的字符串中不能含有不是数字的字符输入的字符串不能太长，否则转换成整数后可能会导致整数溢出。
上述问题中的前三个问题都比较好处理，但最后一个溢出问题比较麻烦，所以重点看一下这个问题。
一般来说，当发生溢出时，取最大或最小的int型值，即大于正整数能表示的范围时返回 MAX INT（2147483647），小于负整数能表示的范围时返回 MIN INT
（-2147483648）。


"""
MAX_INT = 2147483647
MIN_INT = -2147483648

def str_to_int(string):
    n = 0
    string = string.replace(' ','') #去除空格
    if string == '0' or not string: #判断是否为空及是否为0
        return 0

    #考虑正负溢出
    for i in string:
        if string[0] == '+' & n > MAX_INT - n * 10: #正溢出
            n = MAX_INT
            break
        elif string[0] == '-' & (n-1 >  MAX_INT - n * 10) :#负溢出
            n = MIN_INT
            break
        n = n * 10 + int(i)



    return n
if __name__ == '__main__':
    rst = str_to_int("123")

    rst = str_to_int("32123")

    print("rst is ",rst)