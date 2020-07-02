# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    pre = None
    cur = head
    def reverseList(self, head: ListNode) -> ListNode:

        tmp_node = cur.next
        cur.next = pre
        pre = cur
        cur = tmp_node

class SolutionFinal:
    def reverseList(self,head:ListNode):
        pre = None
        curr = head
        while(curr != None):
            nextTemp = curr.next
            curr.next = pre
            pre = curr
            curr = nextTemp
        return pre



"""
参考官方的文档：
要想想链表反序：不要纠结于链表里面的val,其实你想想链表里面的val只是方便人看，真正关心的最原子的操作时链表整个对象；现在要翻转的是链表。
因此，会有几个要素变量：当前链表，当前链表的前一链表，下一个链表；
实现的功能：将当前链表指向当前链表的前一链表；
当前链表更新为当前链表的下一链表； #需要借助一个中间变量
当前链表的前一链表更新为当前链表;

####注意的点
遍历链表从当前链表节点判断，依次替换为.next，再计算；
要注意最终返回的是头链表指针；
"""