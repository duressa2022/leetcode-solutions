# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap=[]
        for index,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,index,node))
        
        ans=ListNode(0)
        cur=ans
        while heap:
            val,index,node=heapq.heappop(heap)
            cur.next=node
            cur=cur.next
            if node.next:
                heapq.heappush(heap,(node.next.val,index,node.next))
        return ans.next


        