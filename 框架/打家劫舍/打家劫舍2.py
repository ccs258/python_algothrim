"""
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
nums = [1,2,3,1]#[2,3,2]
mem = [-1] * len(nums)


def solution(start, nums):
    if start >= len(nums):  # 这个地方是大于等于，最末尾为起点，已经被前面的点(作为start+1或start+2)计算在内了，所以以它为起点的都为0；
        return 0
    if mem[start] != -1:
        return mem[start]
    res = max(nums[start] + solution(start + 2, nums), solution(start + 1, nums))
    mem[start] = res
    return res


def solution_1(nums):
    """
    首尾相连，因为头部0与尾部元素索引len(num)-1相邻，因此，nums中能遍历的元素分为两类：
    证明要么包含头：即从0开始（包含头）到len(nums)-2（尾部为倒数第二位）；要么包含尾len(nums)-1，从1开始（不包含头）到len(nums)-1（即最后一位）

    """
    rst = max(solution(0, nums[:len(nums)-1]),solution(1,nums[:len(nums)]))

    return rst


if __name__ == '__main__':
    rst = solution_1(nums)
    print("rst is ", rst)
