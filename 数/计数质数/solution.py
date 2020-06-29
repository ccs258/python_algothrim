import math


class Solution:
    def countPrimes(self, n: int) -> int:
        rst = self.countPrimes_sub(n)
        rst.remove(1)
        return len(rst)

    def countPrimes_sub(self,n):
        sqrt_n = int(math.sqrt(n))
        rst = []
        if n == 1:
            return [1]
        if 1 < n <= 3 :
            return list(range(1,n+1,1))
        else:
            for i in range(sqrt_n+1,n+1,1): #3,9,1
                flag = 0
                for j in range(2,sqrt_n+1,1): #1,3,1
                    if i % j == 0 and j != 1:
                        flag = 1
                if flag == 0:
                    rst.append(i)
                    print("rst is ",rst)
            return self.countPrimes_sub(sqrt_n) + rst

class Solution2:
    def countPrimes(self, n: int) -> int:
        rst = self.countPrimes_sub(n)
        rst.remove(1)
        return len(rst)

    def countPrimes_sub(self,n):
        sqrt_n = int(math.sqrt(n))
        rst = 0
        if n == 1:
            return 0
        if 1 < n <= 3 :
            return len(list(range(2,n+1,1)))
        else:
            for i in range(sqrt_n+1,n+1,1): #3,9,1
                flag = 0
                for j in range(2,sqrt_n+1,1): #1,3,1
                    if i % j == 0 and j != 1:
                        flag = 1
                if flag == 0:
                    rst = rst + 1
            return self.countPrimes_sub(sqrt_n) + rst

class Solution3:
    def countPrimes(self, n: int) -> int:
        rst = self.countPrimes_sub(n)
        return rst

    def countPrimes_sub(self,n):
        input = list(range(0,n+1,1))
        sqrt_n = int(math.sqrt(n))
        rst = 0
        if n == 1:
            return 0
        if 1 < n <= 3 :
            return len(list(range(2,n+1,1)))
        else:
            for i in range(sqrt_n+1,n+1,1): #3,9,1
                flag = 0
                input[i] = 0
                for j in range(2,sqrt_n+1,1): #1,3,1
                    if i % j == 0 and j != 1:
                        input[i] = 1
                if flag == 0:
                    rst = rst + 1
            return self.countPrimes_sub(sqrt_n) + rst


"""
出现问题：n越大，递归越多，因此，在leetcode中会超出限制；因此题目说的是让求结果的长度。
Line 18: RecursionError: maximum recursion depth exceeded in comparison;


即便改成版本2，将返回的结果从列表改成数值，其还是会报错，因为本质上迭代还是存在；
解决办法不要利用迭代判断计算一次性实现，而是分成2步：第一步，先标记质数；第二步，计算标记的个数；


改成版本3，发现还是没法实现，因为本质上，我这个地方，每次标记只能根号n之后的结果，前面的还得用递归标记；


对比参考的解法：已知遍历到根号n，根据根号n之前的遍历，标记每个遍历量的倍数，在遍历量平方至n的范围内。



"""
import math


class Solution4:
    def countPrimes(self,n):
        n = n - 1
        if n == 0 or n == -1:
            return 0
        if n == 2:
            return 1
        isPrim  = [1] * (n)
        print("before isPrim is ",isPrim)
        i = 2
        while(i*i <= n):
            if isPrim[i-1]:
                j = i * i
                while(j <= n):
                    isPrim[j-1] = 0
                    j = j + i
            i = i + 1

        count = -1

        print("isPrim is ",isPrim)

        for i in isPrim:
            if i:
                count = count + 1

        return count

"""
注意思路：小于n的输入，不是等于n;
官方的思路：初始化数组；先取前根号n之前的数，遍历；
加了个条件，当前该遍历的量是否已经被标记为非质数，如果是，则不用操作，如果否，才开始下述操作：
根据遍历量的倍数（从遍历量的平方开始，每次遍历加的数为遍历量，直到小于等于n为止），每次循环就标记一次（因为满足倍数关系）；


标记是针对全局的数组变量；因为可能存在前一个遍历量和下一个遍历量共同的倍数，因此，前一次标记之后，下一次就不用了再标记处理。
"""


if __name__ == '__main__':
    so = Solution4()
    n = 8
    rst = so.countPrimes(n)
    print("rst is ",rst)


