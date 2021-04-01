class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        elif N == 4:
            return 7
        elif N % 4 == 0:
            return N + 1
        elif N % 4 == 3:
            return N - 1
        else:
            return N + 2
