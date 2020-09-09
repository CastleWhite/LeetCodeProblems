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
                for j in self.combinationSum(candidates[m:], newtarget):
                    if j:
                        j.append(i) 
                        ans.append(j)

        return ans
