class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1
        even = 0
        l = len(A)

        while odd < l and even < l:
            while A[even] % 2 == 0:
                even += 2
                if even>=l:
                    return A
            while A[odd] % 2:
                odd += 2
                if odd>l:
                    return A
            A[odd], A[even] = A[even], A[odd]
            even += 2
            odd += 2

        return A
