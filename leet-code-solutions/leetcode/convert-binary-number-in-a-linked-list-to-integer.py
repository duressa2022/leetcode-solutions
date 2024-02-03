# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #calculate length is the linkedlist
        lengthDigit=0
        current=head
        while current is not None:
            lengthDigit+=1
            current=current.next
        #work on the conversion of binary to decimal
        result=0
        power=lengthDigit-1
        current=head
        #start to calculate the number
        while current is not None:
            #calculate the value by using given property
            result+=(current.val)*2**power
            #update power and pointer
            power=power-1
            current=current.next
        #return the result
        return result
        