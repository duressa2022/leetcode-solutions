class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        current=float("inf")
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                if current>nums1[i]:
                    current=nums1[i]
                i=i+1
                j=j+1
            elif nums1[i]>nums2[j]:
                j=j+1
            else:
                i=i+1
        return current if current!=float("inf") else -1
        