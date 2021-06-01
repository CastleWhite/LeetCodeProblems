class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        l = len(candiesCount)
        pre_sum = [0] * (l+1)
        for i in range(l):
            pre_sum[i+1] = pre_sum[i] + candiesCount[i]
        ans = []
        for query in queries:
            day = query[1]+1
            ans.append( pre_sum[query[0]] < day*query[2] and day <= pre_sum[query[0]+1] )

        return ans
