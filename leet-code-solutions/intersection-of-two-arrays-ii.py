from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map=Counter(nums1)
        result=[]
        for number in nums2:
            if number in hash_map:
                result.append(number)
                hash_map[number]-=1
                if hash_map[number]==0:
                    hash_map.pop(number)
        return result
        