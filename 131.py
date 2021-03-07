class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        reco = [[True]*l for _ in range(l)]
        for e in range(1,l):
            for b in range(e):
                reco[b][e] = reco[b+1][e-1] and (s[b]==s[e])
        
        anss = []
        ans = []
        def dfs(n: int):
            for i in range(n,l):
                if reco[n][i]:
                    ans.append(s[n:i+1])
                    if i < l-1:
                        dfs(i+1)
                    else:
                        anss.append(ans[:])

                    ans.pop()

        dfs(0)

        return anss



