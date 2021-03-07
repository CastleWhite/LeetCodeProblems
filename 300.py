class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxl = 0
        l = len(nums)
        reco = [nums[0]]

        for i in range(1,l):
            if nums[i] > reco[maxl]:
                reco.append(nums[i])
                maxl += 1

            elif nums[i] == nums[i-1]:
                continue
            else:
                a = 0
                b = maxl
                loc = 0
                while a <= b:
                    mid = (a+b)//2
                    if reco[mid] < nums[i]:
                        loc = mid + 1
                        a = mid + 1
                    elif reco[mid] == nums[i]:
                        loc = mid
                        break
                    else:
                        b = mid - 1
                reco[loc] = nums[i]
        
        return maxl + 1


