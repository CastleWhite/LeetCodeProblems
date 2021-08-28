class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, l, r):
            if l >= r: return 
            flag = nums[r] # random better
            s = l
            for i in range(l, r): 
                if nums[i] < flag:
                    if i != s:
                        nums[i], nums[s] = nums[s], nums[i]
                    s += 1
            nums[s], nums[r] = nums[r], nums[s]
            quickSort(nums, l, s-1)
            quickSort(nums, s+1, r)
        def quickSort1(nums):
            quickSort(nums, 0, len(nums)-1)

        # quickSort1(nums)
        # -----------------worst O(n^2)

        def mergeSort(nums, l, r):
            if l == r: return nums[l:l+1]
            mid = (l + r) >> 1
            n1 = mergeSort(nums, l, mid)
            n2 = mergeSort(nums, mid+1, r)
            i, j = 0, 0
            f = l
            while i < (mid - l + 1) and j < (r - mid):
                if n1[i] < n2[j]:
                    nums[f] = n1[i]
                    i += 1
                else:
                    nums[f] = n2[j]
                    j += 1
                f += 1
            while i < (mid - l + 1):
                nums[f] = n1[i]
                i += 1
                f += 1
            while j < (r - mid):
                nums[f] = n2[j]
                j += 1
                f += 1 
            return nums[l:r+1]
        # res = mergeSort(nums, 0, len(nums)-1)
        # ------------
        def down(nums, i, l):
            lson = i<<1
            rson = i<<1 | 1
            if lson > l: return
            j = lson
            if rson <= l and nums[rson] > nums[lson]: j = rson
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                down(nums, j, l)
        def buildHeap(nums, l):
            for i in range(l>>1, 0, -1):
                down(nums, i, l)
        def heapSort(nums):
            l = len(nums)
            nums.insert(0, 0)
            buildHeap(nums, l)
            while l > 1:
                nums[1], nums[l] = nums[l], nums[1]
                l -= 1
                down(nums, 1, l)
            nums.pop(0)
        # heapSort(nums)
        return nums
