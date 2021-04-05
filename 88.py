class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        while m>0 and n>0:
            if nums1[m-1] < nums2[n-1]:
                nums1[l-1] = nums2[n-1]
                n -= 1
            else:
                nums1[l-1] = nums1[m-1]
                m -= 1
            l -= 1
        
        if n:
            for i in range(l):
                nums1[i] = nums2[i]
        
        

