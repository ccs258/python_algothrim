# -*- coding: utf-8 -*-
# @Time : 2020/6/15 17:30
# @Author : ccs

def twoSum(nums, target):
    lens = len(nums)
    final_rst = []
    for i in range(lens):
        if (target - nums[i]) in nums[i+1:]:
            j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2，注意此处用nums,因为要保留源输入的索引；
            if j:  #写在里面
                rst =  [i,j]
            else:
                rst =  []
            final_rst.append(rst)
    return final_rst


if __name__ == '__main__':
    rst = twoSum([1,2,2,3,4],4)
    print("rst is ",rst)