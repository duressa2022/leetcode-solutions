class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer=0
        prevNumber=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=prevNumber:
                prevNumber=nums[i]
                continue
            numberOf=ceil(nums[i]/prevNumber)
            answer+=numberOf-1
            prevNumber=nums[i]//numberOf
        return answer

        