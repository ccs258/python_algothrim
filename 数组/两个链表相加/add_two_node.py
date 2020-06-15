# -*- coding: utf-8 -*-
# @Time : 2020/6/15 17:54
# @Author : ccs
"""

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
#定义链表
class Node(object):
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

    def addTwoNumbers(self, l1, l2):
        head = Node(0)  # 头结点，无存储，指向链表第一个结点
        node = head  # 初始化链表结点
        carry = 0  # 初始化 进一 的数
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry  # 对每一位求和
            carry = sum // 10  # 地板除，求进一（其为0或1） #整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。
            node.next = Node(sum % 10)  # 取余数，求本位结点
            if l1:  # 求空否，防止出现无后继结点
                l1 = l1.next
            if l2:  # 同上
                l2 = l2.next
            node = node.next  # 更新指针
        if carry != 0:  # 验证最后一位相加是否需 进一
            node.next = Node(1)
        return head.next  # 返回头结点的下一个结点，即链表的第一个结点


    def add_two_node(self,l1,l2):
        """
        总结：if条件写太多，思考是不是反向写一个简单的，包含所有情况的，只是在内部做一点判断；
        """
        rst = Node(0)
        carry = 0
        first = rst
        while(l1 != None and l2 != None):
            rst.val = (l1.val+l2.val+carry)%10
            rst.next = Node(rst.val)
            if int((l1.val+l2.val)/10) == 0:
                carry = 0
            else:
                carry = 1
            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 == None:
                rst.next = None
            elif l1== None and l2 != None:
                rst.next = l2
            elif l1 !=None and l2 == None:
                rst.next = l1
            rst = rst.next


        return first

    def printList(self,node):
        while node:
            print(node)
            node = node.next
if __name__ == '__main__':
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(3)
    node1.next = node2  # 链表之间连接是通过这样实现的；
    node2.next = node3

    node11 = Node(5)
    node21 = Node(6)
    node31 = Node(4)
    node11.next = node21  # 链表之间连接是通过这样实现的；
    node21.next = node31
    solu = Node()
    node_rst = solu.add_two_node(node1, node11)
    print("node_rst is")
    solu.printList(node_rst)

    node_rst = solu.addTwoNumbers(node1, node11)
    print("node_rst is")
    solu.printList(node_rst)

