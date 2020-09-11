class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        for m in range(len(candidates)):
            i = candidates[m]
            if i > target:
                continue
            elif i == target:
                ans.append([i])
            else:
                newtarget = target-i
                for j in self.combinationSum(candidates[m+1:], newtarget):
                    if j:
                        j.append(i) 
                        ans.append(j)
        return ans

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n<1 or n>45:
            return []
        numL = [1,2,3,4,5,6,7,8,9]
        can = self.combinationSum(numL,n)
        ans = []
        for i in can:
            if len(i) == k:
                ans.append(i)
        return ans
        
#用的旧函数，可以针对性优化
#可以剪枝 k长度
