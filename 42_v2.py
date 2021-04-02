class Solution:
    def trap(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        lmax = 0
        rmax = 0

        ans = 0
        while left <= right:
            if height[left] < height[right]:
                if lmax > height[left]:
                    ans += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1
            else:
                if rmax > height[right]:
                    ans += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1
        
        return ans

            

            
