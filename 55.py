class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        l = len(nums)
        can_arrive = 0
        while i < l and can_arrive >= i:
            can_arrive = max(can_arrive, i+nums[i])
            i += 1
        
        return True if i == l else False
