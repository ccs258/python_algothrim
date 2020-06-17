# -*- coding: utf-8 -*-
# @Time : 2020/6/17 14:15
# @Author : ccs
"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
 

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31
class Automation(object):
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table= {
            'start':['start','sign','nums','end'],
            'sign':['end','nums','end','end'],
            'nums':['end','end','nums','end'],
            'end':['end','end','end','end']
        } #状态机，初始状态确定，初始状态机转移规则确定，下一个状态的转移映射（利用同一个转移规则）也会对应确定
    def get_col(self,c):
        if c.isspace():
            return 0 #如果start位置为空字符串，则该位的更新状态仍为start状态(对应索引位置为0)
        if c == '+' or c == '-':
            return 1#如果start位置为符号字符串，则该位的更新状态仍为sign状态(对应索引位置为1)
        if c.isdigit():
            return 2 ##如果start位置为数值，则该位的更新状态仍为num状态(对应索引位置为2)
        return 3 #否则，为end状态; step2:这一步一确定，就可以写完接下来所有的其他状态的取值了；比如sign状态，其取值会返回1，在索引为1处,更新状态为nums


    def get(self,c):
        self.state = self.table[self.state][self.get_col(c)] #状态更新，根据当前状态的取值情况，更新当前状态；
        if self.state == 'nums':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans,INT_MAX) if self.sign == 1 else min(self.ans,-INT_MIN)
        elif self.state == 'sign':
            self.sign = 1 if c == "+" else -1
        #如果是其他状态，ans和符号都不做改变，继续循环；

class Solution:
    def myAtoi(self,str:str)-> int:
        automation = Automation()
        for c in str:
            automation.get(c)  #没有返回值，更新状态和更新结果值
        return automation.sign*automation.ans
if __name__ == '__main__':
    so = Solution()
    a = so.myAtoi("   +0 123") #注意官方的测试用例，该输入会输出0，而不是123；与自己写的int()强制转换有区别

    print("a", a)
"""
📖文字题解
方法一：自动机
思路

字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不小心就会写出极其臃肿的代码。

因此，为了有条理地分析每个输入字符的处理方法，我们可以使用自动机这个概念：

我们的程序在每个时刻有一个状态 s，每次从序列中输入一个字符 c，并根据字符 c 转移到下一个状态 s'。这样，我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s' 的表格即可解决题目中的问题。


复杂度分析

时间复杂度：O(n)，其中 nn 为字符串的长度。我们只需要依次处理所有的字符，处理每个字符需要的时间为 O(1)O(1)。

空间复杂度：O(1)，自动机的状态只需要常数空间存储。




"""