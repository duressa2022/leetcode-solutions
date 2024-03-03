# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        linked_list=[]
        current=head
        while current:
            linked_list.append(current.val)
            current=current.next
        result=[0]*len(linked_list)
        stack=[]
        for i,value in enumerate(linked_list):
            while stack and linked_list[stack[-1]]<value:
                result[stack[-1]]=value
                stack.pop()
            stack.append(i)
        return result

        