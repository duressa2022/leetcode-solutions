# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #create dummy node
        result=ListNode(0)
        #track the node 
        tracker=result
        #create pointer to the head
        current=head
        while current is not None:
            #check the conditions
            if current.val!=val:
                #create the new node and assign tracker to track the node
                tracker.next=ListNode(current.val)
                tracker=tracker.next
            #update the current node
            current=current.next
        #update the head of the new node
        head=result.next
        #return head of the node
        return head

        