class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallerNumber=[]
        for i in range(len(nums)):
            counter=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                     counter+=1
            smallerNumber.append(counter)
        return smallerNumber

        