class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res = []
        tmp = []
        def dfs(i):
            if i == n:
                res.append(''.join(tmp))
                return
            if s[i].isdigit():
                tmp.append(s[i])
                dfs(i + 1)
            else:
                tmp.append(s[i].lower())
                dfs(i + 1)
                tmp.pop()
                tmp.append(s[i].upper())
                dfs(i + 1)
            tmp.pop()
            return

        dfs(0)
        return res
