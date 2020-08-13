class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapify(stones)
        while len(stones)>1:
            a = heappop(stones)
            b = heappop(stones)
            if a<b:
                heappush(stones,a-b)
            

        if stones:
            return -stones[0]
        else:
            return 0
