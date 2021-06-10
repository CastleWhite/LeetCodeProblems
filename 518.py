class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [1] + [0] * amount
        for coin in coins:
            for i in range(coin,amount+1):
                res[i] += res[i-coin]
        
        return res[-1]
