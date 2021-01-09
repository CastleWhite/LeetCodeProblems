class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = len(prices)
        if l<2:
            return 0
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0
        for i in range(1,l):
            buy1 = max(buy1, -prices[i])
            sell1 = max(prices[i]+buy1, sell1)
            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(prices[i]+buy2, sell2)
            
        return sell2
