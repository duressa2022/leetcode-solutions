# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_node=ListNode(head.val)
        outerPointer=result_node
        currentPointer=head.next
        while currentPointer is not None:
            newNode=ListNode(currentPointer.val)
            newNode.next=outerPointer
            outerPointer=newNode
            innerPointer=outerPointer
            while innerPointer.next is not None:
                if innerPointer.val<innerPointer.next.val:
                    temp=innerPointer.val
                    innerPointer.val=innerPointer.next.val
                    innerPointer.next.val=temp
                    innerPointer=innerPointer.next
                else:
                    break
            currentPointer=currentPointer.next
        current=outerPointer
        pre=None
        while current is not None:
            temp=current.next
            current.next=pre
            pre=current
            current=temp
        head=pre
        return head



        