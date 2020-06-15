# -*- coding: utf-8 -*-
# @Time : 2020/6/15 16:44
# @Author : ccs

"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""

class Solution(object):
    def longestCommonPrefix(self, s) -> str:
        if not s:
            return ""
        print("s is ",s)
        s.sort()  #对输入进行排序，短的字符串在最后；
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:  #如果长度小于最短字符，则继续进行比较
                res += a[i]
            else:  #最长公共前缀不会超过里面的最小子符长度；
                break
        return res

"""
作者：powcai
链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

if __name__ == '__main__':
    so = Solution()
    list_str = ["aabbcccc",'andbc']
    rst = []
    rst.append(so.longestCommonPrefix(list_str))
    print("rst is ",rst)