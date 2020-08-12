class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[0:k]
        self.k = k
        heapify(self.heap)
        for i in nums[k:]:
            if i > self.heap[0]:
                heapreplace(self.heap, i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
