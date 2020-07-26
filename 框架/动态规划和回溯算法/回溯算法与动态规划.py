"""
题目：
原题
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3


一共有5种方法让最终目标和为3。

作者：健健_1e44
链接：https://www.jianshu.com/p/f13ee7aefb53
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

#回溯算法解题框架
"""
def trace_back(路径，选择列表):
    if 满足结束条件:
        result.add(路径)
        return 

    for 选择 in 选择列表：
        做选择
        backtrack(路径，选择列表)  #一条路走到底。不行再回溯；
        撤销选择
"""
##解回溯算法---- 自我写法版本1
init = 0
res = 0
target = 21
def trace_back_er(res,nums):
    if res -target == 0:  #多了一个外部项target，其实可以直接根据nums遍历的索引是否达到最大值来判断。
        return res
    for num_v in nums[init:len(nums)]:   #体现不出来+1、-1的选择
        res = res + num_v
        trace_back(res,nums[init+1:len(nums)])
        res = res - num_v

####回溯算法——推荐解法
sum_a = 0
def trace_back(nums,i,sum_a):
    if i == len(nums):
        if sum_a == target: #元素遍历完，还需要判断是否达到了目标
            return
    for opt in [+1,-1]:
        sum_a = sum_a + opt*nums[i]
        trace_back(nums,i+1,sum_a)
        sum_a = sum_a - opt*nums[i]


#动态规划---思路转换
"""
假设A代表所有取+号的元素的和；B代表所有取-号元素的和；
sum(A) - sum(B)  = target
sum(A)  = target + sum(B)
sum(A) + sum(A)  = target + sum(B) + sum(A)
sum(A)   = (target + sum) / 2  #其中sum代表所有元素的和


由上可以看出，题目可以转化为，已知列表，求子项之和能等于(输入target+总体列表和)/2
 """


#动态规划--解题框架
"""
状态转移方程---迭代方向：正向，反向，斜向;
二维元素的含义：dp[i][k] = x ,表示 若只在前i个物品中选择，若当前背包的容量为j,则最多有x种方法可以装满书包（注意：
此二项元素的声明代表我们求的结果--即有多少种；我们最终的目的是遍历完所有元素并且背包容量为target的方式有多少种：即dp[len(nums)-1][target]）

启发：感觉总之都可以先声明一个元素代表结果，对这个结果从头算起，直到达到目标；
为什么可以这样做？因为初始结果通常是可以知道的，并且每一次状态转移方程也是可知的，因此类比于推演，就可以推到得到结果为止。

#初始状态
dp[0][j] = 0  #没有满足的结果子集
dp[i][0] = 1  #不选就是唯一的结果子集


####不太好的写法#####
#正向遍历
dp[i][j] = dp[i-1][j] + 1 or dp[i-1][j]  #这个地方 or应当是求和；并且选当前的元素后的解法并不等于dp[i-1][j] + 1；
而是等于dp[i-1][j-nums[i-1]] #即当前元素出去之后的背包重量在前i-1个物品中的可能组合。

#反向遍历
dp[i][j] = dp[i+1][j] - 1 or dp[i+1][j]

#斜向遍历


####推荐解法####
如果不把 nums[i] 算入子集，或者说你不把这第 i 个物品装入背包，那么恰好装满背包的方法数就取决于上一个状态 dp[i-1][j]，继承之前的结果。
如果把 nums[i] 算入子集，或者说你把这第 i 个物品装入了背包，那么只要看前 i - 1 个物品有几种方法可以装满 j - nums[i-1] 的重量就行了，所以取决于状态 dp[i-1][j-nums[i-1]]。

dp[i][j] = dp[i-1][j-nums[i-1]]  + dp[i-1][j]  

我相信读者做动态规划问题时，肯定会对dp数组的遍历顺序有些头疼。我们拿二维dp数组来举例，有时候我们是正向遍历：

int[][] dp = new int[m][n];
for (int i = 0; i < m; i++)
    for (int j = 0; j < n; j++)
        // 计算 dp[i][j]

有时候我们反向遍历：

for (int i = m - 1; i >= 0; i--)
    for (int j = n - 1; j >= 0; j--)
        // 计算 dp[i][j]

有时候可能会斜向遍历：

// 斜着遍历数组
for (int l = 2; l <= n; l++) {
    for (int i = 0; i <= n - l; i++) {
        int j = l + i - 1;
        // 计算 dp[i][j]
    }
}


"""

###解法1--二维数组
def subset(nums,sum):
    n = len(nums)
    dp = [[]]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(sum):
            if j > nums[i-1]: #当前目标容量大于当前元素，可选/可不选
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
            else:# 背包的空间不足，只能选择不装物品 i
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]

###解法2---一维数组
"""
将二维数组转化成一维数组
dp[j]表示当前有dp[j]种可能使得背包容量为k
"""
def subset_02(nums,sum):
    n = len(nums)
    dp = []
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in reversed(range(sum)): #j要逆向遍历，根据已有结果，再根据结果反推；
            if j >= nums[i-1]: #当前目标容量大于当前元素，可选/可不选
                dp[j] = dp[j] + dp[j-nums[i-1]]  #因为j是从后往前遍历的，因此dp[j-nums[i-1]]就相当于是前面的元素--待计算；
            else:# 背包的空间不足，只能选择不装物品 i
                dp[j] = dp[j]
    return dp[sum]


###假设j不逆向
def subset_02_er(nums,sum):
    n = len(nums)
    dp = []
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(sum):
            if j >= nums[i-1]: #当前目标容量大于当前元素，可选/可不选
                dp[j] = dp[j] + dp[j-nums[i-1]]  #因为j是从后往前遍历的，因此dp[j-nums[i-1]]就相当于是前面的元素--待计算；
            else:# 背包的空间不足，只能选择不装物品 i
                dp[j] = dp[j]
    return dp[sum]


"""
对照二维 dp，只要把 dp 数组的第一个维度全都去掉就行了，唯一的区别就是这里的 j 要从后往前遍历，原因如下：
因为二维压缩到一维的根本原理是，dp[j] 和 dp[j-nums[i-1]] 还没被新结果覆盖的时候，相当于二维 dp 中的 dp[i-1][j] 和 dp[i-1][j-nums[i-1]]。
那么，我们就要做到：在计算新的 dp[j] 的时候，dp[j] 和 dp[j-nums[i-1]] 还是上一轮外层 for 循环的结果。
如果你从前往后遍历一维 dp 数组，dp[j] 显然是没问题的，但是 dp[j-nums[i-1]] 已经不是上一轮外层 for 循环的结果了，这里就会使用错误的状态，当然得不到正确的答案。

"""