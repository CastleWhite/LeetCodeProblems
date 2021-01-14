class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        sumer = 0
        ans = []

        for i in A:
            sumer = sumer*2 + i
            if sumer%5 == 0:
                ans.append(True)
            else:
                ans.append(False)

        return ans
