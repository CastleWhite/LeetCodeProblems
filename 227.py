class Solution:
    def calculate(self, s: str) -> int:

        ans = 0
        stack = []
        num_stack = []
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
            elif s[i] == '*':
                stack.append(3)
                i += 1
            elif s[i] == '/':
                stack.append(4)


                i += 1
            else:
                num = 0
                while i < l and s[i] >= '0' and s[i] <= '9':
                    num = num*10 + ord(s[i])-ord('0')
                    i += 1
                if stack and stack[-1] > 2:
                    sign = stack.pop()
                    num2 = num_stack.pop()
                    if sign == 3:
                        num_stack.append(num2 * num)
                    else:
                        num_stack.append(num2 // num)
                else:
                    num_stack.append(num)    
        ans = 0

        ls = len(stack)
        ln = len(num_stack)
        if ls < ln:
            ans = num_stack.pop(0)
        for i in range(ls):
            ans += stack[i]*num_stack[i]
        return ans
