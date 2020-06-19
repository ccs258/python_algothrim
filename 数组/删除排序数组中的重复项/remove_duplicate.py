# -*- coding: utf-8 -*-
# @Time : 2020/6/19 10:23
# @Author : ccs
from typing import List


class Solution:
    def sub(self,left,right):
        if left[-1:][0] != right[0]:
            left = left + right[:1]
            right = right[1:]
        else:
            right = right[1:]

        if len(right) == 1:
            if left[-1:][0] != right[0]:
                left =  left + right[:1]
            return left
        else:
            return self.sub(left, right)

    def removeDuplicates(self, nums: List[int]) -> int:
        left = nums[:1]
        right = nums[1:]
        left = self.sub(left, right)
        print("left is ",left)
        return len(left)

"""
复杂度分析

时间复杂度：O(n*n)。

空间复杂度：O(1)。


对比官方解法：
输入： [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

官方解法结果：长度为5，数组为 [0, 1, 2, 3, 4, 2, 2, 3, 3, 4],不过可以处理下，根据长度取值；
自己编写的结果：长度为5，数组为 [0, 1, 2, 3, 4]


我的思路：
将数组元素分成两部分：左边不重复部分，和右边数组部分；
初始化的时候：左边=num[:1],右边=nums[1:]
递归逻辑：判断左边最后一个元素跟右边第一个元素的关系（因为是有序数组），更新左边，右边；
如果右边数组长度为1，就返回结果值；
否则，就重新迭代递归逻辑；

遇到的问题：
在leetcode上提交，发现结果运行与本地pycharm不一致；可能是我这个程序"使用了额外的数组空间";
"""


if __name__ == '__main__':
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = [1,1,2]

    so = Solution()
    rst = so.removeDuplicates(nums)
    print("rst is",rst)
