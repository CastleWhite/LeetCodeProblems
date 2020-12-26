class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ans = 0
        r = len(matrix)
        c = len(matrix[0])
        reco = []
        for j in range(c):
            if matrix[0][j] == "1":
                if reco and reco[-1]:
                    new = reco[-1][0]+1
                    reco.append([new])
                    ans = max(ans, new)
                else:
                    reco.append([1])
                    ans = max(ans, 1)
            else:
                reco.append([])

        for i in range(1,r):
            if matrix[i][0] == "1":
                reco[0].append(1)
                ans = max(ans, len(reco[0]))
            else:
                reco[0] = []
            for j in range(1,c):
                if matrix[i][j] == "1":
                    reco[j].append(1)
                    l = len(reco[j-1])
                    ll = len(reco[j])
                    for f in range(min(l, ll)):
                        reco[j][f] = reco[j-1][f]+1
                        ans = max(ans, (f+1)*reco[j][f])
                    if ll>l:
                        for f in range(l, ll):
                            reco[j][f] = 1
                            ans = max(ans, f+1)

                else:
                    reco[j] = []
        
        return ans

