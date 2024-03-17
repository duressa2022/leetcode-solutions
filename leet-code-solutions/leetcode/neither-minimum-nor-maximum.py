class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxNumber=max(nums)
        minNumber=min(nums)
        length=len(nums)
        for num in nums:
            if num!=maxNumber and num!=minNumber:
                return num
        return -1

        