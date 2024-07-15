# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        while slow:
            fast=slow
            while fast and fast.val==slow.val:
                fast=fast.next
            slow.next=fast
            slow=slow.next
        return head