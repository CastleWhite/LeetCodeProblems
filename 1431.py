class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = [i+extraCandies>=m for i in candies]
        return ans
