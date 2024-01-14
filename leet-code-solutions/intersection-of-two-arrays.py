class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set=set()
        for number in nums1:
            if number in nums2:
                hash_set.add(number)
        return list(hash_set)
        