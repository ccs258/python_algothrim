# -*- coding: utf-8 -*-
# @Time : 2020/6/24 17:33
# @Author : ccs
# class NodeTree:
#     pass


# def sorted_array_tree(root:NodeTree):
#     if not root:
#         return None
#     if root.left:
#         return root.left
#     elif root.val:
#         return root.val
#     elif root.right:
#         return root.right
#     else:
#         return None
from typing import List
from random import randint


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sorted_array_tree_by_left(self,nums:List[int]):
        def helper(left,right):
            if left > right:  #这个地方left是数组的左边索引
                print("left,right is",(left,right))
                return None
            # always choose left middle node as a root
            p = (left+right) // 2
            print("left,p-1 is ",left,p-1)
            print("p+1,right is ",p+1,right)
            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left,p-1)
            root.right = helper(p+1,right)
            return root
        return helper(0,len(nums)-1)


    def sorted_array_tree_by_mid(self,nums:List[int]):
        def helper(left,right):
            if left > right:
                return None
            mid = (left + right ) // 2
            if (left+right) % 2:# always choose right middle node as a root
                mid = mid + 1
            root=TreeNode(nums[mid])
            root.left= helper(left,mid-1)   #mid -> left -> right
            root.right= helper(mid+1,right)   #mid -> left -> right
            return root
        return helper(0,len(nums)-1)

    class Solution:
        def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
            def helper(left, right):
                if left > right:
                    return None

                # choose random middle node as a root
                p = (left + right) // 2
                if (left + right) % 2:
                    p += randint(0, 1)

                    # inorder traversal: left -> node -> right
                root = TreeNode(nums[p])
                root.left = helper(left, p - 1)
                root.right = helper(p + 1, right)
                return root

            return helper(0, len(nums) - 1)





"""
理解这个的关键：
首先，对于左序遍历，其遍历顺序是left-> node  -> right这样的顺序(注意：这棵树是针对当前的一颗最小子树而言的)；
因为数组为有序数组，左边为left,中间为node,右边为right;
因此，可以先定义好中间值（对应根节点)，根据中间值索引再定义左右节点；而左右节点定义可参考递归同样以这种方式定义
第一步，先去找根节点node,作为数组中第一个元素；再去找该node点的left,作为数组元素的第二个元素；再找该node点的right，作为数组元素的第三个元素；
第一步中，根节点找到后，如果没有左节点元素，则跳过，去找右节点元素。

对于右节点，按照left -> node -> right这样的顺序查找，即把当前右节点当作树的left点，去找该left点的根节点作为数组元素的第四个元素，把该left点的右节点作为数组元素的第五个元素；


"""
if __name__ == '__main__':
    so = Solution()
    nums = [-2,-10,0,1]#[-10,0,1]
    # nums =  [-10,-3,0,1,2]   #[-3,-10,0,2,1]
    rst = so.sorted_array_tree(nums)
    print(rst)