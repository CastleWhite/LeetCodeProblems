class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = 0
        s = 0
        for i in moves:
            if i=='U':
                s = s + 1
            elif i=='D':
                s = s - 1
            elif i=='L':
                h = h + 1
            elif i=='R':
                h = h - 1
        
        return not (s or h)
