class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can = [-1]
        l = len(s)
        for i in range(l):
            for p in can:
                if s[p+1:i+1] in wordDict:
                    can.append(i)
                    break
        
        return l-1 in can
