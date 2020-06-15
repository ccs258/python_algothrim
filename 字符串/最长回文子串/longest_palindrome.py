# -*- coding: utf-8 -*-
# @Time : 2020/6/13 14:44
# @Author : ccs
def longest_palindrome(string):
    if not string:
        return 0
    max = 0
    j = 0
    for i in range(0,len(string)):
        if len(string) % 2 != 0:
            print("i+j  is ",i+j )
            print("i-j  is ",i-j )
            print("i - j >= 0 & i+j < len(string)-1 is ",(i - j >= 0) & (i+j < len(string)-1))
            while ((i - j >= 0) & (i+j < len(string)-1)):
                if string[i-j] != string[i+j]:
                    break
                c = j*2 + 1
                j = j + 1
        else:
            while((i - j >= 0) & (i+j+1 < len(string)-1)):
                if string[i-j] != string[i+j+1]:
                    break
                c = j * 2 + 2
                j = j + 1
        if c > max:
            max = c
    return max
if __name__ == '__main__':
    string='madam'
    rst = longest_palindrome(string)
    print("rst is ",rst)

    string = 'madamhhah'
    rst = longest_palindrome(string)
    print("rst is ", rst)




    """
    
    思路：代码外层循环表示遍历回文子串中心为i的位置，内层的两个for循环分别处理的是以i为子串中心，回文子串长度为奇数和偶数的两种情况。简而言之，整个代码遍历中心位置i并以其为中心扩展，试图找出最长的回文子串。
    
    
    break能跳出某一重循环（该重循环的本次及剩余次数都不再执行），但并不能跳出该重循环的其他外重循环。
    """




