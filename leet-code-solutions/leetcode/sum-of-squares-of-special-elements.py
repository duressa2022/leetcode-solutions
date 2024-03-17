class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length=len(nums)
        result=0
        for i in range(length):
            if length%(i+1)==0:
                result+=nums[i]**2
        return result

        