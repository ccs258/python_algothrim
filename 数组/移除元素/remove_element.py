# -*- coding: utf-8 -*-
# @Time : 2020/6/19 14:36
# @Author : ccs
"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

题目理解：输入是非排序数组；


"""
from typing import List


class Solution:
    def removeElement_sub(self, nums: List[int], val: int) -> List[int]:
        def remove(x):
            if x[0] == val :
                x =  x[1:]
            if x[-1] == val:
                x =  x[:-1]
            return x
        nums = remove(nums)
        if len(nums) == 1:
            return nums
        else:
            return remove(nums[:len(nums)//2]) + remove(nums[len(nums)//2:])

    def removeElement(self, nums: List[int], val: int) -> int:
        rst = self.removeElement_sub(nums,val)
        print("rst is ",rst)
        return len(rst)


if __name__ == '__main__':
    so = Solution()
    # nums = [3, 2, 2, 3]
    # val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    rst = so.removeElement(nums,val)
    print("rst is ",rst)