class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        l = len(nums)
        # newnums = []
        # for i in range(l):
        #     if i == 0 or nums[i] != nums[i-1]:
        #         newnums.append(nums[i])
        # wrong !!! [-1,-1,2] ??
        
        for i in range(l):
            a = nums[i]
            if i > 0 and a == nums[i-1]: continue
            if a > 0: break # [0,0,0]??

            j = i+1
            k = l-1
            remain = -a
            while j < k:
                if nums[j] + nums[k] == remain:
                    ans.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1] and nums[k] == nums[k+1]:
                        j += 1
                        k -= 1
                    
                elif nums[j] + nums[k] > remain:
                    k -= 1
                else:
                    j += 1

        return ans
