from functools import reduce

target = 1



def sub(amount,coins):
    coins_sorted = sorted(coins,reverse= True)
    if amount == coins_sorted[0]:
        return 1

    if amount == 2:
        return 2
    if amount == 5:
        return 4


def solution(amount, coins):
    index = 0
    rst = []
    def so(amount, coins, index, rst):
        if amount in coins:
            return sub(amount)
        if sum(rst) == amount:
            return reduce(lambda x, y: x*y,map(lambda x: sub(x), rst))
        if index >= len(coins):
            return None
        if sum(rst)+index <= amount:
            rst.append(coins[index])
            return so(amount,coins,index+1,rst)
        else:
            return so(amount,coins,index+1,rst)
    return so(amount,coins,index,rst)
"""
思路：首先，针对coins的每一种币种，先算出每一个币种的所有可能组合数m，比如[1,2,5]币种组合中，1只会有1种，2可能有2种，5可能有4种；
其次，根据目标金额，算出每个只由1,2,5中的任何组合形成的数量n，不能重复;则总数就应当是m*n;

"""

if __name__ == '__main__':
    amount = 10
    coins = [1,2,5]
    rst = solution(amount,coins)
    print("rst is ",rst)