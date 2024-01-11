class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]="_"   
        holder=-1
        for seeker in range(len(nums)):
            if nums[seeker]!="_":
                holder+=1
                (nums[seeker],nums[holder])=(nums[holder],nums[seeker])
        return len(nums)-nums.count("_")