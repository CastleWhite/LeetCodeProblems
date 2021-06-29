class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10**9+7
        n = len(prevRoom)
        rooms = defaultdict(list)
        for i in range(1,n):
            rooms[prevRoom[i]].append(i)
        s, sz = [1] * n, [0] * n
        # def qmi(a, k):
        #     res = 1
        #     while k:
        #         if k & 1:
        #             res *= a % mod
        #         k >>= 1
        #         a *= a % mod
        #     return res
        f, g = [0] * n, [0] * n
        f[0], g[0] = 1, 1
        for i in range(1,n):
            f[i] = (i * f[i-1]) % mod
            g[i] = pow(f[i], mod - 2, mod)
        def dfs(room: int) -> None:
            for son in rooms[room]:
                dfs(son)
                sz[room] += sz[son]
                s[room] *= s[son] * g[sz[son]] % mod           
            s[room] *= f[sz[room]]
            s[room] %= mod
            sz[room] += 1
        dfs(0)
        return s[0]
        
