class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        result=[]
        counter=0
        for num in nums1:
            if num in set2:
                counter+=1
        result.append(counter)
        counter=0
        for num in nums2:
            if num in set1:
                counter+=1
        result.append(counter)
        return result

        