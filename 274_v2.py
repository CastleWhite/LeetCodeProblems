class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort()
        n = len(citations)
        s = [0]*(n+1)
        for i in citations:
            if i > n: s[n] += 1
            else: s[i] += 1
        h = 0
        res = n
        while h <= res:            
            res -= s[h]
            h += 1
        return h-1
