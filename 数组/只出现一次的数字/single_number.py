# -*- coding: utf-8 -*-
# @Time : 2020/6/22 15:28
# @Author : ccs
from typing import List
class Solution_1_improve:
    """
    解法1~改进版:
    每出现一个重复的，会将表里面该重复值移除，然后再重头开始比较，这样会导致计算时间复杂度较高；因为有可能会重复计算之前那些未重复的值；
    更改为：
    每出现一个重复的，会将表里面该重复值移除，不会重头开始比较，而是将已经比较过的元素列表保存下来，供下次比较用；


    但是这个也超出了时间限制？为什么？
    """
    def singleNumber(self, nums: List[int]) -> int:
        q = 0
        res = []
        while(q < len(nums)):
            if  nums[q] not in res:
                res.append(nums[q])
            else:
                res = [i for i in res if i != nums[q]]  #这一步应当在nums修改之后
                nums_1 = [i for i  in nums if  i != nums[q]]
                res_copy = list(res)

                flag = [i for i in res if i in nums_1]
                if len(flag) == 1: #如果是答案，则可以直接返回
                    return flag[0]
                else:
                    nums_1 = [i for i in nums_1 if i not in flag]  #截至当前比较的结果，如果出现在结果集中,且不是答案，则应该去掉；继续用剩下的重复比较
                    res_copy = [i for i in res_copy if i not in flag]
                nums = list(nums_1)
                res = list(res_copy)
                q = -1
            q = q + 1
        return res[0]

class Solution_1:
    """
    解法1:
    每出现一个重复的，会将表里面该重复值移除，然后再重头开始比较，这样会导致计算时间复杂度较高；因为有可能会重复计算之前那些未重复的值；

    """
    def singleNumber(self, nums: List[int]) -> int:
        p = 0
        q = 1
        remove = []
        while(q < len(nums)):
            if  nums[q] not in nums[:p+1]:
                nums[p+1] = nums[q]
                p = p + 1
            else:
                nums = [i for i in nums if i != nums[q]]
                p = 0
                q = 0
            q = q + 1
        return [i for i in nums if i not in remove][0]


class Solution_2:
    """
    解法2
    遇到重复的值，不删除；先记下来；
    到最后面再将原表与需要删除的字符列表求差集。
    """
    def singleNumber(self, nums: List[int]) -> int:
        p = 0
        q = 1
        remove = []
        while(q < len(nums)):
            if  nums[q] not in nums[:p+1]:
                nums[p+1] = nums[q]
                p = p + 1
            else:
                remove.append(nums[q])
            q = q + 1
        return [i for i in nums if i not in remove][0]


"""
执行用时：5888 ms, 在所有 Python3 提交中击败了5.60%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.26%的用户
"""
if __name__ == '__main__':
    # sp =Solution()
    sp = Solution_1_improve()
    # a =  [1,3,1,-1,3]
    # a = [-1,-1,-2]
    a = [4, 1, 2, 1, 2]

    rst = sp.singleNumber(a)
    print("rst is ",rst)


