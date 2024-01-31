# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left=ListNode(0)
        leftPointer=left
        right=ListNode(0)
        rightPointer=right
        current=head
        while current is not None:
            tempValue=current.val
            if tempValue<x:
                leftPointer.next=ListNode(tempValue)
                leftPointer=leftPointer.next
            else:
                rightPointer.next=ListNode(tempValue)
                rightPointer=rightPointer.next
            current=current.next
        leftPointer.next=right.next
        head=left.next
        return head


        