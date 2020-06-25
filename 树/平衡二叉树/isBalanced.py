# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced_sub(self, root: TreeNode) -> int:
        """

        """
        if not root:
            return 0
        if not root.left and not root.right :
            return 0
        elif root.left and root.right:
            return abs(self.isBalanced_sub(root.left) - self.isBalanced_sub(root.right))
        else:
            return self.isBalanced_sub(root.right)+1  if not root.left else self.isBalanced_sub(root.left)+1

    def isBalanced(self,root: TreeNode) -> bool:
        """


        """
        print("self.isBalanced(root) is ",self.isBalanced_sub(root))
        if self.isBalanced_sub(root) <= 1:
                return True
        else:
                return False


#官方解法一---自顶向下，计算子节点高度存在冗余，靠近最深层的子树部分会被计算多次；
class SolutionFinal:
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)


#官方解法二---自底向上的递归

class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:  #根节点
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left) #计算当前左子树的左右节点(及可能左右节点分别的左右节点---从最外层到最底层子树)是否平衡以及子树的高度
        if not leftIsBalanced:  #左子树不平衡，直接返回
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:  #右子树不平衡，直接返回
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


"""
方法二：自底向上的递归
思路

方法一计算 \texttt{height}height 存在大量冗余。每次调用 \texttt{height}height 时，要同时计算其子树高度。但是自底向上计算，每个子树的高度只会计算一次。可以递归先计算当前节点的子节点高度，然后再通过子节点高度判断当前节点是否平衡，从而消除冗余。

算法

使用与方法一中定义的 \texttt{height}height 方法。自底向上与自顶向下的逻辑相反，首先判断子树是否平衡，然后比较子树高度判断父节点是否平衡。算法如下：

检查子树是否平衡。如果平衡，则使用它们的高度判断父节点是否平衡，并计算父节点的高度。



"""
"""
思考勘误：
题目描述：
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

An empty tree has height -1
An empty tree satisfies the definition of a balanced tree
Check if subtrees have height within 1. If they do, check if the subtrees are balanced

存在的问题：
定义递归初始条件，左右子树的高度差不超过1；假设现在是一个最简单的二叉树，求出这颗二叉树左节点高度和右节点高度，做差取绝对值<1,既满足平衡；
如果树不存在(root为null)，在平衡；
其他情况，分别对左子树求左子树是否平衡 && 右子树是否平衡；


我的思考角度：
纠结于左右子树的高度，可以单独把这个逻辑拎出来，单独处理，不要糅合到其他初始化和其他情况的逻辑中去。
单独处理，可以适用于所有的子树。并且注意对树的高度的理解，当前节点的树高度：以当前节点为根节点，求左子树和右子树高度，取其中最高的作为当前节点的高度
还有对于递归的初始条件不是很有把握；对其他情况的写法不是很有信心；可以试着推演下；先局部再整体（self.isBalanced(root.left) and self.isBalanced(root.right)），
对于递归而言，刚开始先分别计算最小子树，他回溯的时候会去判断总体的左右子树是否都满足平衡；


总结：通常来说，递归里面初始条件树的话，就是根节点为null,以及左右节点的计算；如果你写了超过2个以上的if...else...，可能表明代码臃肿了。

一般来说，对于那种左右节点为空的，可以通过根节点求最大把他们合并，即我只求当前根节点的高度。
"""
if __name__ == '__main__':
    so = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)

    t21 = TreeNode(3)
    t22 = TreeNode(3)

    t31 = TreeNode(4)
    t32 = TreeNode(4)

    t1.left = t2
    t1.right = t3

    t3.left = None
    t3.right =  None

    t2.left = t21
    t2.right =  t22

    t21.left = t21
    t21.right = t21





    rst = so.isBalanced(t1)
    print("rst is ",rst)

"""
[Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
"""
