class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        reco = [0] * 1000

        for i in answers:
            if reco[i]:
                reco[i] -= 1
            else:
                reco[i] = i
                ans += i+1
        
        return ans
