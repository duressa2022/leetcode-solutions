class ListNode:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class MyHashMap:
    def __init__(self):
        self.head = None

    def put(self, key: int, value: int) -> None:
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        node = ListNode(key, value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  
                    self.head = current.next
                return
            current = current.next
