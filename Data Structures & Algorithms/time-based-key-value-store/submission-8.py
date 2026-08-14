from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list) # key -> [(time, val)...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        return
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        i = bisect_right(arr, timestamp, key = lambda x : x[0]) - 1
        
        return arr[i][1] if i >= 0 else ""
        
