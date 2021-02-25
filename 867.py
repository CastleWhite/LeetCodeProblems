class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            aans = []
            for j in range(m):
                aans.append(matrix[j][i])
            ans.append(aans)

        return ans
