# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev_linked_list(node):
            if not node:return node
            prev=None
            current=node
            while current:
                next=current.next
                current.next=prev
                prev=current
                current=next
            node=prev
            return node
        head1=rev_linked_list(l1)
        head2=rev_linked_list(l2)
        result=ListNode(0)
        current=result
        carry=0
        while head1 or head2:
            total=carry
            if head1:
                total+=head1.val
                head1=head1.next
            if head2:
                total+=head2.val
                head2=head2.next
            node=ListNode(total%10)
            carry=total//10
            current.next=node
            current=current.next
        if carry:
            current.next=ListNode(carry)
        result=result.next
        result=rev_linked_list(result)
        return result



        