class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_nums = [0]
        for i in nums:
            self.sum_nums.append(i+self.sum_nums[-1])


    def sumRange(self, i: int, j: int) -> int:
        return self.sum_nums[j+1] - self.sum_nums[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
