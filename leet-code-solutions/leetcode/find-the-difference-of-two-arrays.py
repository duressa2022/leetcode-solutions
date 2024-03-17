class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        result=[]
        temp=set()
        for num in nums1:
            if num not in set2:
                temp.add(num)
        result.append(list(temp))
        temp=set()
        for num in nums2:
            if num not in set1:
                temp.add(num)
        result.append(list(temp))
        return result



        