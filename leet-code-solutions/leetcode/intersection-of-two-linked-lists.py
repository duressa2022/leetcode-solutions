# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #create hashset to store the unique values of the linkedlist
        linkedSet=set()
        #create two pointer to track both heads
        currentA=headA
        currentB=headB
        #move through the linkedlist 
        while currentA is not None or currentB is not None:
            #check wether node is in hashset
            if currentA not in linkedSet and currentA is not None:
                #put the node into the hashset
                linkedSet.add(currentA)
                #update the node based on the condition
                currentA=currentA.next
            else:
                #if current node is in the hashset return node
                if currentA is not None:
                    return currentA
            #check wether the node is in hashset
            if currentB not in linkedSet and currentB is not None:
                #add node into the hashset
                linkedSet.add(currentB)
                #upadte the node baseed the condition
                currentB=currentB.next
            else:
                #if the current node is in hashset return the node
                if currentB is not None:
                    return currentB
            
        #if there is no intersection return none
        return None

        