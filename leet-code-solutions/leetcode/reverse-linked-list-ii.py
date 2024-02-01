# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:return head
        dummy_node=ListNode(0)
        dummy_node.next=head
        head=dummy_node
        left_head_current=head
        left_most_node=head
        right_most_node=head
        left_index=0
        right_index=0
        while left_most_node is not None and left_index<left-1:
            left_index=left_index+1
            left_most_node=left_most_node.next
        while right_most_node is not None and right_index<right:
            right_index=right_index+1
            right_most_node=right_most_node.next
        leftTracker=left_most_node.next
        left_most_node.next=None
        rightTracker=right_most_node.next
        right_most_node.next=None
        current=leftTracker
        pre=None
        while current is not None:
            temp=current.next
            current.next=pre
            pre=current
            current=temp
        leftTracker=pre
        left_most_node.next=leftTracker
        current=head
        while current.next is not None:
            current=current.next
        current.next=rightTracker
        return head.next


        



        

        
        