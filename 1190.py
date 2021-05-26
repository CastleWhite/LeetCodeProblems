class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(a, b):
            left = 0
            ans = []
            l1, newa = 0, 0
            for i in range(a, b+1):
                ch = s[i]
                if ch == '(':
                    left += 1
                    if left == 1:
                        l1 = len(ans)
                    elif left == 2:
                        newa = i+1
                elif ch == ')':
                    left -= 1
                    if left == 1:
                        ans.insert(l1, reverse(newa, i-1))
                elif not left:
                    ans.append(ch)
                elif left == 1:
                    ans.insert(l1, ch)
            return ''.join(ans)

        l = len(s)
        
        return reverse(0,l-1)
