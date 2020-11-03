class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l = len(A)
        if l<3:
            return False
        
        pre = A[0]
        up = 0
        for i in range(1,l):
            if pre < A[i]:
                if up==0:
                    up = 1
                elif up == 2:
                    return False
            elif pre == A[i]:
                return False
            else:
                if up == 1:
                    up = 2
                elif up == 0:
                    return False
            pre = A[i]

        if up == 2:
            return True
        else:
            return False

