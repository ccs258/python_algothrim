# -*- coding: utf-8 -*-
# @Time : 2020/6/20 18:56
# @Author : ccs
"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution_err:
    """
    错误写法
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p.val != q.val or p.left != q.left or p.right != q.right:
            return False
        else:
            return True

"""
我的写法的漏洞：
要注意到如果left,right本身也是树结构，其有值；
看题目要求：两棵树相同的定义为：在结构上相同，并且节点具有相同的值，则认为它们是相同的。
因此可写一个函数：比较树的值是否相同(树的val值)，以及是否都存在左右节点（用对象是否为None即可），即可;

通过官方提交的可以看出，p,q在注释里面申明类型:type p: TreeNode；:type q: TreeNode即可，需要把TreeNode类取消注释；

"""

"""
官方的写法
"""
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q: #这个地方比较的是树结构是否相同，即是否都存在，
            return True
        # one of p and q is None
        if not q or not p:   #这个地方比较的是树结构是否相同，即是否有一个不存在，
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

if __name__ == '__main__':
    so = Solution()
    p = TreeNode(1,2,3)
    q = TreeNode(1,2,)
    rst = so.isSameTree(p,q)
    print("rst is ",rst)