# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set=set()
        current=head
        while current!=None:
            if current not in hash_set:
                hash_set.add(current)
            else:
                return True
            current=current.next
        return False
