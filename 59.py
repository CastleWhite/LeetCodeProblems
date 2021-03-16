class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        flag = 1
        h = n
        s = n - 1
        i = 1
        x, y = -1, 0
        ans = [[-1] * n for _ in range(n)]
        while h>0 :
            for _ in range(h):
                x += flag
                ans[y][x] = i
                i += 1
            if s <= 0: break
            for _ in range(s):
                y += flag
                ans[y][x] = i
                i += 1
            h -= 1
            s -= 1
            flag = -flag

        return ans
