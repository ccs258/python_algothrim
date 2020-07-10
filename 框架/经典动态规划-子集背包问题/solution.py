def solution(nums):
    target = sum(nums) // 2
    if sum(nums) % 2 != 0:
        return None
    index = 0
    rst = []

    def so(nums, index, rst):
        if sum(rst) == target:
            return rst
        if index == len(nums):
            return None

        if sum(rst) + nums[index] <= target:  # 判断是否选择当前的数字
            rst.append(nums[index])
            return so(nums, index + 1, rst)
        else:
            return so(nums, index + 1, rst)

    return so(nums, index, rst)


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    rst = solution(nums)
    print("rst is ", rst)
