class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        b = []
        n = len(arr)
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                b.append(i)

        if not b: return 0
        res = b[-1]
        j = n-1
        for i in range(b[0]-1, -1, -1):
            while arr[j] >= arr[i] and j >= b[-1]:
                j -= 1
            res = min(res, j - i)
        return res
