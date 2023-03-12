class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        l = len(nums)
        presum = [nums[0]] * l 
        for i in range(1, l):
            presum[i] = presum[i-1] + nums[i]

        if presum[-1] % p == 0: return 0

        res = l
        target = sum(nums)
        h = defaultdict(list)

        h[0].append(-1)
        prep = [0] * l
        for i in range(l):
            prep[i] = presum[i] % p
            dif = (prep[i] - target) % p
            if h[dif]:
                res = min(res, i - h[dif][-1])

            h[prep[i]].append(i)
        return res if res < l else -1
