"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题目描述可知，K可以为正无穷，无限大的交易次数：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])  #这个地方有点不太明白
            = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])

我们发现数组中的 k 已经不会改变了，也就是说不需要记录 k 这个状态了：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])


如果 k 为正无穷，那么就可以认为 k 和 k - 1 是一样的。可以这样改写框架：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])

我们发现数组中的 k 已经不会改变了，也就是说不需要记录 k 这个状态了：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
直接翻译成代码：
int maxProfit_k_inf(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i]);
    }
    return dp_i_0;
}

"""

def solution_err(prices,K):
    """
    可以交易k次，其中买一次卖一次 称为一个完整的交易
    """
    n = len(prices)
    dp = [[0,0,0] for i in range(n)]
    for i in range(n):
        for j in range(K):
            if i == 0:
                dp[0][j][0] = 0
                dp[0][j][1]  = -prices[i]
                i = i + 1
                continue
            dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
            dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j][0]-prices[i])

    return dp[n-1][K-1][0]

def solution_fianl_err(prices):
    """
    可以交易k次，其中买一次卖一次 称为一个完整的交易
    """
    n = len(prices)
    dp = [[0,0] for i in range(n)]
    for i in range(n):
        if i == 0:
            dp[0][0] = 0
            dp[0][1]  = -100000 #是-inf,而不是-prices[i]
            continue
        dp[i][0] = max(dp[i][0],dp[i][1]+prices[i])  #先有买，再有卖，有历史盈利项；
        dp[i][1] = max(dp[i][1],dp[i][0]-prices[i])  #这个地方相比与1版本，因为可发生多次交易，因此，可能是先卖后买，也有历史盈利项；
    return dp[n-1][0]


# def solution_final_2(prices):
#     """
#     可以交易k次，其中买一次卖一次 称为一个完整的交易
#     """
#     n = len(prices)
#     # dp = [[0,0] for i in range(n)]
#     # dp[0][0] = 0
#     # dp[0][1]  = -100000
#     dp = [[0,-100000] for i in range(n)]
#
#     for i in range(n):
#         tmp = dp[i][0]
#         dp[i][0] = max(dp[i][0],dp[i][1]+prices[i])  #先有买，再有卖，有历史盈利项---但是是利用当前状态来更新的，没有用历史状态去更新？？？--这样方便写逻辑？；
#         dp[i][1] = max(dp[i][1],tmp-prices[i])  #这个地方相比与1版本，因为可发生多次交易，因此，可能是先卖后买，也有历史盈利项；
#     return dp[n-1][0]

def solution_final(prices):
    """
    最终正确版本，可以看出，这个地方是没进行一次交易，状态为历史所有交易最新盈利值；因此，程序里面没有用数组去计算而是用盈利的累积最新；
    目的就是：尽可能保持最大盈利，并且交易次数尽量多；每次刷新这个盈利值（对应最终状态为买的盈利值和最终状态为卖的盈利值），咱们结果对应最终状态为卖的盈利值；
    """
    n = len(prices)
    # dp = [[0,0] for i in range(n)]
    # dp[0][0] = 0
    # dp[0][1]  = -100000
    dp_i_0 = 0
    dp_i_1 = -10000

    for i in range(n):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0,dp_i_1+prices[i])  #先有买，再有卖，有历史盈利项---但是是利用当前状态来更新的，没有用历史状态去更新？？？--这样方便写逻辑？；
        dp_i_1 = max(dp_i_1,tmp-prices[i])  #这个地方相比与1版本，因为可发生多次交易，因此，可能是先卖后买，也有历史盈利项；
    return dp_i_0,dp_i_1


if __name__ == '__main__':
    # prices = [1,2,3,4,5]
    prices = [7,1,5,3,6,4]
    #k可以为正无穷，因此K = +inf
    rst = solution_final(prices)
    print("rst is ", rst)