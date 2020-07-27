class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = len(prices)
        m = prices[0]
        ans = [0]
        for i in range(1,l):
            
            if prices[i] < m:
                m = prices[i]
                
            else:
                ans.append(prices[i] - m)

        return max(ans)
            
