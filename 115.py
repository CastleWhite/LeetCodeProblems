class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        l = len(t)
        reco = [0] * l
        for i in s:
            
            for j in range(l-1,0,-1):
                if i == t[j]:
                    reco[j] += reco[j-1]
            if i == t[0]:
                reco[0] += 1

        return reco[-1]
