class ListNode:
    def __init__(self,val):
        self.next=None
        self.val=val

class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def get(self, index: int) -> int:
        current=self.head
        pos=0
        while current!=None:
            if pos==index:
                return current.val
            pos=pos+1
            current=current.next
        return -1

    def addAtHead(self, val: int) -> None:
        node=ListNode(val)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
        
    def addAtTail(self, val: int) -> None:
        node=ListNode(val)
        if self.head is None:
            self.head=node
            return
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=node

    def addAtIndex(self, index: int, val: int) -> None:
        node=ListNode(val)
        if self.head==None and index==0:
            self.head=node
            return 
        current=self.head
        if index==0:
            node.next=self.head
            self.head=node
            return
        pos=0
        while current!=None and pos<index-1:
            pos=pos+1
            current=current.next
        if current and current.next==None:
            current.next=node
        elif current!=None:
            temp=current.next
            current.next=node
            node.next=temp
    def deleteAtIndex(self, index: int) -> None:
        if self.head==None:
            return 
        current=self.head
        if index==0:
            self.head=self.head.next
            return
        pos=0
        while current!=None and pos<index-1:
            pos=pos+1
            current=current.next

        if current and current.next!=None:
            current.next=current.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)