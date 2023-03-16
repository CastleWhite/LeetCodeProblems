class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ik = -1
        for i, n in enumerate(nums):
            if n == k:
                ik = i 
                break
        
        N = 100001
        left = [0] * (N << 1)
        left[N] = 1
        res = 1

        cnt = 0
        for i in range(ik-1, -1, -1):
            if nums[i] > k:
                cnt += 1
            else:
                cnt -= 1
            left[N + cnt] += 1
            if cnt == 0 or cnt == 1: res += 1
        cnt = 0
        for i in range(ik+1, len(nums)):
            if nums[i] > k:
                cnt += 1
            else:
                cnt -= 1
            res += left[N - cnt]
            res += left[N - cnt + 1]

        return res

        
