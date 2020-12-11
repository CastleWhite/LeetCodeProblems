class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        re = 0
        senate = list(senate)
        while senate:
            i = 0
            for _ in range(len(senate)):
                if senate[i] == 'R':
                    if re >= 0:
                        re += 1
                        i += 1
                    else:
                        re+=1
                        senate.pop(i)
                else:
                    if re > 0:
                        senate.pop(i)
                    else:
                        i += 1
                    re -= 1
            if len(senate) <= abs(re):
                if re > 0:
                    return "Radiant"
                elif re < 0:
                    return "Dire"
