# -*- coding: utf-8 -*-
# @Time : 2020/6/14 15:25
# @Author : ccs
"""

题目描述:寻找和为定值的两个数


输入一个整数数组和一个整数，在数组中查找一对数，满足它们的和正好是输入的那个整数。
如果有多对数的和等于输入的整数，输出任意一对即可。
例如，如果输入数组[1,2,4,5,7,11,15]和整数15，那么由于4+11=15，因此输出4和11。


参考：https://blog.csdn.net/zichen_ziqi/article/details/81417262?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.nonecase

"""

#暴力解法 #寻找两个数加起来和为target #需要去重

def get_res_enumeration(arr,value):
    """
    时间复杂度为O(N^2)
    """
    l1 = len(arr)
    res = []
    for i in range(l1):
        for j in range(i+1,l1):
            if arr[i] + arr[j] == value:
                res.append((arr[i],arr[j]))
    return res


def get_res_quicksort(nums,target):
    """
    双指针——快速排序思想，O(NlogN)

     思想：来自于快速排序，在一个有序的数组（从小到大）中最左边一定是最小值，最右边是最大值。我们可将最小值与最大值相加与目标值进行比较，如果两数之和大于目标值，我们就让最大值小一点（读取第二个最大值），如果两数之和小于目标值，我们就让最小值大一点（读取第二个最小值），如果两数之和刚好等于目标值，保存最大值，最小值，并且让最大值小一点，最小值大一点。需要注意的是前提条件是数组必须有序！！！

        简化：对nums先排序，然后定义两个指针，一个low = 0指向数组头，一个high = len(nums) - 1指向数组的尾，看其和nums[low]+nums[high]是否== target；若==，则查找成功返回；若>sum，则尾指针high--；若<sum，则头指针low++。

         时间复杂度：快排O(NlogN)，查找O(N)；所以总的时间复杂度为：O(NlogN)。

    """
    nums = sorted(nums)
    l1 = len(nums)
    res = []
    if l1 >= 2:
        low,high = 0,l1-1
        while low < high:
            if nums[low] + nums[high] == target:
                res.append((nums[low],nums[high]))
                low += 1
                high -= 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low += 1
        return res

"""
需要注意的是，这里的排序算法选择的是时间复杂度为O(NlogN)的，加上查找所花时间O(N)，最终为O(NlogN)。肯定有人会想，那我为啥不选择时间复杂度为O(N)的排序算法（如：非比较排序的基数排序、计数排序或桶排序）先排序，再查找呢？这样结果就是O(N)了，效率岂不是更高，哎呀，你真的很聪明！！！但是接下面的方法，并不是这样做的，而是利用哈希表来完成！

"""

def get_res_hash_map(nums,target):
    """

    思想：给定一个数，根据hash表查找另一个数只需要O(1)的时间。
    但需要空间换时间，空间复杂度为O(n)；可以用hashMap实现，hashMap<a[i], 次数>。
    遍历一遍数组，若次数没有存在hashMap中，则将其加入，次数为1；
    再遍历一遍数组，对每个值nums[i]，判断target - nums[i]是否在hashmap中
    【即对应的value是否==1】；若存在，则查找成功；否则继续遍历下一个。直到遍历完整个数组。

    """
    result = []
    for i,value in enumerate(nums):
        if (target-value) in nums[i+1:]:
            result.append((value,target-value))
    return result

if __name__ == '__main__':
    input = [1,2,3,4,6,4,5,7,1,3,4,0,2]
    target = 6
    print(set(get_res_enumeration(input,target)))
    print(set(get_res_quicksort(input,target)))
    print(set(get_res_hash_map(input,target)))



