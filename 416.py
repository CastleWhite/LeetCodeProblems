class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        m = max(nums)
        target = s // 2
        if m > target:
            return False
        elif m == target:
            return True
        
        # ans = [0]
        # i = 0
        # su = nums[0]
        l = len(nums)

        # while ans:

        #     if su < target:
        #         i = i+1
        #         if i >= l:
                    
        #             i = ans.pop()
        #             su -= nums[i]
        #             if not ans:
        #                 return False
        #             i = ans.pop() + 1
        #             su -= nums[i-1]
        #         ans.append(i)
        #         su += nums[i]
        #     elif su == target:
        #         return True
        #     else:
        #         i = ans.pop() + 1
        #         su -= nums[i-1]
        #         while i >= l:
        #             if not ans:
        #                 return False
        #             i = ans.pop() + 1
        #             su -= nums[i-1]

        #         ans.append(i)
        #         su += nums[i] 

        # return False
        # 超时了
        state = [1]+[0]*target
        for i in nums:
            for j in range(target-i,-1,-1):
                if state[j] :
                    state[j+i] = 1
            if state[-1]:
                return True

        return False
