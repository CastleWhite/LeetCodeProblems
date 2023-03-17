class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        same = [0] * n
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                same[i] = same[i-1] + 1
            else:
                same[i] = same[i-1]
        same.append(same[-1])
        
        r = 0
        res = n
        for i, l in enumerate(nums):
            if i < n -1 and nums[i+1] == l: continue
            target = l + n - 1
            while r < n and nums[r] < target: r += 1
            t = n - r + i + same[r] - same[i]
            if r < n and nums[r] == target: t -= 1
            res = min(res, t)
            if r == n: break
        return res
