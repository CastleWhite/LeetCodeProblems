class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = []
        ans.append([r0, c0])

        def legal (loc: List[int]) -> bool:
            return loc[0]>=0 and loc[0]<R and loc[1]>=0 and loc[1]<C 

        i = 1
        while i:
            for add_c in range(i):
                tmp = [r0-i+add_c, c0+add_c]
                if legal(tmp):
                    ans.append(tmp)
                tmp = [r0+i-add_c, c0-add_c]
                if legal(tmp):
                    ans.append(tmp)
                tmp = [r0-add_c, c0-i+add_c]
                if legal(tmp):
                    ans.append(tmp)
                tmp = [r0+add_c, c0+i-add_c]
                if legal(tmp):
                    ans.append(tmp)

            if len(ans) == R*C:
                return ans
            i += 1
