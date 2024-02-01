# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        slow=node
        fast=node.next
        while fast and fast!=None:
            temp=slow.val
            slow.val=fast.val
            fast.val=temp
            slow=slow.next
            fast=fast.next
        current=node
        while current.next.next is not None:
            current=current.next
        current.next=None


        