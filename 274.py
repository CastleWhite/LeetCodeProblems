class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l, h = 0, n-1
        while l <= h:
            mid = l+h >> 1
            if n-mid > citations[mid]:
                l = mid + 1
            elif n-mid < citations[mid]:
                h = mid - 1
            else:
                return n-mid
        return n-l
