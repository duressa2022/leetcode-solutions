class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copied_num1=[number for number in nums1]
        i=j=k=0
        while i<m and j<n:
            if copied_num1[i]<nums2[j]:
                nums1[k]=copied_num1[i]
                i=i+1
            else:
                nums1[k]=nums2[j]
                j=j+1
            k=k+1
        while i<m:
            nums1[k]=copied_num1[i]
            i=i+1
            k=k+1
        while j<n:
            nums1[k]=nums2[j]
            j=j+1
            k=k+1



        