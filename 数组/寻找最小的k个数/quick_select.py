# -*- coding: utf-8 -*-
# @Time : 2020/6/13 16:11
# @Author : ccs
"""
题目描述：有n个整数，请找出其中最小的k个数，要求时间复杂度尽可能低

分析与解法

解法一：全部排序要求在一个序列中寻找最小的k个数，按照惯有的思维方式，应该先对这个序列从小到大进行排序，然后输出前面最小的k个数。
至于选取哪种排序方法，一般人会第一时间想到快速排序（快速排序的平均时间复杂度为 O（nlogn），然后再把序列中的前k个元素输出即可。因此，在n远大于k的情况下，此方法总的时间复杂度为 o（nlogn）+O（k）= O（nlogn）

解法二：部分排序题目没有要求最小的k个数有序，也没有要求最后nk个数有序。既然如此，又何必对所有元素进行排序呢？因此，可以只对部分元素进行排序。具体操作步骤如下。
（1）遍历n个数，把最先遍历到的k个数存入到大小为k的数组中，假设它们就是最小的k个数。
（2）利用选择排序或交换排序找到这k个元素中的最大值kn（找最大值需要遍历这k个数，时间复杂度为O（k）。
（3）继续遍历剩余的nk个数。假设每次遍历到的新元素的值为x，把x与knax进行比较：如果x<km，则用x替换kmx，并回到第2步重新找出k个元素的数组中新的最大元素k；如果x≥kmx，则继续遍历，不更新数组。
每次遍历，更新或不更新数组所用的时间分别为Ok）或0.所以，在k远小于n的情况下，整个过程下来时间复杂度为O（k）+（n-k）0（k）=O（nk）

解法三：用堆代替数组更好的办法是维护一个容量为k的最大堆。
（1）用容量为k的最大堆存储最先遍历到的k个数，假设它们就是最小的k个
数，建堆费时O（k）。建好堆后堆中的元素就是有序的，可令k1<k2<…<kmx（kmx设为最大堆中的最大元素）。
（2）遍历剩余nk个数。假设每次遍历到的新元素的值为x，把x与堆顶元素kmx进行比较：如果x<kma，用x替换km，然后更新堆（用时o（ogk）；否则不更新堆。
这样下来，如果第2步中每遍历剩余的n-k个数中的一个数都要调整堆，那么将得到最坏情况下的时间复杂度Ok+（n-k）ogk）= O（nlogk）。
此解法的原理与解法二的类似，之所以时间复杂度降低了不少，主要是在堆中进行查找或更新的时间复杂度均为Oogk）（若使用解法二，在数组中找出最大元素的时间复杂度为O（k）

"""

#快速排序
import heapq


def get_least_numbers_solution(input,k):
    if len(input) < k :
        return []
    return quick_sort(input)[:k]

def quick_sort(list):
    print("list is ",list)
    if len(list) < 2: #比较是两两比较
        return list[:]
    left = quick_sort([i for i in list[1:] if i <= list[0]])
    print("left is ",left)
    right = quick_sort([i for i in list[1:] if i > list[0]])
    return left + [list[0]] + right #

def get_least_numbers_solution_2(input,k):
    if len(input) < k:
        return []
    return merge_sort(input)[:k]

def merge_sort(list):
    if len(list) < 2:
        return list[:]
    left = merge_sort(list[:len(list)//2])
    right = merge_sort(list[len(list)//2:])
    return merge(left,right)

def merge(left,right):
    res = []
    while left and right:
        res.append(left.pop(0)) if left[0] < right[0] else res.append(right.pop(0))
    res += left if not right else right
    return res


#最大堆
"""
Python中的heapq模块用来建立“堆”这种数据结构。
heapq.heappush(res, -i) 意为：向堆res中添加一个元素-i
heapq.heappushpop(res, -i)意为：将元素-i与堆顶的元素比较。如果该元素值大于堆顶元素，则将该元素与堆顶元素替换。否则不改变堆元素。

"""
def get_least_numbers_solution_3(input,k):
    if len(input) < k :
        return []
    res = []
    for i in input:
        heapq.heappush(res,-i) if len(res) < k else heapq.heappushpop(res,-i)
        rst = list(map(lambda x:-x,res))
        print("rst *** is ",rst)
        return sorted(rst)





if __name__ == '__main__':
    # list = [2,5,7,1,2,3]
    # rst = get_least_numbers_solution(list,5)
    # print("rst is ",rst)
    #
    # list = [2,5,7,1,2,3]
    # rst = get_least_numbers_solution_2(list, 5)
    # print("rst is ", rst)
    #
    list = [2,5,7,1,2,3]
    rst = get_least_numbers_solution_3(list, 5)
    print("rst is ", rst)


