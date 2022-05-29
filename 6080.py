class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []
        for n in nums:
            m = 0
            while st and st[-1][0] <= n:
                m = max(m, st.pop()[1])
            if not st: m -= 1
            st.append((n, m+1))
        return max([y[1] for y in st])
