class MyHashMap:

    def __init__(self):
        # map stors arrays of (key, val) tuples
        self.data = [[] for _ in range(100)]

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.data[self.get_idx(key)]):
            if k == key:
                self.data[self.get_idx(key)][i] = ((key, value))
                return

        self.data[self.get_idx(key)].append((key, value))
        return
        
        

    def get(self, key: int) -> int:
        for k, v in self.data[self.get_idx(key)]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        for k, v in self.data[self.get_idx(key)]:
            if k == key:
                self.data[self.get_idx(key)].remove((k, v))
                return
        return

        


    def get_idx(self, key: int):
        return key % 100

    # returns whether a key exists in the map
    def exists(self, key: int):
        for k, _ in self.data[self.get_idx(key)]:
            if k == key:
                return True
            
        return False

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)