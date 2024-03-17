class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        set3=set(nums3)
        result=set()
        for num in nums1:
            if num in  set2 or num in  set3:
                result.add(num)
        for num in nums2:
            if num in set3:
                result.add(num)
        return list(result)
        