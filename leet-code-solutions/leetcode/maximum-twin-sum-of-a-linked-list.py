# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_result=-float("inf")
        linked_list=[]
        current=head
        while current:
            linked_list.append(current.val)
            current=current.next
        left,right=0,len(linked_list)-1
        while left<right:
            max_result=max(max_result,linked_list[left]+linked_list[right])
            left=left+1
            right=right-1
        return max_result


        