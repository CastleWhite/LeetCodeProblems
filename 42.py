class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        stack = [ (height[0], 0)  ]
        ans = 0

        for i, h in enumerate(height, 1):
            if h == 0: continue

            if h < stack[-1][0]:
                ans += h * (i - stack[-1][1] - 1)                
            else:
                pre = 0
                while stack and stack[-1][0] <= h:
                    (l, w) = stack.pop()
                    ans += (l - pre) * (i - w - 1)
                    pre = l 
                if stack:
                    ans += (h - pre) * (i - stack[-1][1] - 1)
            stack.append( (h, i) )

        return ans
