# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def solver(prev,cur):
            if not cur:
                return prev
            next_node=cur.next
            cur.next=prev
            return solver(cur,next_node)
            

        return solver(None,head) if head and head.next else head
        