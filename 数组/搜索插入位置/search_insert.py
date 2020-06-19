# -*- coding: utf-8 -*-
# @Time : 2020/6/19 16:34
# @Author : ccs

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2

输入: [1,3,5,6], 7
输出: 4

"""
from typing import List

class Solution:

    def searchInsertSub(self, nums: List[int], target: int):
        if len(nums) == 1:
            if target >= nums[0]:
                return (nums[0], 1)
            else:
                return (nums[0], -1)
        else:
            mid = len(nums) // 2
            if target > nums[mid]:
                return self.searchInsertSub(nums[mid:], target)
            else:
                return self.searchInsertSub(nums[:mid], target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        num_dict = {}
        for idx, val in enumerate(nums):
            num_dict[val] = idx
        if target in nums:
            return num_dict.get(target)
        else:
            val, flag = self.searchInsertSub(nums, target)
            if flag == 1:
                return num_dict.get(val) + 1
            else:
               return 0 if num_dict.get(val) == 0 else  num_dict.get(val) - 1

"""
执行用时：32 ms, 在所有 Python3 提交中击败了97.02%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了7.14%的用户

思路分析：
输入前提：可以假设输入是无重复的有序数组；
第一步：先初始化一个hash字典，用以存储{元素:索引}，方便后续通过元素找到索引；
第二步，找target的索引：
分两种情况：
case1：target在hash字典中，直接去hash表中查找返回其索引位置；
case2：target不在hash字典中，通过二分法查找,与目标值最近的目标值；如果大于目标值，则返回目标值索引+1;否则，返回目标值索引-1。



"""

if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, 5, 6]
    target = 0

    rst = so.searchInsert(nums, target)
    print("rst is", rst)
