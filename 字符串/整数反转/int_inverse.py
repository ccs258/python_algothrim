# -*- coding: utf-8 -*-
# @Time : 2020/6/17 19:57
# @Author : ccs
"""

"""

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


#错误版本1
class SolutionErr:
    """
    不用默认参数，在里面实现的话会报错；
    """
    def reverse_sub(self, x: int) -> int:
        m = x // 10
        n = x % 10
        if m == 0:
            return n
        else:
            return self.reverse_sub(n)

    def reverse_sub_2(self, x, ans):
        print("x is ", x)
        print("self.reverse(x) is ", self.reverse(x))
        ans = ans * 10 + self.reverse(x)  #怎么将这个地方的ans=0,在递归中实现；第一次是0，后面都是ans;感觉这个地方，ans需要从外面传入；可以加默认参数；
        x = x // 10
        y = x % 10
        print("ans is ", ans)
        print("x,y is ", x, y)

        if y == 0:
            return ans
        else:
            return self.reverse_sub_2(x, ans)

    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
        x = x * sign
        return min(sign * self.reverse_sub_2(x, 0), INT_MAX) if sign == 1 else max(sign * self.reverse_sub_2(x, 0), INT_MIN)



#错误版本2
# class SolutionErr2:
#     """
#     未考虑溢出值处理，溢出值后取值为0
#     """
#     def reverse_sub(self, x: int) -> int:
#         m = x // 10
#         n = x % 10
#         if m == 0:
#             return n
#         else:
#             return self.reverse_sub(n)
#
#     def reverse(self,x,ans=0):
#         sign =  1
#         if x < 0:
#             sign = -1
#         x = x * sign
#         print("self.reverse_sub(x) is ",self.reverse_sub(x))
#         ans  =  ans * 10 + self.reverse_sub(x)
#         print("ans is ",ans)
#         x = x // 10
#         y = x % 10
#         print("x,y is ",x,y)
#
#         if y == 0 and x < 10:
#             return sign*ans
#         else:
#             return sign*self.reverse(x,ans)

###最终正确的版本
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31
class Solution:
    """
    思路：python用两阶段递归实现，第一个递归实现按反取位，第二个递归实现对取出位数据的拼接；
    （1）reverse_sub(x)递归函数:实现了取出每个输入x的末位；递归的返回为自然值(非递归值，即return n)是当且仅当遍历到数据的最低位时（x//10 == 0,即m==0,此时数据只有一位）；
    （2）reverse(x,ans=0)递归函数:实现了第一次输入不改变输入值，后面每次输入为去除右边最低位保留左边高位的数字(通过x//10实现)；递归的返回为自然值(非递归值，
    即return sign*ans)的条件，是当且仅当输入只有一位数据时（x//10 == 0,即m==0,此时数据只有一位）；
    （3）需要注意对溢出值的处理，如果返回值出现溢出（正溢出或反溢出，即if sign*self.reverse(x,ans)>INT_MAX or sign*self.reverse(x,ans) < INT_MIN ）那就返回0，否则返回结果本身；

    执行用时 : 212 ms, 在所有 Python3 提交中击败了6.51%的用户
    内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.67%的用户

    """
    def reverse_sub(self, x: int) -> int:
        m = x // 10
        n = x % 10
        if m == 0:
            return n
        else:
            return self.reverse_sub(n)

    def reverse(self,x,ans=0):
        sign =  1
        if x < 0:
            sign = -1
        x = x * sign
        ans  =  ans * 10 + self.reverse_sub(x)
        x = x // 10
        if x == 0 :
            return sign*ans
        else:
            return 0 if sign*self.reverse(x,ans)>INT_MAX or sign*self.reverse(x,ans) < INT_MIN else sign*self.reverse(x,ans)


if __name__ == '__main__':
    so = Solution()
    rst = so.reverse(2**32)

    print(rst)
"""

执行用时 :
212 ms
, 在所有 Python3 提交中击败了
6.51%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
6.67%
的用户

 

"""

