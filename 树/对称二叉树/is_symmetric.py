# -*- coding: utf-8 -*-
# @Time : 2020/6/22 13:35
# @Author : ccs
"""
给定一个二叉树，检查它是否是镜像对称的。

"""
# Definition for a binary tree node.


import sys

sys.setrecursionlimit(1000000)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    这个是在比较树的结构，不用关心数值； #明明是给定的一颗二叉树；怎么输入变两颗了？？？

    观察发现：二叉树的根值都必须是一样的；因此可以把这个一个二叉树的镜像；
    必须实现：首先这两棵树的子树本身对称；其次，这两棵树本身对称；


    """
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        首先，该逻辑有漏洞；
        漏洞1：没有考虑到根节点是否相等；
        漏洞2：没有考虑点数较大时（即深度>=3时），结构的对称性：左——右；根节点；右——左
        该逻辑只适合两层以内对称完全二叉树的比较；而不适合对称不完全二叉树；

        其次，
        当树的深度>=3时，会报如下错误：
        python maximum recursion depth exceeded解决方式；
        在代码全局处加入：
        import sys
        sys.setrecursionlimit(1000000)
        但还是报错：Process finished with exit code -1073741571 (0xC00000FD)
        参考的解决方式：https://blog.csdn.net/youzhouliu/article/details/77828658



        """
        if isinstance(root,TreeNode):
            if not root.left and not root.right:
                return True
            elif root.left and root.right:
                return self.isSymmetric(root.left) and self.isSymmetric(root.right)
            else:
                return False
        else:
            return False

class Solution2:
    def isSymmetric(self, root_1: TreeNode,root_2: TreeNode) -> bool:
        if root_1.val != root_2.val:
            return False
        if  root_1.left and root_2.right:
            return self.isSymmetric(root_1.left,root_2.right)
        elif not root_1.left and not root_2.right:
            return True
        else:
            return False
"""
对比官方C++的写法：
class Solution {
public:
    bool check(TreeNode *p, TreeNode *q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        return p->val == q->val && check(p->left, q->right) && check(p->right, q->left);
    }

    bool isSymmetric(TreeNode* root) {
        return check(root, root);
    }
};



"""




if __name__ == '__main__':
    # so = Solution()
    so = Solution2()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)

    t21 = TreeNode(1)
    t22 = TreeNode(2)

    t31 = TreeNode(1)
    t32 = TreeNode(2)

    t1.left = t2
    t1.right = t3

    t2.left = t21
    t2.right = t22

    # t3.left = None
    # t3.right = t32


    rst = so.isSymmetric(t1.left,t1.right)
    print("rst is ",rst)



