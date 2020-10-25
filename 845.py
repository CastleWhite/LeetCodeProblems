class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        l = len(A)
        if l<3:
            return 0
        up = 0
        down = 0
        ans = 0
        anses = 0
        for i in range(1,l):
            tr = A[i] - A[i-1] 
            if tr > 0:
                if down > 0:
                    anses = max(anses, ans + down)
                    ans = 0
                    down = 0
                up += 1
            elif tr == 0:
                if down > 0:
                    anses = max(anses, ans + down)
                ans = 0
                up = 0
                down = 0               
            else:
                if down > 0:
                    down += 1
                elif up > 0:
                    down = 1
                    ans = up
                up = 0
        if down > 0:
            anses = max(anses, ans + down)
        
        if anses:
            return anses+1
        else:
            return 0
