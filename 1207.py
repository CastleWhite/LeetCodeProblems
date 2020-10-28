class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        

        def countOccur(arr: List[int]) -> List[int]:
            reco = dict.fromkeys(arr,0)  ##注意用法

            for i in arr:
                reco[i] += 1
            return reco.values()

        count = countOccur(arr)
        ccount = countOccur(count)

        for i in ccount:
            if i != 1:
                return False
        
        return True
