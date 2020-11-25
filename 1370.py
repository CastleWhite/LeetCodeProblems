class Solution:
    def sortString(self, s: str) -> str:
        reco = [0]*26
        for i in s:
            reco[ord(i)-ord('a')] += 1
        ans = ""
        flag = 1
        loc = 0
        for i in range(len(s)):

            while reco[loc] <= 0:
                loc += flag
                if loc < 0 or loc > 25:
                    loc -= flag*2
                    flag = -flag

            ans += chr(ord('a')+loc)
            reco[loc] -= 1
            loc += flag
            if loc < 0 or loc > 25:
                loc -= flag
                flag = -flag
        
        return ans
