"""
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，
每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""
nums = [3,2,3,None,3,None,1]  # [2,3,2]
mem = {}


def solution(root):
    if not root:
        return 0
    if mem.get(root):  #加一个对树的缓存
        return mem.get(root)
    # 当前节点抢，然后去下下家
    left_val = 0
    right_val = 0
    if root.left:
        left_val = solution(root.left.left) + solution(root.left.right)
    if root.right:
        right_val = root.val + solution(root.right.left) + solution(root.right.right)
    do_it = root.val + left_val + right_val

    # 当前节点不抢，去下家
    not_do = solution(root.left) + solution(root.right)
    res = max(do_it, not_do)  # 最优的是选取当前节点抢不抢的最大值，注意当前节点抢不抢的值不只是包含当前节点的值是否取，还关系到后面的抢的值；是自顶向下的；
    mem[root] = res
    return res


def solution_1(nums):
    """
    首尾相连，因为头部0与尾部元素索引len(num)-1相邻，因此，nums中能遍历的元素分为两类：
    证明要么包含头：即从0开始（包含头）到len(nums)-2（尾部为倒数第二位）；要么包含尾len(nums)-1，从1开始（不包含头）到len(nums)-1（即最后一位）

    """
    rst = max(solution(0, nums[:len(nums) - 1]), solution(1, nums[:len(nums)]))

    return rst


if __name__ == '__main__':
    rst = solution_1(nums)
    print("rst is ", rst)
