class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        count = 1
        l =len(s)
        pre = s[0]
        for i in range(1,l):
            if s[i] == pre:
                count += 1
            else:
                if count >= 3:
                    ans.append([i-count,i-1])
                pre = s[i]
                count = 1
        if count >= 3:
            ans.append([l-count,l-1])
        return ans
