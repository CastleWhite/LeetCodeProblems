class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        reco = [0]*1001
        for i in arr1:
            reco[i] += 1
        ans = []
        for j in arr2:
            if reco[j]:
                ans += [j]*reco[j]
                reco[j] = 0
            else:
                print('error')
        for i,n in enumerate(reco):
            if n:
                ans += [i]*n

        return ans
            
