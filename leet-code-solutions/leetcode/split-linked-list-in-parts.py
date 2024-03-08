# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length,current=0,head
        while current:
            length+=1
            current=current.next
        _length,length_=length//k,length%k
        result=[]
        current=head
        for i in range(k):
            result.append(current)
            temp=0
            if length_:
                temp=1
            for i in range(_length-1+temp):
                if not current:
                    break
                current=current.next
            if length_:
                length_-=1
            else:
                length_-=0
            if current:
                temp=current.next
                current.next=None
                current=temp
        return result


            
        