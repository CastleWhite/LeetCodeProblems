class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
