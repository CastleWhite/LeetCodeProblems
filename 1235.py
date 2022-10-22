class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [0] * 50010
        t = list(zip(startTime, endTime, profit))
        t.sort(key = lambda x: x[1])
        s, e, p = zip(*t)
        for i in range(len(s)):
            f = bisect_right(e, s[i]) - 1
            dp[i] = max(dp[i-1], p[i]+dp[f])
        return dp[len(s)-1]
