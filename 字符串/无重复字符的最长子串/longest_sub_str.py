# -*- coding: utf-8 -*-
# @Time : 2020/6/15 20:13
# @Author : ccs


"""

标签：滑动窗口
暴力解法时间复杂度较高，会达到 O(n^2)O(n
2
 )，故而采取滑动窗口的方法降低时间复杂度
定义一个 map 数据结构存储 (k, v)，其中 key 值为字符，value 值为字符位置 +1，加 1 表示从字符位置后一个才开始不重复
我们定义不重复子串的开始位置为 start，结束位置为 end
随着 end 不断遍历向后，会遇到与 [start, end] 区间内字符相同的情况，此时将字符作为 key 值，获取其 value 值，并更新 start，此时 [start, end] 区间内不存在重复字符
无论是否更新 start，都会更新其 map 数据结构和结果 ans。
时间复杂度：O(n)O(n)
代码

作者：guanpengchn
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

def longest_sub_str(str):
    max = 1
    for i,_ in enumerate(str):
        if  str[i+1]  in str[:i+1]:
            return max, str[:i+1],str[i+1:]
        else:
            max = max + 1
    return max,str[:i+1], str[i + 1:]

def longest_sub_str_2(str):
    max,rst,str = longest_sub_str(str)
    while(max < len(str)):
        max_new,rst_new,str_new = longest_sub_str(str)
        str = str_new
        if max_new > max:
            max = max_new
            rst = rst_new
        else:
            continue
    return max,rst

"""
思路对比：
先计算第一个字符开始的情况，返回，当前字符对应最大字符长度，对应最大字符，以及即将遍历的下一个字符；（缺点：就是存储东西太多）
后面再单独处理？ 
~~~~缺点：不够通用；应当想一个通用的循环，需要哪些变量（起始索引，终止的计数指针，出现元素的集合），每一次循环要做的事：
起始索引更新，终止的计数指针更新，出现元素的集合更新；计算出当前历史累计的最大值；

对于字符串重复，我的是利用in判断，如果在里面，就跳出；如果不在里面循环进行

而他也是用in，如果不在里面，就循环进行最大字符长度计数；默认如果在里面，不进行任何操作（不会返回的形式，浪费资源，而是直接计算当前最大元素长度
————————即while不执行了，而是去执行求最大字符长度 ans = max(ans, rk - i + 1)），rk是右指针，i是当前第i个元素，

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:  #当前指针在n的范围内，并且当前指针对应元素不在出现的集合中；
                # 不断地移动右指针
                occ.add(s[rk + 1])  #更新集合
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)  #每一次遍历，当前元素右指针的遍历；

        return ans


"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


if __name__ == '__main__':

    #自己解法，leecode提交不能通过所有测试用例
    rst = longest_sub_str_2("abcabcbb")
    print("rst is ",rst)

    #官方写法，可以通过所有样例
    s = Solution()
    rst = s.lengthOfLongestSubstring("abcabcbb")
    print("rst is ",rst)

