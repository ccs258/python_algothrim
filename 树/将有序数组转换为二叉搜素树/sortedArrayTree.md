#遍历树的方法。DFS：先序遍历，中序遍历，后序遍历；BFS。
遍历树的两种通用策略：

#深度优先遍历（DFS）

    这种方法以深度 depth 优先为策略，从根节点开始一直遍历到某个叶子节点，然后回到根节点，在遍历另外一个分支。
    根据根节点，左孩子节点和右孩子节点的访问顺序又可以将 DFS 细分为先序遍历 preorder，中序遍历 inorder 和后序遍历 postorder。

#广度优先遍历（BFS）

    按照高度顺序，从上往下逐层遍历节点。
    先遍历上层节点再遍历下层节点。
    
    下图中按照不同的方法遍历对应子树，得到的遍历顺序都是 1-2-3-4-5。根据不同子树结构比较不同遍历方法的特点。
    
    
    
    将有序数组转换为二叉搜索树的结果为什么 不唯一 ？
    众所周知，二叉搜索树的中序遍历是一个升序序列。
    
    将有序数组作为输入，可以把该问题看做 根据中序遍历序列创建二叉搜索树。
    
    这个问题的答案唯一吗。例如：是否可以根据中序遍历序列和二叉搜索树之间是否一一对应，答案是 否定的。
    
    下面是一些关于 BST 的知识。
    中序遍历不能唯一确定一棵二叉搜索树。
    先序和后序遍历不能唯一确定一棵二叉搜索树。
    先序/后序遍历和中序遍历的关系：
    inorder = sorted(postorder) = sorted(preorder)，
    中序+后序、中序+先序可以唯一确定一棵二叉树。
    
    因此，“有序数组 -> BST”有多种答案。
    
    
    
    因此，添加一个附件条件：树的高度应该是平衡的、例如：每个节点的两棵子树高度差不超过 1。
    
    这种情况下答案唯一吗？仍然没有。
    
    高度平衡意味着每次必须选择中间数字作为根节点。这对于奇数个数的数组是有用的，但对偶数个数的数组没有预定义的选择方案。
    
    对于偶数个数的数组，要么选择中间位置左边的元素作为根节点，要么选择中间位置右边的元素作为根节点，不同的选择方案会创建不同的平衡二叉搜索树。方法一始终选择中间位置左边的元素作为根节点，方法二始终选择中间位置右边的元素作为根节点。方法一和二会生成不同的二叉搜索树，这两种答案都是正确的。

#参考
    本题目参考：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-15/
    理解参考：https://zhuanlan.zhihu.com/p/24986203
    
    

