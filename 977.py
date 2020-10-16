class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        right = len(A)-1
        left = 0
        ans = [0]*(right+1)
        pos = right
        while right>=left:
            if A[right] > -A[left]:
                # insert 操作慢？
                ans[pos] = A[right]**2
                right -= 1
            else:
                ans[pos] = A[left]**2
                left += 1
            pos -= 1
        
        return ans

        
