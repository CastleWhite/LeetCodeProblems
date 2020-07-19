class MaxQueue:

    def __init__(self):
        self.maxList = []
        self.val = []
        
    def max_value(self) -> int:
        if self.maxList:
            return self.maxList[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.val.append(value)
        while self.maxList and value > self.maxList[-1]:
            self.maxList.pop(-1)
        self.maxList.append(value)
        
        
    def pop_front(self) -> int:
        if self.val:
            out = self.val.pop(0)
            if out == self.maxList[0]:
                self.maxList.pop(0)
            return out

        else:
            return -1

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
