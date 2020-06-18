# -*- coding: utf-8 -*-
# @Time : 2020/6/18 16:43
# @Author : ccs
class Solution:
    """
    最长匹配字符非前缀字符
    """
    def cal_common_prefix(self,x,start,input_list):
        new_str = list(map(lambda y: True if x == y[:start+1] else False, input_list))
        if False in new_str :
            return 0,None
        else:
            return start+1, x[:start+1]

    def longestCommonPrefix(self,strs):
        if not isinstance(strs,list) or not strs:
            return  ''
        min_len = min([len(x) for x in strs])
        min_str = list(filter(lambda x: len(x) == min_len, strs))[0]
        if len(strs) > 1:
            strs.remove(min_str)
        else:
            return strs[0]
        max = 0
        max_str = ''

        for idx,_ in enumerate(min_str) :
            max_len,max_len_str = self.cal_common_prefix(min_str[:idx+1],idx,strs) #时间复杂度是，0+1+2+3+...+n = n*(n+1)/2
            if max_len > max  :
                max = max_len
                max_str = max_len_str
        return max,max_str




if __name__ == '__main__':
    so = Solution()
    # strs = ["flower","flow","flight"]
    # strs = ["dog", "racecar", "car"]
    # strs = ["floflwtwer","flowflwt","fligflwtht"]



    # strs = ["a"]
    strs = ["c","c"]

    rst,rst2 = so.longestCommonPrefix(strs)
    print(rst,rst2)

    #["ca","a"]

    """









第一版本：计算了所有公共字符长度，思路是：
现在字符串列表中找到最短的那个字符串，并且剩下的字符串元素作为比较字符串元素；（需要考虑一些边界条件，输入为["a","a"],[],["ca","a"]）
用来做遍历，
第一次是用从第一个字符串开始的整个字符串作为标准字符串，遍历该标准字符串按第一个开始，连续去匹配，匹配方式是如果当前连续增长的索引 是否 in 剩余字符串中，找最长的；
第二次是用从第二个开始的,按上述规则匹配....

第二版本；题目求的是最长前缀，改了匹配里面的匹配规则为前缀单个元素相等，for循环保留的，但这样其实没必要；可以直接不用循环，直接取整个前缀比较；
第三版本：时间效率提升了，去掉了匹配里面的for循环；


第一版本 执行结果：
执行用时 :444 ms, 
在所有 Python3 提交中击败了5.85%的用户
内存消耗 :13.7 MB, 
在所有 Python3 提交中击败了6.15%的用户
存在 重复计算；

第二版本 执行结果：
执行用时 :48 ms, 
在所有 Python3 提交中击败了36.58%的用户
内存消耗 :13.8 MB, 
在所有 Python3 提交中击败了6.15%的用户
    
    
#官方的解答；
执行用时 :36 ms, 
在所有 Python3 提交中击败了92.29%的用户内存消耗 :
13.7 MB, 在所有 Python3 提交中击败了6.15%的用户
    """

