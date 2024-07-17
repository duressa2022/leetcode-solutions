# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length,tail=self.get_length(head)
        if not head or not head.next or k%length==0:
            return head

        node=self.get_Nth_node(head,length-k%length)
        tail.next=head
        temp=node.next
        node.next=None
        head=temp

        return head



    def get_length(self,head):
        cur,length=head,1
        while cur and cur.next:
            length+=1
            cur=cur.next
        return length,cur
    def get_Nth_node(self,head,n):
        cur,counter=head,1
        while cur:
            if counter==n:
                return cur
            counter+=1
            cur=cur.next
        return  None

        