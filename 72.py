class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0: return n
        elif n == 0: return m

        reco = [[501] * n for _ in range(m)]

        same = False
        for i in range(m):
            if same:
                reco[i][0] = i
            elif word1[i] == word2[0]:
                same = True
                reco[i][0] = i
            else:
                reco[i][0] = i + 1

        for j in range(1,n):
            reco[0][j] = j if word1[0] == word2[j] else reco[0][j-1] + 1
            for i in range(1,m):
                if word1[i] == word2[j]:
                    reco[i][j] = reco[i-1][j-1]
                else:
                    reco[i][j] = min(reco[i][j-1], reco[i-1][j], reco[i-1][j-1]) + 1
        
        return reco[m-1][n-1] 
