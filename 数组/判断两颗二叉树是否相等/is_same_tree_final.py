# -*- coding: utf-8 -*-
# @Time : 2020/6/14 12:21
# @Author : ccs
# -*- coding:utf-8 -*-
class BiTNode(object):
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


'''
方法功能：判断两棵二叉树是否相等
参数：root1与root2分别为两棵二叉树的根节点
返回值：如果两棵树相等则返回true，否则返回false
'''


def isEqual(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root1 != None and root2 == None:
        return False
    if root1.data == root2.data:
        return isEqual(root1.lchild, root2.lchild) and isEqual(root1.rchild, root2.rchild)
    else:
        return False


# def constructTree():
#     root = BiTNode()
#     node1 = BiTNode()
#     node2 = BiTNode()
#     node3 = BiTNode()
#     node4 = BiTNode()
#     root.data = 6
#     node1.data = 3
#     node2.data = -7
#     node3.data = -1
#     node4.data = 9
#     root.lchild = node1
#     root.rchild = node2
#     node1.lchild = node3
#     node1.rchild = node4
#     node2.lchild = node2.rchild = node3.lchild = node3.rchild = node4.lchild = node4.rchild = None
#     return root

def constructTree_01():
    root = BiTNode()
    node1 = BiTNode()
    node2 = BiTNode()
    root.data = 6
    root.lchild = node1
    root.rchild = node2
    node1.data = 3
    node2.data = 2
    node1.lchild = None
    node1.rchild = None
    node2.lchild = None
    node2.rchild = None
    return root


# def constructTree_02():
#     """
#     这种写法不对，因为左右子节点默认也是一棵树（通用性，多层级树的考虑），只不过左右子节点的子节点为None而已；否则会破坏程序的通用性；
#
#
#     File "C:/Users/ccs/PycharmProjects/python-算法/数组/判断两颗二叉树是否相等/is_same_tree_final.py", line 27, in isEqual
#     return isEqual(root1.lchild, root2.lchild) and isEqual(root1.rchild, root2.rchild)
#   File "C:/Users/ccs/PycharmProjects/python-算法/数组/判断两颗二叉树是否相等/is_same_tree_final.py", line 26, in isEqual
#     if root1.data == root2.data:
# AttributeError: 'int' object has no attribute 'data'
#
#     """
#     root = BiTNode()
#     root.data = 6
#     root.lchild = 1
#     root.rchild = 3
#     return root

def constructTree_02():
    root = BiTNode()
    node1 = BiTNode()
    node2 = BiTNode()
    root.data = 6
    root.lchild = node1
    root.rchild = node2
    node1.data = 3
    node2.data = 2
    node1.lchild = None
    node1.rchild = None
    node2.lchild = None
    node2.rchild = None
    return root

if __name__ == "__main__":
    root1 = constructTree_01()
    root2 = constructTree_02()
    equal = isEqual(root1, root2)
    if equal:
        print("两棵树相等！")
    else:
        print("两棵树不相等！")
