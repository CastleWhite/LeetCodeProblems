class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0: return 0

        reco = [0] * (n+1)
        reco[0] = 1
        reco[1] = 1
        for i in range(2,n+1):
            for j in range(i//2):
                reco[i] += reco[j] * reco[i-1-j] * 2
            if i % 2:
                reco[i] += reco[i//2] ** 2

        return reco[-1]
