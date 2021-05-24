class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * (l+1)
        post = [1] * (l+1)
        for n,i in enumerate(nums):
            pre[n+1] = pre[n] * i
        for n,i in enumerate(nums[::-1]):
            post[n+1] = post[n] * i

        out = [0] * l
        for i in range(l):
            out[i] = pre[i] * post[l-i-1]

        return out
