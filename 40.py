class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
               
        ans = []
        for m in range(len(candidates)):
            i = candidates[m]
            if m!=0 and candidates[m-1]==i:
                continue

            if i > target:
                continue
            elif i == target:
                ans.append([i])
            else:
                
                nex = self.combinationSum(candidates[m+1:],target-i)
                for a in nex:
                    a.append(i)
                    ans.append(a)

        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() #无返回值，直接改原来List #且只能用于List
        #sorted（cand） 返回排好的，不改原来
        return self.combinationSum(candidates,target)
        
