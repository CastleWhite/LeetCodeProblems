class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                left[j] *= (i-j)
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        while stack:
            j = stack.pop()
            left[j] *= n - j
        res = 0

        for i in range(n):
            res += arr[i] * left[i]
        return res % (10**9+7)
