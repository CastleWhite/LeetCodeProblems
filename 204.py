class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [0, 0] + [1]*(n-2)
        up = ceil(sqrt(n))
        for i in range(2,up):
            if isPrimes[i]:
                a = i * i
                while a < n:
                    isPrimes[a] = 0
                    a += i

        return sum(isPrimes)
