# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        head=ListNode(0)
        current=head
        while head1 and head2:
            if head1.val<head2.val:
                current.next=ListNode(head1.val)
                head1=head1.next
            else:
                current.next=ListNode(head2.val)
                head2=head2.next
            current=current.next
        while head1:
            current.next=ListNode(head1.val)
            head1=head1.next
            current=current.next
        while head2:
            current.next=ListNode(head2.val)
            head2=head2.next
            current=current.next
        return head.next

        