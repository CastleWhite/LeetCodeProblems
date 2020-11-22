class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        reco = [0]*26
        for i in s:
            reco[ord(i)-ord('a')] += 1

        for i in t:
            if reco[ord(i)-ord('a')] == 0:
                return False
            reco[ord(i)-ord('a')] -= 1

        return reco == [0]*26
