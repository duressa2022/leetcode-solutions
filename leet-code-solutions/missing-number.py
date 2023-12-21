class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet=set(nums)
        for i in range(0,len(nums)+1):
            if i not in hashSet:
                return i

        