"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
nums = [2,7,9,3,1]#[1, 2, 3, 1]
mem = [-1] * len(nums)


def solution(start, nums):
    """
    递归的形式---自顶向下
    """
    if start >= len(nums):  # 这个地方是大于等于，最末尾为起点，已经被前面的点(作为start+1或start+2)计算在内了，所以以它为起点的都为0；
        return 0  #这是递归最底部结果返回
    if mem[start] != -1:
        return mem[start] #这是递归中间缓存结果返回
    res = max(nums[start] + solution(start + 2, nums), solution(start + 1, nums))
    mem[start] = res
    return res  #这是递归结果返回

def solution_2_err(nums):
    """
    自底向上
    """
    res = 0
    index = 0
    while(index <= len(nums)-3):
        if index <= len(nums)-3:
            tmp = max(nums[index]+nums[index+2],nums[index+1])
            res = res + tmp
            index = index + 1  #这样写不好，因为可能index的跨度不是为1，因此不要用累加这种来写，而是用更新每个值状态来写；
    return res  #这是递归结果返回

def solution_3(nums):
    n = len(nums)
    dp = [0]*(n+2)
    i = n - 1
    while(i>0):  #从顶往下计算
        dp[i]=max(dp[i+1],dp[i+2]+nums[i])
        i = i  - 1
    return dp[0]




def solution_1(nums):
    """

    """
    rst = solution(0, nums)

    return rst


if __name__ == '__main__':
    # rst = solution_1(nums)
    rst = solution_3(nums)

    print("rst is ", rst)
