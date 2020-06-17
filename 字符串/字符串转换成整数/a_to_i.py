# -*- coding: utf-8 -*-
# @Time : 2020/6/17 10:56
# @Author : ccs
import math
import re

INT_MAX = math.pow(2,31) - 1
INT_MIN = -math.pow(2,31)

def num_cal(x):
    int_rst = ''
    tmp = re.match(r'^\d+', x)
    if re.match(r'^\d+', x):
        int_rst= tmp.group(0)
    # list_int_rst = list(int_rst)
    # rst = 0
    # for val in list_int_rst:
    #     # rst = rst + val*(10^(idx))  #常规写法---逆序判断
    #     rst = rst * 10 + int(val)   #正序判断
    return int(int_rst) #报错：invalid literal for int() with base 10 --非纯数字组成的字符串强转为整型会报错：ValueError: invalid literal for int() with base 10



def a_to_i(x):
    if not x:
        return 0
    if x.startswith("+") or x[0].isdigit():#出现错误；
        sign =  1
        return min(sign*num_cal(x.replace("+","")),INT_MAX)
    elif x.startswith("-"):
        sign = -1
        return max(sign*num_cal(x.replace("-","")),INT_MIN)
    else:
        return 0

#invalid
    # if int_rst:
        #     int_rst = int(int_rst)
        #     if int_rst > INT_MAX: #这样写可能不对，因为本身会溢出，因此需要在即将溢出之前判断。
        #         return INT_MAX
        #     elif int_rst < INT_MIN:
        #         return INT_MIN
        #     else:
        #         return int_rst
#了解溢出的概念，溢出后，值是原样输出，还是会变成其他什么数；判断溢出的条件；
"""
"+-2"
+1
+
-
"   +0 123"   #每一种情况都要写一个if else,但如果用状态机的方式去实现，针对每个位置对应状态对应的取的值进行考虑，就行；
"  +00  123"

"+-2"  

总结测试用例，各个位置都有可能是:+,-,nums,以及其他；
"""

import math
import re

INT_MAX = int(math.pow(2, 31) - 1)
INT_MIN = int(-math.pow(2, 31))


class Solution:

    def num_cal(self, x):
        if not x:
            return 0
        int_rst = ''
        tmp = re.match(r'^\d+', x)
        if re.match(r'^\d+', x):
            int_rst = tmp.group(0)

        # list_int_rst = list(int_rst)
        # rst = 0
        # for val in list_int_rst:
        #     # rst = rst + val*(10^(idx))  #常规写法---逆序判断
        #     rst = rst * 10 + int(val)   #正序判断
        else:
            int_rst = 0
        return int(int_rst)

    def myAtoi(self, x):
        x = x.replace(" ", "")
        if not x:
            return 0
        if x.startswith("+") or x[0].isdigit():
            sign = 1
            return min(sign * self.num_cal(x.replace("+", "")), INT_MAX)
        elif x.startswith("-"):
            sign = -1
            return max(sign * self.num_cal(x.replace("-", "")), INT_MIN)
        else:
            return 0


"""
#对比官方解法,自己的解法存在的一些缺陷：
（1）对位置有较严格的取值控制，默认第一个为符号位，第二个为数值位；
但其实有可能前面有很多其他的取值情况，如果每一个情况需要单独写条件来判断，很臃肿；
    例如：输入为"  +","  -"," 1"
（2）基于当前位假设if...else判断完毕，它的下一位还要再写同样的if..else...判断，很累赘，可以利用一个状态映射矩阵，对此做同样的逻辑映射处理；
    例如："++123",输出应当为0;
    
（3）我的逻辑，倾向于一个判断一个返回，不够通用；最好的做法是，一个判断情况，对应中间状态值更新，结果仍然统一用中间状态值去计算，这样可以避免臃肿；
    例如："++123",直接写输出应当为0;这样很不好，可以判断当前位置字符，对应的数值是多少，一直遍历完，有些符号，遍历过程中，数值不会发生变化，有些符号，
    遍历过程中数值会发生变化。
    
    
官方解法的优点：
（1）已经有了一个符号位后，后续的状态如果再遇到符号位，其映射为end;


"""

if __name__ == '__main__':
    so = Solution()
    a = so.myAtoi("   +0 123")
    print("a",a)
    # x = "-42"
    # r = a_to_i(x)
    # print("rst is",a_to_i(x))
    #
    # x = "-42"
    # print("rst is", a_to_i(x))
    #
    # x = "4193 with words"
    # r = a_to_i(x)
    #
    # print("rst is", a_to_i(x))
    #
    # x = "words and 987"
    # print("rst is", a_to_i(x))
    #
    # x = "-91283472332"
    # print("rst is", a_to_i(x))