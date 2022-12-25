class Solution:
    def minimumBoxes(self, n: int) -> int:
        @cache
        def fib(x):
            if x == 0:
                return 0
            return x + fib(x-1)

        i = 1
        while n - fib(i) >= 0:
            n -= fib(i)
            i += 1
        res = fib(i-1)

        l, r = 0, i
        while l < r:
            mid = (l + r) >> 1
            if n <= fib(mid):
                r = mid
            else:
                l = mid + 1
        # print(res, l, r, n)
        return res + l
