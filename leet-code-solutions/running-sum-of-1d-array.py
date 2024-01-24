class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        sumResult=0
        for num in nums:
            sumResult+=num
            result.append(sumResult)
        return result
