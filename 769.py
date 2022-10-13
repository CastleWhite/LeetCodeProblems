class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxN = 0
        res = 0
        for i, a in enumerate(arr):
            maxN = max(maxN, a)
            if maxN == i: res += 1
        return res
