class MinStack:
    
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if self.data:
            _, last_min = self.data[-1]
            self.data.append((val, min(last_min, val)))
        else:
            self.data.append((val, val))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        val, _ = self.data[-1]
        return val

    def getMin(self) -> int:
        _, curr_min = self.data[-1]
        return curr_min
        
