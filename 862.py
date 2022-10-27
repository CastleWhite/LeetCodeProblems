class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        l = len(nums)
        for i in range(1, l):
            nums[i] += nums[i-1]
        nums = [0] + nums
        stack = deque([0])
        res = l + 1
        for i in range(1, l+1):
            while stack and nums[i] >= k + nums[stack[0]]:
                res = min(res, i - stack[0])
                stack.popleft()
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop() 
            stack.append(i)
        return res if res <= l else -1
