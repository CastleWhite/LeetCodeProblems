class Solution:
    stack = 0
    def generateParenthesis(self, n: int) -> List[str]:
        anss = []
        ans = []

        def backtrack(n, ans):
            if n == 0:
                ans += [')']*self.stack
                anss.append("".join(ans))
                for i in range(self.stack):
                    ans.pop()
                return 
            #choice 1: add )
            if self.stack>0:
                ans.append(')')
                self.stack -= 1
                backtrack(n, ans)
                ans.pop()
                self.stack += 1
            #choice 2: add (

            self.stack += 1
            ans.append('(')
            backtrack(n-1, ans)
            ans.pop()
            self.stack -= 1
            return
        
        backtrack(n, ans)
        return anss

