class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for i in strs:
            count = [0]*26
            for zimu in i:
                count[ord(zimu)-ord('a')] += 1
            tu_count = tuple(count)
            if tu_count in di:
                di[tu_count].append(i)
            else:
                di[tu_count] = [i]
        
        return (list(di.values()))
