class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(loc: int, i: int, j: int) -> bool:
            if loc==l-1:
                return True
            used[i][j] = True
            if i != 0:
                if (board[i-1][j]==word[loc+1]) and (used[i-1][j]==False):
                    if find(loc+1, i-1, j):
                        return True 
            if i != m-1:
                if (board[i+1][j]==word[loc+1]) and (used[i+1][j]==False):
                    if find(loc+1, i+1, j):
                        return True 
            if j != 0:
                if (board[i][j-1]==word[loc+1]) and (used[i][j-1]==False):
                    if find(loc+1, i, j-1):
                        return True 
            if j != n-1:
                if (board[i][j+1]==word[loc+1]) and (used[i][j+1]==False):
                    if find(loc+1, i, j+1):
                        return True 
            used[i][j] = False
            return False
        
        m = len(board)
        n = len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    # used = [[False] * n] * m
                    # 这种生成方式修改矩阵元素有问题，导致错误
                    used = [[False] * n for _ in range(m)]
                    if find(0, i, j):
                        return True
        return False
