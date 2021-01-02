class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_stack = []
        window_head = 0 
        # window_tail = head + k

        for i in range(k):
            while mono_stack and nums[mono_stack[-1]]<nums[i]:
                mono_stack.pop()
            mono_stack.append(i)
        # init

        ans = [nums[mono_stack[0]]]
        l = len(nums)

        for h in range(1,l-k+1):
            if mono_stack and mono_stack[0]<h:
                mono_stack.pop(0)
            while mono_stack and nums[mono_stack[-1]]<nums[h+k-1]:
                mono_stack.pop()
            mono_stack.append(h+k-1)
            ans.append(nums[mono_stack[0]])

        
        return ans
                
