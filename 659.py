class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        results = []
        pre = nums[0]
        for i in range(len(nums)):
            if nums[i] == pre:
                flag = False
                for result in results:
                    if result[0] == (pre - 1):
                        result[0] += 1
                        result[1] += 1
                        flag = True
                        break
                if not flag:
                    results = [[nums[i],1]] + results
            elif nums[i] == (pre+1):
                results[0][0] += 1
                results[0][1] += 1
            else:
                results = [[nums[i],1]] + results
                # 记录数目，新建头时，强制判断长度3
            pre = nums[i]
     
        for result in results:
            if result[1] < 3:
                return False
        return True
#使用哈希表
# collection Counter
