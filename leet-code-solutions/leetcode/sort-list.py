# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list=[]
        current=head
        while current:
            temp_list.append(current.val)
            current=current.next
        temp_list.sort()
        result=ListNode(0)
        current=result
        for number in temp_list:
            current.next=ListNode(number)
            current=current.next
        return result.next


        