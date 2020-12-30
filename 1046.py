class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones)>1:
            x = heappop(stones)
            y = heappop(stones)
            remain = x-y
            if remain!=0:
                heappush(stones,remain)
        return -stones[0] if stones else 0
