class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l < 2: return 0
        
        hold = -prices[0]
        emp = 0
        sell_today = 0

        for i in range(1, l):
            p = prices[i]
            hold, emp, sell_today = max(emp - p, hold), max(emp, sell_today), hold + p
        
        return max(emp, sell_today)
