# -*- coding: utf-8 -*-
# @Time : 2020/6/15 16:05
# @Author : ccs
"""

Merge Two Sorted Lists
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

参考：https://blog.csdn.net/weixin_42304045/article/details/80518128
"""
class Solution(object):
    def sorted(self,l1, l2):
        head = Node(0) ##创建一个新链表，此为头节点
        first = head #初始化已知当前新链表的值；

        #当前新链表值已知的情况下，判断当前链表值的next是谁(是链表l1还是链表,l2)；还有注意node的迭代
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next #通过这个完成链表迭代
            else:
                head.next = l1
                l1 = l1.next
            head = head.next

        #判断谁先结束，则后续就接着谁；
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1

        return first



#定义链表
class Node(object):
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)



if __name__ == '__main__':

    #初始化链表
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node1.next = node2  #链表之间连接是通过这样实现的；
    # node2.next = node3
    def printList(node):
        while node:
            print(node)
            node = node.next
    # printList(node1)

    #合并两个有序链表
    #Input: 1->2->4, 1->3->4
    #Output: 1->1->2->3->4->4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(4)
    node1.next = node2  # 链表之间连接是通过这样实现的；
    node2.next = node3

    node11 = Node(1)
    node21 = Node(3)
    node31 = Node(4)
    node11.next = node21  # 链表之间连接是通过这样实现的；
    node21.next = node31
    solu = Solution()
    node_rst = solu.sorted(node1,node11)
    print("node_rst is")
    printList(node_rst)






    """
    list_1 = ListNode()
list_1.val = 1
list_1.next = ListNode()
list_1.next.val = 2
list_1.next.next = ListNode()  #  这个地方写的很臃肿，可以直接右边初始化链表设定，左边直接等于链表就可以了；
list_1.next.next.val = 4


list_2 = ListNode()
list_2.val = 1
list_2.next = ListNode()
list_2.next.val = 3
list_2.next.next = ListNode()
list_2.next.next.val = 4

    """