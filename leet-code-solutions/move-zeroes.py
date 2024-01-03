class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder=-1
        for seeker in range(len(nums)):
            if nums[seeker]!=0:
                holder+=1
                (nums[seeker],nums[holder])=(nums[holder],nums[seeker])


        