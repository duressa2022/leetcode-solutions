class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        i=0
        j=1
        while j<len(nums):
            result.extend([nums[j]]*nums[i])
            i=i+2
            j=j+2
        return result
        