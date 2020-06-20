# -*- coding: utf-8 -*-
# @Time : 2020/6/20 9:56
# @Author : ccs
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]
if __name__ == '__main__':
    so = Solution()
    rst = so.numSquares(12)
    print("rst is ",rst)