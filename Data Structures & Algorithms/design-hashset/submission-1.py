class Node:
    def __init__(self, data: int, next = None):
        self.data = data
        self.next = next

class MyHashSet:

    def __init__(self):
        self.data = [None] * 100

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        # Add key if there is no node yet
        curr = self.data[self.hash(key)]
        if not curr:
            self.data[self.hash(key)] = Node(key)
            return
        
        # Reach the last node and append
        while curr.next:
            curr = curr.next
        curr.next = Node(key)
        return

    def remove(self, key: int) -> None:       
        # Search for node with key and remove it
        curr = self.data[self.hash(key)]
        prev = None
        while curr:
            if curr.data == key:
                # remove key
                if prev:
                    prev.next = curr.next
                else:
                    self.data[self.hash(key)] = curr.next
                return


            prev = curr
            curr = curr.next
        
        return


    def hash(self, key):
        return key % 100

    def contains(self, key: int) -> bool:
        curr = self.data[self.hash(key)]
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)