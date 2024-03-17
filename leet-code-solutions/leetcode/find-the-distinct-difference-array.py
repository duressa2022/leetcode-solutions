class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[]
        for i in range(length):
            left=len(set(nums[:i+1]))
            right=len(set(nums[i+1:]))
            result.append(left-right)
        return result
    
        