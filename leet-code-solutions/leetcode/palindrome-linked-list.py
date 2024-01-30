# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        generated=[]
        current=head
        while current is not None:
            generated.append(current.val)
            current=current.next
        left,right=0,len(generated)-1
        while left<right:
            if generated[left]!=generated[right]:
                return False
            left=left+1
            right=right-1
        return True
        