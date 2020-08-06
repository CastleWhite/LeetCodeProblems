class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k==1 :
            return nums
        q = [nums[0]]
        for i in range(1,k):
            while q and nums[i]>q[-1]:
                q.pop()
            q.append(nums[i])
        ans = []
        ans.append(q[0])
        for j in range(len(nums)-k):
            if nums[j]==q[0]:
                q.pop(0)
            while q and nums[j+k]>q[-1]:
                q.pop()
            q.append(nums[j+k])
            ans.append(q[0])
        return ans

