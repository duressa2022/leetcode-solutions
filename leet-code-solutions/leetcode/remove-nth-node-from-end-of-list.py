# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        interval=1
        if fast.next is None and n==1:
            return head.next
        elif fast.next is None and n==0:
            return head
        while fast and  fast.next!=None:
            if interval<n+1:
                interval+=1
                fast=fast.next
            else:
                slow=slow.next
                fast=fast.next
        if fast.next is None and interval<n+1:
            return head.next
        slow.next=slow.next.next
        return head


        