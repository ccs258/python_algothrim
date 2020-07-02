"""
先看下题目：给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，
每种硬币的数量无限，再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。


比如说 k = 3，面值分别为 1，2，5，总金额 amount = 11。那么最少需要 3 枚硬币凑出，即 11 = 5 + 5 + 1。

"""
##版本1,对每一次值，先去币值列表里面找最大的来组合，这样到最后就会是最小的币值数量组合了；
#好处，不存在多次计算的问题，比如10-5=5，不会会递归去调用两次计算5，而是直接返回结果；但是如果是两个6呢，5,5,2；而不是5,1,5,1；
def solution_1(a,coins):
    if a < 0 :
        return -1
    rst = float("INF") #int("INF"),ValueError: invalid literal for int() with base 10: 'INF'
    coins = sorted(coins,reverse=True)  #让所有的货币组先排序，从大到小；
    print("coins is ",coins)
    if a == 1 or a == 2 or a == 5:
        return 1
    for coin in coins:
        print("XXXXX")
        if a - coin < 0: #如果发现当前值小于最大币值，则继续循环，找到下一个币值；
            continue
        rst = min(rst,solution_1(a-coin,coins)+1) #找到币值后，钱更新为剩下的，coins币种仍然不变；
    return rst if rst != float('INF') else -1



#版本2---labuladong,有点抽象，思想跟上面一样;但实现方式不太一样：这个会产生重复计算，增加备忘录

#他这里coins没有排序
def coinChange_2(coins,a):
    def dp(n):
        if n == 0 : return 0
        if n < 0 : return -1
        res = float("INF")
        for coin in coins:
            subproblem = dp(n-coin)
            if subproblem == -1:continue
            res = min(res,1+subproblem)
        return res if res != float("INF") else -1
    return dp(a)


#版本3 -- 增加备忘录
#他这里coins没有排序，会算出来有很多组合，最终取最小；
def coinChange_3(coins,a):
    memo = []
    def dp(n):
        if n in memo:return memo[n]
        if n == 0:return 0  #可以看出，初始值，就表示当前值的最小币值个数；
        if n < 0:return -1
        res = float("INF")
        for coin in coins:
            subproblem = dp(n-coin)  #只会有一个输入
            if subproblem == -1:continue
            res = min(res,1+subproblem)

        memo[n] = res if res != float("INF") else -1
        return memo[n]
    return dp(a)


#版本4，


if __name__ == '__main__':
    a = 14
    coins = [1,2,5]
    rst = solution_1(a,coins)
    print("rst is ",rst)

    #RecursionError: maximum recursion depth exceeded while calling a Python object