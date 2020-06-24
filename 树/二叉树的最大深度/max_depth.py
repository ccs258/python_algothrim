# -*- coding: utf-8 -*-
# @Time : 2020/6/22 20:00
# @Author : ccs
# Definition for a binary tree node.
"""
二叉树深度的定义

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return  2+max(self.maxDepth(root.left),self.maxDepth(root.right))
        if root.left:
            return 2 + self.maxDepth(root.left)
        if root.right:
            return 2 + self.maxDepth(root.right)

#官方解答
class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            print("left_height is ",left_height)
            right_height = self.maxDepth(root.right)
            print("right_height is ",right_height)

            return max(left_height,right_height)+1

"""
对比官方的写法，我的思路存在的问题：
（1）首先对递归返回情况理解不深，到底是返回0，还是返回1；应当理解：最基本的单元情况下返回的值，什么是最基本的单元（不用考虑其他需要递归条件考虑的部分，
即if里面条件不含递归变量，结果即可直接返回：即if里面是not root这种形式，而不是not root.left等这种，这个可以当作递归条件再度调用时计算）；

（2）理解递归函数的调用顺序：
对于已知二叉树输入为：[1,2,3,null,2]，又由于二叉树的深度为根节点到最远叶子节点的最长路径上的节点数；因此该深度为3，其调用计算过程为：
left_height is  0
left_height is  0
right_height is  0
right_height is  1
left_height is  2
left_height is  0
right_height is  0
right_height is  1
rst is  3

可以看出，大致过程是：maxDepth（t1）——> maxDepth（t1.left也即t2树节点）——> maxDepth（t2.left）——>
(迭代完从根节点t1.left再到t2左节点为None,此内层部分执行完有结果返回，因此顺序执行打印)——>(打印一次子结果：left_height is  0)
——>maxDepth（t2.right有值）——>maxDepth（t2.right.left为None）——>（打印一次子结果：left_height is  0）——>

maxDepth（t2.right.right为None）——>（打印一次子结果：right_height is  0）
——>左边部分的left_height计算完了——>嵌套计算self.maxDepth(root.right) = max(self.maxDepth(root.right。left),self.maxDepth(root.right.right))+1
root.right。left为None,root.right。right也为None,因此，self.maxDepth(root.right)的结果等与1，得到结果，计算完成（不是return，是嵌套里面return，最外层并没有
return,只是将内层return的结果加起来了而已），此时right_height为1，因此顺序执行，继续打印——>right_height is  1;

maxDepth（t2.left）的结果，等于每一层的左右节点嵌套结果计算，打印多少次就对应有多少层，可以看出打印了2次，因此，左边的节点深度即为2；

maxDepth（t1）——> maxDepth（t1.left也即t2）——> maxDepth（t2.right也即t3树节点）——>
maxDepth（t3.left)由于t3的左节点为None,此内层部分执行完有结果返回，因此顺序执行打印)——>(打印一次子结果：left_height is  0)
——>maxDepth（t3.right)由于t3的左节点为None,此内层部分执行完有结果返回，因此顺序执行打印)——>(打印一次子结果：right_height is  0)
——>嵌套计算self.maxDepth（t2.right也即t3树节点） = max(self.maxDepth(t3.left),self.maxDepth(t3.right))+1——>
得到结果，计算完成（不是return，是嵌套里面return，最外层并没有
return,只是将内层return的结果加起来了而已），此时right_height为1，因此顺序执行，继续打印——>right_height is  1;

最后最终的结果，则是max(left_height,right_height)+1的最外层left_height，right_height带入进去求得的值3；


总结：可以看出，递归的过程是：
按顺序执行逻辑，
对于第一个左边节点递归调用：第一次进入嵌套后，依据代码顺序再次执行逻辑，如果有嵌套，则再继续；直到最后输出内层嵌套结果；
再输出倒数第二层结果；

对于第二个右边节点递归调用：顺序执行到对于右边节点，对于右边节点，再重复按最初遍历左节点开始的时候那样，
按顺序执行逻辑，第一次进入嵌套后，依据代码顺序再次执行逻辑，如果有嵌套，则再继续；到最后输出内层嵌套结果；
再输出倒数第二层结果；

最终结果：对上述递归结果进行计算求得最终的值：max(2,1)+1=3；

即：递归是遇到递归则会先把当前递归先计算完，得到结果后，在顺序执行下一个递归；这两个递归之间的联系，其实是没有联系的，可以看出是独立的；
最终是根据我们的业务逻辑来确定要根据这两递归怎么计算得到最终结果；

两递归怎么计算得到最终结果?---------确定方式是，用最初始的条件最简单的情况，即初始化状态的形式看看结果与条件的关系，比如当root为None的时候，
直接确定结果为0，不需要递归；但root为最小二叉树时，深度为2，对应根节点到最长子节点的节点数为2，其应该是max(左子节点深度（为None---没有子树）,右子节点深度（为None---没有子树））+ 1
= max(1,1）+ 1 ；可以看出:左子节点深度（右子节点深度）为1，只要root为None,深度即为0即为max(0+0）+ 1



"""


if __name__ == '__main__':
    so = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)

    # t21 = TreeNode(1)
    # t22 = TreeNode(2)
    #
    # t31 = TreeNode(1)
    # t32 = TreeNode(2)

    t1.left = t2
    t1.right = t3

    t2.left = None
    t2.right = TreeNode(2)
    #
    # t3.left = None
    # t3.right = None
    rst = so.maxDepth(t1)
    print("rst is ",rst)