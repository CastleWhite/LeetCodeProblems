class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d: return ""
        if self.d[key][0][1] > timestamp: return ""
        n = len(self.d[key])
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) >> 1
            if self.d[key][mid][1] > timestamp:
                r = mid - 1
            elif self.d[key][mid][1] == timestamp:
                return self.d[key][mid][0]
            else:
                l = mid + 1
        return self.d[key][r][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
