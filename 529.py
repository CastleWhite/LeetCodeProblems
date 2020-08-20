class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x = click[0]
        y = click[1]
        m = len(board)
        n = len(board[0])
        a = board[x][y]
        if a == 'M':
            board[x][y] = 'X'
            
        elif a == 'E':
            num = 0
            R = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if x+i>=0 and x+i<m and y+j>=0 and y+j<n:
                        if board[x+i][y+j] == 'M':
                            num = num+1
                        elif board[x+i][y+j] == 'E':
                            R.append(x+i)
                            R.append(y+j)
            if num:
                board[x][y] = str(num)
            else:
                board[x][y] = 'B'
                while R:
                    i = R.pop()
                    j = R.pop()
                    self.updateBoard(board, [j,i])
                
        return board

