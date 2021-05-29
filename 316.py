class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        for i in s:
            if i not in stack:
                while stack and stack[-1] >= i and count[stack[-1]] > 1:
                    count[stack[-1]] -= 1
                    stack.pop()
                stack.append(i) 
            else:
                count[i] -= 1
        return ''.join(stack)
