class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        a = 0
        b = l-1
        ans = 0

        while (a<b):
            new = (b-a)*min(height[a],height[b])
            if new > ans: ans = new
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        
        return ans
            
