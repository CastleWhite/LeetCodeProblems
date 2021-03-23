class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        left2 = 0
        right2 = 0
        ans = 0

        for a in range(len(s)):
            i = s[a]
            if i == '(':
                left += 1
            else:
                right += 1
                if right == left:
                    ans = max(ans, right*2)
                elif right > left:
                    right = left = 0

            j = s[-a-1]
            if j == ')':
                left2 += 1
            else:
                right2 += 1
                if right2 == left2:
                    ans = max(ans, right2*2)
                elif right2 > left2:
                    right2 = left2 = 0

        return ans
