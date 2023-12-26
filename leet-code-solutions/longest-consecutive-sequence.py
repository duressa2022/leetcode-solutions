class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        length=-float("inf")
        counter=1
        if len(nums)==0:return 0
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                counter+=1
            elif nums[i]!=nums[i+1]:
                length=max(length,counter)
                counter=1
        return max(length,counter)


        