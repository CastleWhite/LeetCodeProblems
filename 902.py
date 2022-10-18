class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        l = len(digits)
        n = str(n)
        m = len(n)

        @cache
        def dfs(isLimit, isLead, i):
            if i == m: return int(not isLead)
            res = 0
            if isLead: res += dfs(0, 1, i+1)
            if isLimit:
                for j in digits:
                    if j < n[i]: res += dfs(0, 0, i+1)
                    elif j == n[i]: res += dfs(1, 0, i+1)
                    else: break
            else:
                res += l ** (m - i)
            return res

        return dfs(1, 1, 0)
