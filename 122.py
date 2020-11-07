class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        l = len(prices)
        while i < l-1:

            while i+1 < l and prices[i] >= prices[i+1]:
                i += 1
            start = prices[i]
            while i+1 < l and prices[i] <= prices[i+1]:
                i += 1
            end = prices[i]

            ans += end - start

        return ans
