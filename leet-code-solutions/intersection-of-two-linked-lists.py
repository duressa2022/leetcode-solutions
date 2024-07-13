# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        hashset=set()
        cur=headA

        while cur:
            hashset.add(cur)
            cur=cur.next

        cur=headB
        while cur:
            if cur in hashset:
                return cur
            cur=cur.next

        return None
        