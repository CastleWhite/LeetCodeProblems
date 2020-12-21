class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tmp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            tmp[0], tmp[1] = tmp[1], min(tmp)+cost[i]
        
        return min(tmp)
