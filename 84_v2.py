class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0

        heights = [-1] + heights
        l = len(heights)
        stack = [0]
        ans = heights[0]

        for i in range(1,l):
            while stack and heights[i] <= heights[stack[-1]]:
                hi = stack.pop()
                ans = max(ans, heights[hi] * (i-1-stack[-1]))
            stack.append(i)
                
        for i in range(1, len(stack)):
            ans = max(ans, heights[stack[i]]*(l-1-stack[i-1]))

        return ans
            
