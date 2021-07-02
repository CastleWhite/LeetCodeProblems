class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        # dp = [0] * (coins+1)
        # for c in costs:
        #     for i in range(coins,0,-1):
        #         if i-c<0:
        #             break
        #         dp[i] = max(dp[i], dp[i-c] + 1)
        # return dp[-1]
        res = 0
        for c in costs:
            coins -= c
            if coins<0:
                break
            res += 1

        return res
