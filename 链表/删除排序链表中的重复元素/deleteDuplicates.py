# -*- coding: utf-8 -*-
# @Time : 2020/6/19 17:10
# @Author : ccs
# Definition for singly-linked list.

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    """
    官方
    #正确理解（0）：此处first是一个节点指针；每一次循环节点指针都会更新
    #正确理解（1）：如果当前节点指针与下一个节点指针值不同，则不做任何链表改变操作，节点指针+1
    #正确理解（2）：如果当前节点指针与下一个节点指针值相同，不做任何链表改变操作，将下一节点指针替换会下下一个节点指针；

    first  = head 赋值给他：这个地方是把head链表的指针赋值给他，
    可以看出，链表的指针变量，还是链表，链表的指针变量指的内容以及指针变量的顺序会改变 head内容

    #else逻辑里面first = first.next
    #当前这个first已经走到head里面两个值不相等的地方了（first.next.val != first.val），因此可继续遍历向下走，不用改变内容；

    #理解，链表的值是不能改变的，只要含有next就是指针；可以通过改变next的指向来改变链表内容

    由于链表的特性（next指针），知道了头指针，那么整个链表的元素都能够被访问，也就是说头指针是必须存在的。
    参考：https://blog.csdn.net/mcgrady_tracy/article/details/32130421

    first刚开始的指针
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first  = head #这个地方链表的内存地址都指向一个地方，因此内容一样；注意链表在内存当中的存储形式；链表表头决定内存的位置
        while(first != None and first.next != None):
            if first.next.val == first.val:
                # 疑问；这个地方first改变，会导致head也跟着变化，但是为什么下面else的地方，first变化，head不跟着变化；
                first.next = first.next.next #正确理解（2）：如果当前节点指针与下一个节点指针值相同，不做任何链表改变操作，将下一节点指针替换会下下一个节点指针；
                #这个地方就相当于与是跳过了first.next这个节点；图像化思维；直接指向first.next。next
            else:
                first = first.next   #正确理解（1）：如果当前节点指针与下一个节点指针值不同，则不做任何链表改变操作，节点指针正常遍历
                #第一版本理解有误：这个地方相当于重新生成了一个新的链表，其内存地址是不一样的；因此，切记这样写的目的会导致重新生成一个新的链表
                #正确理解（0）：此处first是一个节点指针；每一次循环节点指针都会更新

                #当前这个first已经走到head里面两个值不相等的地方了（first.next.val != first.val），因此可继续遍历向下走，不用改变内容；


        return head

class Solution_err:
    """

    注意：将first = first.next会改变当前first前面的值；

    """
    def deleteDuplicates_err(self, head: ListNode) -> ListNode:
        first = ListNode(0)
        tmp = ListNode(0)

        while(head != None):
            if head.val !=  head.next.val:
                first.val = head.val
                first.next = tmp
                first = first.next   #这样写错误，会生成新的链表
            head = head.next #这样写错误，会生成新的链表
        return first

    def deleteDuplicates(self, head_in: ListNode) -> ListNode:
        head = head_in
        first = ListNode(0)  #终于知道为什么声明的之后，初始化一个0值了，其实就是初始化一个内存地址；
        tmp = ListNode(0)
        while (head.next != None and head.next.next != None):
            if head.next.val == head.next.next.val or head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
            head_in.next = head

            #     first = first.next  # 这样写错误，会生成新的链表
            # head = head.next  # 这样写错误，会生成新的链表
        return head_in



if __name__ == '__main__':
    so = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(2)
    l1.next = l2
    l2.next = l3
    l3.next = None

    rst = so.deleteDuplicates(l1)
    for i in range(2):
        print(rst.val)
        rst = rst.next

"""
程序理解：当输入链表为1,2,2时；当迭代到第2个元素的时候，按道理first重新生成了；id(first) == id(head)的结果为False;
那为什么head的程序却变了；
"""

