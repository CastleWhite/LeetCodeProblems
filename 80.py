class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        l = len(nums)

        i = 1
        pre = nums[0]
        num = 1

        for _ in range(l-1):
            if nums[i] == pre:
                if num == 2:
                    nums.pop(i)
                else:
                    num += 1
                    i += 1
            else:
                pre = nums[i]
                nums = 1
                i += 1
        
        return len(nums)
