class Solution:
    def calculate(self, s: str) -> int:

        ans = 0
        stack = []
        num_stack = [0]
        l = len(s)
        i = 0
        while i < l:

            if s[i] == ' ':
                i += 1

            elif s[i] == '+':
                stack.append(1)
                i += 1
            elif s[i] == '-':
                stack.append(-1)
                i += 1
            elif s[i] == '(':
                stack.append(3)
                i += 1
            elif s[i] == ')':
                if stack[-1] == 3:
                    stack.pop()
                if stack and stack[-1] < 2:
                    num = num_stack.pop()
                    num2 = num_stack.pop()
                    num_stack.append(num2 + num*stack.pop())

                i += 1
            else:
                num = 0
                while i < l and s[i] >= '0' and s[i] <= '9':
                    num = num*10 + ord(s[i])-ord('0')
                    i += 1
                if stack and stack[-1] < 2:
                    num2 = num_stack.pop()
                    num_stack.append(num2 + num*stack.pop())
                else:
                    num_stack.append(num)    

        return num_stack[-1]
