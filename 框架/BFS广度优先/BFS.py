import queue


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def solution(start, target):
    q = queue.Queue()
    depth = 1  # min_depth = 0
    step = 0
    root = TreeNode()
    while (root != None):
        if root.left == None and root.right == None:
            return depth
        # if root.val == target:  #乱了，我们目标是找最短深度
        #     return depth

        if root.left != None:
            q.put(root.left)
        if root.right != None:
            q.put(root.right)


def minDepth(root: TreeNode):
    if root == None:
        return 0
    q = queue.Queue()
    q.put(root)  #把root推到队列中
    depth = 1 #有根节点的时候，本身数量就为1层了；
    while (q):  # 用队列作为循环
        sz = q.qsize()
        i = 0
        while (i < sz): #用当前队列的元素，向周围扩散；根节点计算完之后，向左右节点扩散；
            #但由于是队列，因此左右节点扩散之后队列是先进先出，后进后出，会是按层（面）计算，而不是按深度（线）计算；
            cur = q.get() #获取当前队列中的长度
            if cur.left == None and cur.right == None:
                return depth
            if cur.left != None:
                q.put(cur.left)
            if cur.right != None:
                q.put(cur.right)
            i= i + 1
        depth = depth + 1  #本行对应上述其他行内容对应外层的队列的一次循环；没循环一次，对应的是做的当前层的计算；
        #以root根节点为例，本行运行之后表示遍历到根节点的左右节点；可以看出，每次都是面遍历；
    return depth

