class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        if l<2:
            return 0
        buy_prices = []

        flag = 0
        for i in range(1,l):
            if flag == 0:
                if prices[i] > prices[i-1]:
                    buy_prices.append(prices[i-1])

                    # end = prices[i]
                    flag = 1
            else:
                if prices[i] < prices[i-1]:
                    buy_prices.append(prices[i-1])

                    flag = 0
        if flag == 1:
            if buy_prices[-1] == prices[-1]:

                buy_prices.pop()
            else:

                buy_prices.append(prices[-1])
        
        while len(buy_prices) > k*2:
            min_i = 0
            min_profit = buy_prices[1]-buy_prices[0]
            for i in range(1,len(buy_prices)-1,2):
                if buy_prices[i]-buy_prices[i+1] < min_profit:
                    min_profit = buy_prices[i]-buy_prices[i+1]
                    min_i = i
                if buy_prices[i+2]-buy_prices[i+1] < min_profit:
                    min_profit = buy_prices[i+2]-buy_prices[i+1]
                    min_i = i+1
            buy_prices.pop(min_i)
            buy_prices.pop(min_i)
        ans = 0
        for i in range(0,len(buy_prices),2):
            ans += buy_prices[i+1]-buy_prices[i]
        return ans
