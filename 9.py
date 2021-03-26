class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        elif x == 0 : return True
        elif x % 10 == 0 : return False
        
        reco = 0
        xx = x
        while xx > reco:
            reco = reco * 10 + xx % 10
            xx = xx // 10

        return xx == reco or xx == reco // 10 
