class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ha = {5:0, 10:0, 20:0}
        def find(re: int):
            # greedy
            while re>0:
                if re>5 and ha[10] > 0:
                    ha[10] -= 1
                    re -= 10
                elif ha[5] > 0:
                    ha[5] -= 1
                    re -= 5
                else:
                    return False
            return True

        for bill in bills:

            re = bill - 5
            if not find(re):
                return False

            # if ha.has_key(bill):
            ha[bill] += 1
            # else:
            #     ha[bill] = 1
        
        return True
