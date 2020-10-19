class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def xiao(ST: str, loc: int) -> int:
            skip = 0
            while ST[loc] == '#' or skip > 0:
                if ST[loc] == '#' :
                    skip += 1
                    
                else:
                    skip -= 1
                loc -= 1
                if loc<0:
                    return -1
            return loc

        first = len(S)-1
        second = len(T)-1
        first = xiao(S, first) 
        second = xiao(T, second) 
        while first>=0 and second>=0:                 
            if S[first] != T[second] :
                return False
            else:
                first -= 1
                second -= 1
                first = xiao(S, first) 
                second = xiao(T, second)   

        if first<0 and second<0:
            return True
        else:
            return False
