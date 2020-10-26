class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordnums = list(nums)
        ordnums.sort()

        mydict = {}
        mydict.fromkeys(nums,-1)
        l = len(nums)

        mydict[ordnums[0]] = 0
        for i in range(1,l):
            if ordnums[i] == ordnums[i-1]:
                continue
            else:
                mydict[ordnums[i]] = i

        ans = []
        for i in nums:
            ans.append(mydict[i])

        return ans
