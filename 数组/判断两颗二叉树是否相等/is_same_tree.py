# -*- coding: utf-8 -*-
# @Time : 2020/6/14 11:30
# @Author : ccs
class TreeNode(object):
    def __init__(self, node):  # 列表的数据结构：[根节点，左节点，右节点]
        self.val = node[0]  # 根节点
        self.left = node[1]  # 左节点
        self.right = node[2]  # 左节点


class Solution(object):
    def isSameTree(self, p, q):
        """
        """

        def read_tree(tree, r_list):
            if tree == None:
                r_list.append('null')
            else:
                r_list.append(tree.val)
                read_tree(tree.left, r_list)
                read_tree(tree.right, r_list)
            return r_list

        r1 = read_tree(p, [])

        r2 = read_tree(q, [])
        print("r1,r2 is ", r1, r2)
        if r1 == r2:
            return True
        else:
            return False


class Solution_2(object):
    """

    """

    def isSameTree(self, p, q):
        def same_tree(p, q):
            if not p and not q:  # 两棵树均为空
                return True
            elif not p and q or not q and p:  # 两棵树只有一棵为空
                return False
            else:
                return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

        return same_tree(p, q)



if __name__ == '__main__':
    so = Solution()
    rst = so.isSameTree(TreeNode([1, 2, 3]), TreeNode([1, 2, 3]))
    print("rst is ", rst)
    #
    # rst = so.isSameTree(TreeNode([1, 2, 3],[2,3,4]), TreeNode([2, 2, 3]))
    # print("rst is ", rst)

