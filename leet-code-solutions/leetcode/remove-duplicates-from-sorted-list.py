# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode(0)
        indictor=result
        linkedSet=set()
        current=head
        while current!=None:
            if current.val not in linkedSet:
                node=ListNode(current.val)
                indictor.next=node
                indictor=node
                linkedSet.add(current.val)
            current=current.next
        return result.next


        