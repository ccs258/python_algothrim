#基本的二分搜索
def binary_search(nums,target):
    left = 0
    right = len(nums) -1
    while(left<=right):
        mid =  left + (right - left)//2  #防止溢出，如果left是一个比较大的数，right是一个更大的数，直接加起来除以2求mid可能会溢出；巧妙的办法是先求出一半，再相加，利用数学公式；
        if nums[mid] < target :
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        elif nums[mid] == target:
            return mid
    return -1
"""
上面搜索left,right为什么会变成mid-1和mid+1?

解说：
刚才明确了「搜索区间」这个概念，而且本算法的搜索区间是两端都闭的，即 [left, right]。那么当我们发现索引 mid 不是要找的 target 时，下一步应该去搜索哪里呢？
当然是去搜索 [left, mid-1] 或者 [mid+1, right] 对不对？因为 mid 已经搜索过，应该从搜索区间中去除。

参考：https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/er-fen-cha-zhao-xiang-jie
"""

#左边索引的二分搜索
# 目标：找到目标列表中小于该目标值的元素个数
"""
题目描述
比如对于有序数组 nums = [2,3,5,7], target = 1，算法会返回 0，含义是：nums 中小于 1 的元素有 0 个。
再比如说 nums = [2,3,5,7], target = 8，算法会返回 4，含义是：nums 中小于 8 的元素有 4 个。
"""
def binary_search_left(nums,target):
    """
    左边索引的二分搜索
    """
    left = 0
    right = len(nums) -1
    while(left<=right):
        mid =  left + (right - left)//2
        if nums[mid] < target :
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] == target:
            right = mid -1
    if nums[left] != target or left > len(nums):
        return -1
    return left

def binary_search_right(nums,target):
    """
    右边索引的二分搜索
    """
    left = 0
    right = len(nums) -1
    while(left<=right):
        mid =  left + (right - left)//2
        if nums[mid] < target :
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] == target:
            left = mid + 1
    if nums[right] != target or right < 0:
        return -1
    return right



if __name__ == '__main__':
    nums = [1,2,3,3,4,5]
    target = 3
    rst = binary_search(nums,target)
    print("普通的二分法查找：rst is ",rst)

    rst = binary_search_left(nums,target)
    print("左边索引搜索法：rst is ",rst)

    rst = binary_search_right(nums,target)
    print("右边索引搜索法：rst is ",rst)