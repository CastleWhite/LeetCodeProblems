class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        
        l = len(heights)
        stack = [0]
        ans = heights[0]

        for i in range(1,l):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
                
            pre = -1
            for a in stack:
                ans = max(ans, heights[a]*(i-pre))
                pre = a

        return ans
            
