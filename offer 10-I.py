class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 :
            return 1
        else:
            a = 0
            b = 1
            for i in range(n-1):
                
                c = a
                a = b
                b = c+b
            return b%1000000007
