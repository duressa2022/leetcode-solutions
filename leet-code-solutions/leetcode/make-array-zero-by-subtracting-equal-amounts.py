class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter=0
        nums.sort()
        length=len(nums)
        current=0
        for i in range(length):
            if nums[i]>0:
                if nums[i]-current!=0:
                    counter+=1
                current+=nums[i]-current
        return counter
        