class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        length=len(nums)
        counter=0
        for i in range(length):
            for j in range(i+1,length):
                if abs(nums[i]-nums[j])==k:
                    counter+=1
        return counter
        