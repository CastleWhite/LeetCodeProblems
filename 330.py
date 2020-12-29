class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cover = 0
        ans = 0
        while cover<n:
            if nums and nums[0] <= cover+1:
                cover += nums[0]
                nums.pop(0)
            else:
                ans += 1
                cover += cover+1
        return ans
