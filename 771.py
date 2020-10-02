class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        JJ = set(J)
        ans = 0
        for i in S:
            if i in JJ:
                ans += 1

        return ans
