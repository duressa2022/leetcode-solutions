class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        nums.sort()
        result=[]
        for i in range(length):
            if nums[i]==target:
                result.append(i)
        return result

        