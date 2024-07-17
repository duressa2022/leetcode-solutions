# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(head):
            if not head or not head.next:
                return head
            mid=self.compute_mid(head)
            temp=mid.next
            mid.next=None
            left=merge_sort(head)
            right=merge_sort(temp)
        
            return self.merge(left,right)
        if not head or not head.next:
            return head
        return merge_sort(head)
    
    def compute_mid(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def merge(self,head1,head2):
        ans=ListNode(0)
        cur1,cur2,cur=head1,head2,ans
        while cur1 and cur2:
            if cur1.val<cur2.val:
                cur.next=cur1
                cur1=cur1.next
                cur=cur.next
            else:
                cur.next=cur2
                cur2=cur2.next
                cur=cur.next
        if cur1:
            cur.next=cur1
        if cur2:
            cur.next=cur2
        return ans.next
        