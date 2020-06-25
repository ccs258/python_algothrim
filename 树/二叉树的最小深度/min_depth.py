from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_err:
    class Solution:
        def minDepth(self, root: TreeNode) -> int:
            if not root:
                return 0
            if root.left and root.right:
                return min(self.minDepth(root.left),self.minDepth(root.right))+1
            else:
                return  max(self.minDepth(root.left)+1,self.minDepth(root.right)+1)

'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

看清题目描述：对于输入[2,1]这样的数字，输出期望是2，而不是1；最小的深度是到最近叶子结点的深度，并不是到右叶子节点(为空)的深度1；！！！！注意审题。

'''
#官方解法一：递归
class Solution_final:
    def minDepth(self,root):
        if not root:
            return 0

        children = [root.left,root.right]
        if not any(children):
            return 1
        min_depth = float("inf")
        for c in children:
            if c:
                min_depth = min(self.minDepth(c),min_depth)
                return min_depth+1

"""
复杂度分析

时间复杂度：我们访问每个节点一次，时间复杂度为 O(N)O(N) ，其中 NN 是节点个数。
空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 NN （树的高度）次，因此栈的空间开销是 O(N)O(N) 。但在最好情况下，树是完全平衡的，高度只有 \log(N)log(N)，因此在这种情况下空间复杂度只有 O(\log(N))O(log(N)) 。

def any(*args, **kwargs): # real signature unknown
    Return True if bool(x) is True for any x in the iterable.
    If the iterable is empty, return False.
"""

##思路对比
"""
我的思路：
（0）当根节点为空时，返回0
（1）当左右子树都存在时，求树的最小深度，是去分别求左右子树的最小深度；
（2）左右子树都存在时，递归遍历；
（3）左右子树只有一方存在时，取最大的那方的深度作为最小深度（因为题目要求最小深度是到最近叶子结点的距离）

"""
#方法二：深度优先搜索迭代
"""
我们可以利用栈将上述解法中的递归变成迭代。

想法是对于每个节点，按照深度优先搜索的策略访问，同时在访问到叶子节点时更新最小深度。

我们从一个包含根节点的栈开始，当前深度为 1 。

然后开始迭代：弹出当前栈顶元素，将它的孩子节点压入栈中。当遇到叶子节点时更新最小深度。

"""
class Solution:
    """
    #方法二：深度优先搜索迭代
    栈：先进后出；
    """
    def minDepth(self,root):
        if not root:
            return 0
        else:
            stack,min_depth = [(1,root),],float("inf") #构建遍历的栈--深度优先的方向以及结果
        while stack:
            depth,root = stack.pop()
            children = [root.left,root.right]
            if not any(children):
                min_depth = min(depth,min_depth)
            for c in children:
                if c:
                    stack.append((depth+1,c))
        return min_depth


class Solution_2:
    """
    #方法三：广度优先搜索迭代
    队列：先进先出


    深度优先搜索方法的缺陷是所有节点都必须访问到，以保证能够找到最小深度。因此复杂度是 O(N)O(N) 。

    一个优化的方法是利用广度优先搜索，我们按照树的层去迭代，第一个访问到的叶子就是最小深度的节点，这样就不用遍历所有的节点了。

    """
    def minDepth(self,root):
        if not root:
            return 0
        else:
            node_queue = deque([(1,root),])
        while node_queue:
            depth,root = node_queue.popleft()
            children = [root.left,root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_queue.append((depth+1,c))

    """
    复杂度分析
    时间复杂度：最坏情况下，这是一棵平衡树，我们需要按照树的层次一层一层的访问完所有节点，除去最后一层的节点。这样访问了 N/2N/2 个节点，因此复杂度是 O(N)O(N)。
    空间复杂度：和时间复杂度相同，也是 O(N)O(N)。
    
     def popleft(self, *args, **kwargs): # real signature unknown
        Remove and return the leftmost element. 
    
    类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)    
    
    返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。

    Deque队列是由栈或者queue队列生成的（发音是 “deck”，”double-ended queue”的简称）。Deque 支持线程安全，内存高效添加(append)和弹出(pop)，从两端都可以，两个方向的大概开销都是 O(1) 复杂度。
    
    虽然 list 对象也支持类似操作，不过这里优化了定长操作和 pop(0) 和 insert(0, v) 的开销。它们引起 O(n) 内存移动的操作，改变底层数据表达的大小和位置。
    
    如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。限定长度deque提供类似Unix filter tail 的功能。它们同样可以用与追踪最近的交换和其他数据池活动。
    
    双向队列(deque)对象支持以下方法：
    
    append(x)
    添加 x 到右端。
    
    appendleft(x)
    添加 x 到左端。
    
    pop()
    移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。

    popleft()
    移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。

    参考：    https://docs.python.org/zh-cn/3/library/collections.html
    """


