# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode(0)
        current=result
        rem=0
        while l1 or l2:
            sumResult=rem
            if l1:
                sumResult+=l1.val
                l1=l1.next
            if l2:
                sumResult+=l2.val
                l2=l2.next
            node=ListNode(sumResult%10)
            rem=sumResult//10
            current.next=node
            current=node
        if rem!=0:
            current.next=ListNode(rem)
        return result.next


        