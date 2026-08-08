class TimeMap:
    # key -> [(timestamp, value), ...]

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search of greatest timestamp thats <= parameter timestamp

        l, r = 0, len(self.data[key]) - 1
        prev_timestamp = (-1, -1)

        while l <= r:
            m = (r - l)//2 + l
            if self.data[key][m][0] == timestamp:
                return self.data[key][m][1]
            elif self.data[key][m][0] < timestamp:
                l = m + 1
                prev_timestamp = (m, max(prev_timestamp[1], self.data[key][m][0]))
            else:
                r = m - 1
            
        if prev_timestamp[1] == -1:
            return ""
        else:
            return self.data[key][prev_timestamp[0]][1]
            