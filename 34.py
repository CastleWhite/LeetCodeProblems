class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        low = -1
        high = l

        begin = 0
        end = l-1
        flag = False
        while begin <= end:
            mid = (begin+end)//2
            if nums[mid] < target:
                low = mid
                begin = mid + 1
            elif nums[mid] > target:
                high = mid
                end = mid - 1
            else:
                if not flag:
                    flag = True
                    begin2 = mid + 1
                    end2 = end
                end = mid - 1
        if not flag:
            return [-1,-1]

        while begin2 <= end2:
            mid = (begin2+end2)//2
            if nums[mid] > target:
                high = mid
                end2 = mid - 1
            else:
                begin2 = mid + 1
        return [low+1, high-1]
