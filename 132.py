class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        reco = [[True] * l for _ in range(l)]
        for j in range(1,l):
            for i in range(j):
                reco[i][j] = reco[i+1][j-1] and (s[i] == s[j])

        minc = [2002] * l
        for i in range(l):
            if reco[0][i]:
                minc[i] = 0
            else:
                for j in range(i):
                    if reco[j+1][i]:
                        minc[i] = min(minc[i], minc[j]+1)
                        
        return minc[l-1]
