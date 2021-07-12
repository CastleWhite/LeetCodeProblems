class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        while l<=r:
            mid = l+r >> 1
            if n-mid > citations[mid]:
                l = mid + 1
            elif n-mid < citations[mid]:
                r = mid - 1
            else:
                return n-mid
        return n-l
