class ListNode:
    def __init__(self,key):
        self.next=None
        self.prev=None
        self.key=key
class MyHashSet:
    def __init__(self):
        self.head=None

    def add(self, key: int) -> None:
        if self.contains(key):
            return None
        node=ListNode(key)
        if not self.head:
            self.head=node
            return None
        current=self.head
        while current.next:
            current=current.next
        current.next=node
        node.prev=current
        return None
    def remove(self, key: int) -> None:
        if not self.head:
            return None
        if self.head.key==key:
            if not self.head:
                self.head=None
            else:
                self.head.next.prev=None
                self.head=self.head.next
            return None
        current=self.head
        while current:
            if current.key==key:
                break
            current=current.next
        if not current:
            return None
        if not current.next:
            current.prev.next=None
            current.prev=None
            return None
        temp=current.next
        current.prev.next=temp
        temp.prev=current.prev
        return None






    def contains(self, key: int) -> bool:
        if not self.head:
            return False
        current=self.head
        while current:
            if current.key==key:
                return True
            current=current.next
        return False
    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)