class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        i = m - 1
        j = n - 1
        total = m + n - 1
        while(i >= 0 and j >= 0):
            if nums1[i] < nums2[j]:
                nums1[total] = nums2[j]
                j = j - 1
            else:
                nums1[total] = nums1[i]
                i = i - 1
            total = total - 1
        
        while j >= 0:
            nums1[total] = nums2[j]
            j -= 1
            total -= 1