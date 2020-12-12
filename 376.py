class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return l

        flag = nums[1] - nums[0]
        pre = nums[1]
        ans = 2 if flag else 1
        for i in range(2,l):
            if (nums[i] - pre) * flag > 0:
                pre = nums[i]
            elif nums[i] == pre:
                continue
            else:
                flag = nums[i] - pre
                pre = nums[i]
                ans += 1
        return ans
