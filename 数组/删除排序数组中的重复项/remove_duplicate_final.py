# -*- coding: utf-8 -*-
# @Time : 2020/6/19 14:08
# @Author : ccs

"""
已知输入是：排序数组；

方法：双指针法
算法

数组完成排序后，我们可以放置两个指针 ii 和 jj，其中 ii 是慢指针，而 jj 是快指针。只要 nums[i] = nums[j]nums[i]=nums[j]，我们就增加 jj 以跳过重复项。

当我们遇到 nums[j] \neq nums[i]nums[j]

​
 =nums[i] 时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]nums[j]）的值复制到 nums[i + 1]nums[i+1]。然后递增 ii，接着我们将再次重复相同的过程，直到 jj 到达数组的末尾为止。

"""
def remove_dupliacted(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i = i + 1
            nums[i] = nums[j]

    return i+1,nums

"""
复杂度分析

时间复杂度：O(n)，假设数组的长度是 nn，那么 ii 和 jj 分别最多遍历 nn 步。

空间复杂度：O(1)。

"""
if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    rst,rst2 = remove_dupliacted(nums)
    print("rst is ",rst)
    print("rst2 is ",rst2)

